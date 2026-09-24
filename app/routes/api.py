import json

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import Form
from fastapi import HTTPException
from fastapi import UploadFile

from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from ..database import get_db

from ..models import User
from ..models import RecommendationHistory

from ..schemas import RegisterRequest
from ..schemas import LoginRequest
from ..schemas import HomeRequest
from ..schemas import PartyRequest

from ..auth import hash_password
from ..auth import verify_password
from ..auth import create_access_token
from ..auth import COOKIE_NAME

from ..dependencies import get_current_user

from ..config import settings

from ..services.ai_service import (
    generate_recommendation
)


router = APIRouter(
    prefix="/api"
)


@router.post("/register")
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db)
):

    email = payload.email.lower()

    existing_user = (

        db.query(User)

        .filter_by(
            email=email
        )

        .first()
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail=(
                "An account with this "
                "email already exists."
            )
        )

    user = User(

        name=payload.name.strip(),

        email=email,

        password_hash=
            hash_password(
                payload.password
            )
    )

    db.add(user)

    db.commit()

    return {
        "message":
            "Registration successful"
    }


@router.post("/login")
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):

    user = (

        db.query(User)

        .filter_by(
            email=payload.email.lower()
        )

        .first()
    )

    if (
        not user
        or not verify_password(
            payload.password,
            user.password_hash
        )
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    token = create_access_token(
        user.id
    )

    response = JSONResponse({

        "message":
            "Login successful",

        "user": {

            "id": user.id,

            "name": user.name,

            "email": user.email
        }
    })

    response.set_cookie(

        COOKIE_NAME,

        token,

        httponly=True,

        samesite="lax",

        secure=settings.cookie_secure,

        max_age=86400
    )

    return response


@router.post("/logout")
def logout():

    response = JSONResponse({

        "message":
            "Logged out"
    })

    response.delete_cookie(
        COOKIE_NAME
    )

    return response


@router.get("/session-info")
def session_info(
    user: User = Depends(
        get_current_user
    )
):

    return {

        "logged_in": True,

        "user": {

            "id": user.id,

            "name": user.name,

            "email": user.email
        }
    }


@router.get("/session-data")
def session_data(
    user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):

    count = (

        db.query(
            RecommendationHistory
        )

        .filter_by(
            user_id=user.id
        )

        .count()
    )

    return {

        "user_id":
            user.id,

        "recommendation_count":
            count
    }


def save_history(
    db,
    user,
    category,
    budget,
    payload,
    result
):

    row = RecommendationHistory(

        user_id=user.id,

        category=category,

        budget=budget,

        input_json=json.dumps(
            payload,
            ensure_ascii=False
        ),

        result_json=
            result.model_dump_json()
    )

    db.add(row)

    db.commit()

    return row


@router.post("/generate-home")
def generate_home(
    payload: HomeRequest,

    user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db)
):

    result = generate_recommendation(

        "home",

        payload.budget,

        payload.model_dump()
    )

    save_history(

        db,

        user,

        "home",

        payload.budget,

        payload.model_dump(),

        result
    )

    return result


@router.post("/generate-party")
def generate_party(
    payload: PartyRequest,

    user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db)
):

    result = generate_recommendation(

        "party",

        payload.budget,

        payload.model_dump()
    )

    save_history(

        db,

        user,

        "party",

        payload.budget,

        payload.model_dump(),

        result
    )

    return result


@router.post("/generate-jewelry")
async def generate_jewelry(

    budget: float = Form(...),

    occasion: str = Form(...),

    outfit_style: str = Form(...),

    metal_preference: str = Form("Any"),

    notes: str = Form(""),

    image: UploadFile | None =
        File(None),

    user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db)
):

    if budget <= 0:

        raise HTTPException(

            status_code=422,

            detail=
                "Budget must be greater than zero."
        )

    image_bytes = None

    mime = None

    if image:

        allowed = {

            "image/jpeg",

            "image/png",

            "image/webp"
        }

        if image.content_type not in allowed:

            raise HTTPException(

                status_code=400,

                detail=
                    "Only JPG, PNG or WEBP "
                    "images are supported."
            )

        raw = await image.read()

        if (
            len(raw)
            > settings.max_upload_mb
            * 1024
            * 1024
        ):

            raise HTTPException(

                status_code=400,

                detail=(
                    f"Image must be smaller "
                    f"than {settings.max_upload_mb} MB."
                )
            )

        image_bytes = raw

        mime = image.content_type

    payload = {

        "budget": budget,

        "occasion": occasion,

        "outfit_style": outfit_style,

        "metal_preference":
            metal_preference,

        "notes": notes,

        "image_uploaded":
            bool(image_bytes)
    }

    result = generate_recommendation(

        "jewelry",

        budget,

        payload,

        image_bytes,

        mime
    )

    save_history(

        db,

        user,

        "jewelry",

        budget,

        payload,

        result
    )

    return result


@router.get("/history")
def api_history(

    user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db)
):

    rows = (

        db.query(
            RecommendationHistory
        )

        .filter_by(
            user_id=user.id
        )

        .order_by(
            RecommendationHistory.created_at.desc()
        )

        .all()
    )

    return [

        {

            "id": row.id,

            "category":
                row.category,

            "budget":
                row.budget,

            "created_at":
                row.created_at.isoformat(),

            "result":
                json.loads(
                    row.result_json
                )
        }

        for row in rows
    ]


@router.get(
    "/recommendations-details/{history_id}"
)
def recommendation_details(

    history_id: int,

    user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db)
):

    row = (

        db.query(
            RecommendationHistory
        )

        .filter_by(

            id=history_id,

            user_id=user.id
        )

        .first()
    )

    if not row:

        raise HTTPException(

            status_code=404,

            detail=
                "Recommendation not found."
        )

    return json.loads(
        row.result_json
    )
import json

from fastapi import APIRouter
from fastapi import Request
from fastapi import Depends

from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from ..database import get_db

from ..dependencies import get_current_user

from ..models import User
from ..models import RecommendationHistory


router = APIRouter()


templates = Jinja2Templates(
    directory="app/templates"
)


def render(request, template, **context):
    return templates.TemplateResponse(
        request=request,
        name=template,
        context={"request": request, **context}
    )

    return templates.TemplateResponse(
        template,
        {
            "request": request,
            **context
        }
    )


@router.get(
    "/",
    response_class=HTMLResponse
)
def home(request: Request):

    return RedirectResponse(
        "/dashboard",
        status_code=303
    )


@router.get(
    "/login",
    response_class=HTMLResponse
)
def login_page(
    request: Request
):

    return render(
        request,
        "login.html",
        title="Login"
    )


@router.get(
    "/register",
    response_class=HTMLResponse
)
def register_page(
    request: Request
):

    return render(
        request,
        "register.html",
        title="Register"
    )


@router.get(
    "/dashboard",
    response_class=HTMLResponse
)
def dashboard(
    request: Request,
    user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):

    recent = (

        db.query(
            RecommendationHistory
        )

        .filter_by(
            user_id=user.id
        )

        .order_by(
            RecommendationHistory.created_at.desc()
        )

        .limit(5)

        .all()
    )

    return render(
        request,
        "dashboard.html",
        title="Dashboard",
        user=user,
        recent=recent
    )


@router.get(
    "/planner/{category}",
    response_class=HTMLResponse
)
def planner(
    request: Request,
    category: str,
    user: User = Depends(
        get_current_user
    )
):

    if category not in {
        "home",
        "party",
        "jewelry"
    }:

        return RedirectResponse(
            "/dashboard",
            status_code=303
        )

    return render(
        request,
        "planner.html",
        title=f"{category.title()} Planner",
        user=user,
        category=category
    )


@router.get(
    "/history",
    response_class=HTMLResponse
)
def history(
    request: Request,
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

    return render(
        request,
        "history.html",
        title="History",
        user=user,
        rows=rows
    )


@router.get("/logout")
def logout():

    response = RedirectResponse(
        "/login",
        status_code=303
    )

    response.delete_cookie(
        "pocketsmart_token"
    )

    return response
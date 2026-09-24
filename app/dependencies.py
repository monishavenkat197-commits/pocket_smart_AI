from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request

from sqlalchemy.orm import Session

from .database import get_db
from .models import User

from .auth import COOKIE_NAME
from .auth import decode_access_token


def get_current_user(
    request: Request,
    db: Session = Depends(get_db)
) -> User:

    token = request.cookies.get(
        COOKIE_NAME
    )

    if not token:

        raise HTTPException(
            status_code=401,
            detail="Login required"
        )

    user_id = decode_access_token(
        token
    )

    if not user_id:

        raise HTTPException(
            status_code=401,
            detail="Session expired. Please login again."
        )

    user = db.get(
        User,
        user_id
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user
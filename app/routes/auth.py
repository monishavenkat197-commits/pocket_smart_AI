from datetime import datetime
from datetime import timedelta
from datetime import timezone

import jwt

from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

from .config import settings


password_hash = PasswordHash(
    (
        Argon2Hasher(),
    )
)


ALGORITHM = "HS256"

COOKIE_NAME = "pocketsmart_token"


def hash_password(password: str) -> str:

    return password_hash.hash(password)


def verify_password(
    password: str,
    hashed: str
) -> bool:

    try:

        return password_hash.verify(
            password,
            hashed
        )

    except Exception:

        return False


def create_access_token(
    user_id: int,
    expires_minutes: int = 60 * 24
) -> str:

    payload = {

        "sub": str(user_id),

        "exp": (
            datetime.now(timezone.utc)
            + timedelta(minutes=expires_minutes)
        )
    }

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=ALGORITHM
    )


def decode_access_token(
    token: str
):

    try:

        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[ALGORITHM]
        )

        return int(
            payload["sub"]
        )

    except (
        jwt.PyJWTError,
        KeyError,
        TypeError,
        ValueError
    ):

        return None
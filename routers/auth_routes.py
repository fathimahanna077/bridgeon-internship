from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from database import get_connection

from schemas import (
    UserRegister,
    UserLogin
)

from auth import (
    hash_password,
    verify_password,
    create_access_token,
    verify_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

security = HTTPBearer()


@router.post("/register")
def register(user: UserRegister):

    with get_connection() as conn:

        existing = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (user.email,)
        ).fetchone()

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        conn.execute(
            "INSERT INTO users(email,password) VALUES(?,?)",
            (
                user.email,
                hash_password(user.password)
            )
        )

        conn.commit()

    return {"message": "Registered"}


@router.post("/login")
def login(user: UserLogin):

    with get_connection() as conn:

        db_user = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (user.email,)
        ).fetchone()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def get_current_user(
    credentials:
    HTTPAuthorizationCredentials =
    Depends(security)
):

    token = credentials.credentials

    email = verify_token(token)

    if not email:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return email


@router.get("/me")
def me(
    current_user=Depends(
        get_current_user
    )
):
    return {"email": current_user}
from typing import Literal

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


Category = Literal[
    "home",
    "party",
    "jewelry"
]


class RegisterRequest(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=128
    )


class LoginRequest(BaseModel):

    email: EmailStr

    password: str


class RecommendationItem(BaseModel):

    title: str

    description: str

    estimated_price: float = Field(
        ge=0
    )

    platform: str

    url: str

    reason: str


class RecommendationResult(BaseModel):

    category: Category

    budget: float = Field(
        ge=0
    )

    summary: str

    allocation: dict[str, float] = {}

    recommendations: list[RecommendationItem]

    tips: list[str] = []

    source_mode: str = "demo"

    disclaimer: str = (
        "Prices and availability are estimates; "
        "verify them on the destination platform."
    )


class HomeRequest(BaseModel):

    budget: float = Field(
        gt=0
    )

    room_type: str = Field(
        min_length=2,
        max_length=50
    )

    style: str = Field(
        min_length=2,
        max_length=50
    )

    items: str = Field(
        min_length=2,
        max_length=500
    )


class PartyRequest(BaseModel):

    budget: float = Field(
        gt=0
    )

    event_type: str = Field(
        min_length=2,
        max_length=50
    )

    guests: int = Field(
        gt=0,
        le=10000
    )

    city: str = Field(
        min_length=2,
        max_length=100
    )

    preferences: str = Field(
        default="",
        max_length=500
    )


class JewelryRequest(BaseModel):

    budget: float = Field(
        gt=0
    )

    occasion: str = Field(
        min_length=2,
        max_length=50
    )

    outfit_style: str = Field(
        min_length=2,
        max_length=100
    )

    metal_preference: str = Field(
        default="Any",
        max_length=50
    )

    notes: str = Field(
        default="",
        max_length=500
    )
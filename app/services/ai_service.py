import json

from typing import Any

from pydantic import ValidationError

from .catalog_service import demo_catalog

from ..config import settings

from ..schemas import RecommendationResult


def _fallback(
    category: str,
    budget: float,
    data: dict[str, Any],
    image_bytes: bytes | None = None
):

    if category == "home":

        allocation = {

            "lighting":
                round(budget * 0.15, 2),

            "furniture":
                round(budget * 0.45, 2),

            "decor":
                round(budget * 0.25, 2),

            "storage":
                round(budget * 0.15, 2),
        }

        query = (
            f"{data.get('room_type', 'room')} "
            f"{data.get('style', 'modern')} decor"
        )

        tips = [

            "Prioritize essential furniture first.",

            "Compare dimensions before purchasing.",

            "Keep a small amount for installation "
            "or delivery.",
        ]

    elif category == "party":

        allocation = {

            "food":
                round(budget * 0.45, 2),

            "decoration":
                round(budget * 0.20, 2),

            "venue":
                round(budget * 0.25, 2),

            "contingency":
                round(budget * 0.10, 2),
        }

        query = (
            f"{data.get('event_type', 'party')} "
            f"party for {data.get('guests', 1)} guests"
        )

        tips = [

            "Reserve a contingency amount.",

            "Confirm guest count before ordering food.",

            "Compare venue rules and inclusions.",
        ]

    else:

        allocation = {

            "jewelry":
                round(budget * 0.85, 2),

            "contingency":
                round(budget * 0.15, 2),
        }

        query = (
            f"{data.get('occasion', 'occasion')} "
            f"{data.get('outfit_style', 'classic')} jewelry"
        )

        tips = [

            "Match the jewelry to the outfit neckline "
            "and style.",

            "Check material and return policy before buying.",

            "If purchasing precious metal, verify "
            "hallmark/certification details.",
        ]

    items = demo_catalog(
        category,
        query,
        max(budget, 1000)
    )

    return RecommendationResult(

        category=category,

        budget=budget,

        summary=(
            f"Demo recommendations prepared for "
            f"your {category} plan within a budget "
            f"of ₹{budget:,.0f}."
        ),

        allocation=allocation,

        recommendations=items,

        tips=tips,

        source_mode="demo",
    )


def _prompt(
    category: str,
    budget: float,
    data: dict[str, Any]
):

    return f"""
You are PocketSmart AI,
a budget-aware recommendation assistant.

Create practical recommendations
for the category: {category}.

User budget: INR {budget}.

User details:
{json.dumps(data, ensure_ascii=False)}

Rules:

1. Never exceed the total budget.

2. Give realistic estimated prices,
not guaranteed live prices.

3. Give 4 to 6 useful options.

4. Mention platform/search destination
only as a place to compare products
or services.

5. Do not claim live inventory,
exact availability, or exact current prices.

6. Give a simple budget allocation.

7. Give 3 practical tips.

8. Return ONLY valid JSON matching
the requested schema.
"""


def generate_recommendation(
    category: str,
    budget: float,
    data: dict[str, Any],
    image_bytes: bytes | None = None,
    image_mime: str | None = None
):

    # -------------------------------------------------
    # DEMO MODE
    # -------------------------------------------------

    if not settings.gemini_api_key:

        return _fallback(
            category,
            budget,
            data,
            image_bytes
        )

    # -------------------------------------------------
    # GEMINI MODE
    # -------------------------------------------------

    try:

        from google import genai

        from google.genai import types

        client = genai.Client(
            api_key=settings.gemini_api_key
        )

        contents = [

            _prompt(
                category,
                budget,
                data
            )
        ]

        # Optional image for Jewelry Planner

        if image_bytes:

            contents.append(

                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type=image_mime or "image/jpeg"
                )
            )

            contents.append(
                """
Analyze the uploaded outfit image only
for general style, color and occasion matching.

Do not identify the person.
"""
            )

        response = client.models.generate_content(

            model=settings.gemini_model,

            contents=contents,

            config=types.GenerateContentConfig(

                response_mime_type="application/json",

                response_schema=
                    RecommendationResult.model_json_schema(),

                temperature=0.4,
            )
        )

        text = response.text or ""

        result = (
            RecommendationResult
            .model_validate_json(text)
        )

        return result

    except (
        ValidationError,
        ValueError,
        TypeError,
        Exception
    ):

        return _fallback(
            category,
            budget,
            data,
            image_bytes
        )
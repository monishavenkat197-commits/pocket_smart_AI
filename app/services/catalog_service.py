from typing import Any


def demo_catalog(
    category: str,
    query: str,
    budget: float
) -> list[dict[str, Any]]:

    if category == "home":
        return [
            {
                "title": "Modern LED Ceiling Light",
                "description": "Simple lighting option for a modern room.",
                "estimated_price": min(1500, budget),
                "platform": "Amazon / Flipkart",
                "url": "https://www.amazon.in/",
                "reason": "Useful for improving room lighting."
            },
            {
                "title": "Compact Storage Cabinet",
                "description": "Space-saving storage for everyday items.",
                "estimated_price": min(4500, budget),
                "platform": "Amazon / Flipkart",
                "url": "https://www.amazon.in/",
                "reason": "Helps organize the room efficiently."
            },
            {
                "title": "Decorative Wall Art",
                "description": "Simple wall decoration for a modern interior.",
                "estimated_price": min(1200, budget),
                "platform": "Amazon / Flipkart",
                "url": "https://www.amazon.in/",
                "reason": "Adds decoration without using much budget."
            },
            {
                "title": "Small Side Table",
                "description": "Compact table suitable for bedrooms or living rooms.",
                "estimated_price": min(2500, budget),
                "platform": "Amazon / Flipkart",
                "url": "https://www.amazon.in/",
                "reason": "Useful and practical furniture choice."
            }
        ]

    if category == "party":
        return [
            {
                "title": "Party Decoration Set",
                "description": "Basic decoration items for a small celebration.",
                "estimated_price": min(1500, budget),
                "platform": "Amazon / Flipkart",
                "url": "https://www.amazon.in/",
                "reason": "Covers common decoration needs."
            },
            {
                "title": "Cake and Dessert Package",
                "description": "Budget-friendly option for party food.",
                "estimated_price": min(2500, budget),
                "platform": "Local bakery",
                "url": "https://www.google.com/",
                "reason": "Suitable for a small celebration."
            },
            {
                "title": "Party Venue",
                "description": "Example venue category to compare locally.",
                "estimated_price": min(5000, budget),
                "platform": "Local venues",
                "url": "https://www.google.com/",
                "reason": "Helps compare venue options within budget."
            },
            {
                "title": "Party Return Gifts",
                "description": "Simple gifts for guests.",
                "estimated_price": min(1000, budget),
                "platform": "Amazon / Flipkart",
                "url": "https://www.amazon.in/",
                "reason": "Useful for guest appreciation."
            }
        ]

    return [
        {
            "title": "Classic Earrings",
            "description": "Simple earrings suitable for traditional occasions.",
            "estimated_price": min(1500, budget),
            "platform": "Jewellery stores",
            "url": "https://www.google.com/",
            "reason": "Easy to match with traditional outfits."
        },
        {
            "title": "Pendant Necklace",
            "description": "Minimal necklace for casual or festive outfits.",
            "estimated_price": min(2500, budget),
            "platform": "Jewellery stores",
            "url": "https://www.google.com/",
            "reason": "Versatile option for different outfits."
        },
        {
            "title": "Bangle Set",
            "description": "Decorative bangle set for traditional wear.",
            "estimated_price": min(1200, budget),
            "platform": "Jewellery stores",
            "url": "https://www.google.com/",
            "reason": "Works well with traditional styling."
        },
        {
            "title": "Simple Bracelet",
            "description": "Minimal bracelet for everyday styling.",
            "estimated_price": min(1000, budget),
            "platform": "Jewellery stores",
            "url": "https://www.google.com/",
            "reason": "Simple accessory for regular use."
        }
    ]
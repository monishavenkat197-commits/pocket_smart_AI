from urllib.parse import quote_plus


def search_url(
    platform: str,
    query: str
) -> str:

    q = quote_plus(query)

    bases = {

        "Amazon":
            f"https://www.amazon.in/s?k={q}",

        "Flipkart":
            f"https://www.flipkart.com/search?q={q}",

        "IKEA":
            f"https://www.ikea.com/in/en/search/?q={q}",

        "Swiggy":
            f"https://www.swiggy.com/search?query={q}",

        "Zomato":
            f"https://www.zomato.com/search?query={q}",

        "OYO":
            f"https://www.oyorooms.com/search?location={q}",
    }

    return bases.get(
        platform,
        f"https://www.google.com/search?q={q}"
    )


def demo_catalog(
    category: str,
    query: str,
    budget: float
):

    if category == "home":

        data = [

            (
                "LED Ceiling Light",
                "Amazon",
                899,
                "Energy-efficient ceiling light"
            ),

            (
                "Minimal Wall Art Set",
                "IKEA",
                1299,
                "Simple wall decor for a modern room"
            ),

            (
                "Storage Side Table",
                "Flipkart",
                1799,
                "Compact furniture with storage"
            ),

            (
                "Decorative Cushion Set",
                "Amazon",
                699,
                "Accent cushions for a coordinated look"
            ),

            (
                "Study/Task Lamp",
                "IKEA",
                999,
                "Useful focused lighting"
            ),
        ]

    elif category == "party":

        data = [

            (
                "Birthday Food Combo",
                "Swiggy",
                2499,
                "Food package idea for a small group"
            ),

            (
                "Party Catering Search",
                "Zomato",
                3499,
                "Catering options to compare"
            ),

            (
                "Decoration Kit",
                "Amazon",
                999,
                "Reusable balloons and decoration supplies"
            ),

            (
                "Event Venue Search",
                "OYO",
                4999,
                "Accommodation/venue search reference"
            ),

            (
                "Table Decor Set",
                "Flipkart",
                799,
                "Low-cost table decoration"
            ),
        ]

    else:

        data = [

            (
                "Pearl Stud Earrings",
                "Amazon",
                799,
                "Versatile option for traditional or casual outfits"
            ),

            (
                "Minimal Pendant Necklace",
                "Flipkart",
                1299,
                "Simple necklace for many occasions"
            ),

            (
                "Oxidised Jhumka Style",
                "Amazon",
                699,
                "Statement option for ethnic outfits"
            ),

            (
                "Silver-Tone Bracelet",
                "Flipkart",
                999,
                "Minimal accessory for a clean look"
            ),

            (
                "Classic Bangle Set",
                "Amazon",
                899,
                "Works well with festive styling"
            ),
        ]

    results = []

    for title, platform, price, description in data:

        if price <= budget:

            results.append({

                "title": title,

                "description": description,

                "estimated_price": price,

                "platform": platform,

                "url": search_url(
                    platform,
                    query
                ),

                "reason":
                    "Fits the requested category "
                    "and is within a practical demo "
                    "budget range.",
            })

    if not results:

        title, platform, price, description = data[0]

        results.append({

            "title": title,

            "description": description,

            "estimated_price": price,

            "platform": platform,

            "url": search_url(
                platform,
                query
            ),

            "reason":
                "Shown as a fallback because "
                "the budget is below the demo "
                "catalog prices.",
        })

    return results[:5]
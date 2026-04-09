from urllib.parse import quote

from flask import Flask, abort, render_template, url_for


app = Flask(__name__)

SHOPS = [
    {
        "id": "shop1",
        "name": "Sunset Bites",
        "tagline": "Street food with rooftop warmth",
        "counter": "Counter 01",
        "location": "Barasat, Kolkata",
        "hours": "10:00 AM - 11:00 PM",
        "phone": "+91 98765 12001",
        "email": "sunset@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Jaipur%20Rajasthan&output=embed",
        "about": "A lively flagship outlet serving fast-moving Indian fusion plates, family combos, and late-evening desserts.",
        "featured_review": {
            "author": "Riya",
            "stars": 5,
            "text": "Fast service, bright flavors, and the paneer tikka wrap was genuinely memorable.",
        },
    },
    {
        "id": "shop2",
        "name": "Harbor Spice",
        "tagline": "Coastal bowls and fire-grilled mains",
        "counter": "Counter 02",
        "location": "Barasat, Kolkata",
        "hours": "11:00 AM - 11:30 PM",
        "phone": "+91 98765 12002",
        "email": "harbor@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Mumbai%20Maharashtra&output=embed",
        "about": "Designed for busy lunch crowds and dinner groups, this branch balances bold spice with polished presentation.",
        "featured_review": {
            "author": "Aman",
            "stars": 4,
            "text": "The grilled fish bowl was fresh and filling, and the staff handled a busy night really well.",
        },
    },
    {
        "id": "shop3",
        "name": "Citrus Kitchen",
        "tagline": "Healthy plates with cafe energy",
        "counter": "Counter 03",
        "location": "Barasat, Kolkata",
        "hours": "8:30 AM - 10:30 PM",
        "phone": "+91 98765 12003",
        "email": "citrus@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Bengaluru%20Karnataka&output=embed",
        "about": "A modern neighborhood stop for breakfast, coworking lunches, and lighter evening meals.",
        "featured_review": {
            "author": "Neha",
            "stars": 5,
            "text": "Loved the orange ambience and the smoothie pairing suggestions from the team.",
        },
    },
    {
        "id": "shop4",
        "name": "Ember Thali",
        "tagline": "Regional comfort in a polished setting",
        "counter": "Counter 04",
        "location": "Barasat, Kolkata",
        "hours": "12:00 PM - 10:30 PM",
        "phone": "+91 98765 12004",
        "email": "ember@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Ahmedabad%20Gujarat&output=embed",
        "about": "Known for plated regional meals, family seating, and a rotating chef-special dessert counter.",
        "featured_review": {
            "author": "Karan",
            "stars": 4,
            "text": "Very good thali portions and a clean, well-managed dining area for families.",
        },
    },
    {
        "id": "shop5",
        "name": "Ember Thali",
        "tagline": "Regional comfort in a polished setting",
        "counter": "Counter 05",
        "location": "Barasat, Kolkata",
        "hours": "12:00 PM - 10:30 PM",
        "phone": "+91 98765 12004",
        "email": "ember@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Ahmedabad%20Gujarat&output=embed",
        "about": "Known for plated regional meals, family seating, and a rotating chef-special dessert counter.",
        "featured_review": {
            "author": "Karan",
            "stars": 4,
            "text": "Very good thali portions and a clean, well-managed dining area for families.",
        },
    },
    {
        "id": "shop6",
        "name": "Ember Thali",
        "tagline": "Regional comfort in a polished setting",
        "counter": "Counter 06",
        "location": "Barasat, Kolkata",
        "hours": "12:00 PM - 10:30 PM",
        "phone": "+91 98765 12004",
        "email": "ember@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Ahmedabad%20Gujarat&output=embed",
        "about": "Known for plated regional meals, family seating, and a rotating chef-special dessert counter.",
        "featured_review": {
            "author": "Karan",
            "stars": 4,
            "text": "Very good thali portions and a clean, well-managed dining area for families.",
        },
    },
    {
        "id": "shop7",
        "name": "Ember Thali",
        "tagline": "Regional comfort in a polished setting",
        "counter": "Counter 07",
        "location": "Barasat, Kolkata",
        "hours": "12:00 PM - 10:30 PM",
        "phone": "+91 98765 12004",
        "email": "ember@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Ahmedabad%20Gujarat&output=embed",
        "about": "Known for plated regional meals, family seating, and a rotating chef-special dessert counter.",
        "featured_review": {
            "author": "Karan",
            "stars": 4,
            "text": "Very good thali portions and a clean, well-managed dining area for families.",
        },
    },
    {
        "id": "shop8",
        "name": "Ember Thali",
        "tagline": "Regional comfort in a polished setting",
        "counter": "Counter 08",
        "location": "Barasat, Kolkata",
        "hours": "12:00 PM - 10:30 PM",
        "phone": "+91 98765 12004",
        "email": "ember@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Ahmedabad%20Gujarat&output=embed",
        "about": "Known for plated regional meals, family seating, and a rotating chef-special dessert counter.",
        "featured_review": {
            "author": "Karan",
            "stars": 4,
            "text": "Very good thali portions and a clean, well-managed dining area for families.",
        },
    },
    {
        "id": "shop9",
        "name": "Ember Thali",
        "tagline": "Regional comfort in a polished setting",
        "counter": "Counter 09",
        "location": "Barasat, Kolkata",
        "hours": "12:00 PM - 10:30 PM",
        "phone": "+91 98765 12004",
        "email": "ember@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Ahmedabad%20Gujarat&output=embed",
        "about": "Known for plated regional meals, family seating, and a rotating chef-special dessert counter.",
        "featured_review": {
            "author": "Karan",
            "stars": 4,
            "text": "Very good thali portions and a clean, well-managed dining area for families.",
        },
    },
    {
        "id": "shop10",
        "name": "Ember Thali",
        "tagline": "Regional comfort in a polished setting",
        "counter": "Counter 10",
        "location": "Barasat, Kolkata",
        "hours": "12:00 PM - 10:30 PM",
        "phone": "+91 98765 12004",
        "email": "ember@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Ahmedabad%20Gujarat&output=embed",
        "about": "Known for plated regional meals, family seating, and a rotating chef-special dessert counter.",
        "featured_review": {
            "author": "Karan",
            "stars": 4,
            "text": "Very good thali portions and a clean, well-managed dining area for families.",
        },
    },
    {
        "id": "shop11",
        "name": "Ember Thali",
        "tagline": "Regional comfort in a polished setting",
        "counter": "Counter 11",
        "location": "Barasat, Kolkata",
        "hours": "12:00 PM - 10:30 PM",
        "phone": "+91 98765 12004",
        "email": "ember@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Ahmedabad%20Gujarat&output=embed",
        "about": "Known for plated regional meals, family seating, and a rotating chef-special dessert counter.",
        "featured_review": {
            "author": "Karan",
            "stars": 4,
            "text": "Very good thali portions and a clean, well-managed dining area for families.",
        },
    },
    {
        "id": "shop12",
        "name": "Ember Thali",
        "tagline": "Regional comfort in a polished setting",
        "counter": "Counter 12",
        "location": "Barasat, Kolkata",
        "hours": "12:00 PM - 10:30 PM",
        "phone": "+91 98765 12004",
        "email": "ember@foodcompany.com",
        "map_embed": "https://www.google.com/maps?q=Ahmedabad%20Gujarat&output=embed",
        "about": "Known for plated regional meals, family seating, and a rotating chef-special dessert counter.",
        "featured_review": {
            "author": "Karan",
            "stars": 4,
            "text": "Very good thali portions and a clean, well-managed dining area for families.",
        },
    },
]

SHOP_LOOKUP = {shop["id"]: shop for shop in SHOPS}

ITEMS = [
    {
        "id": "item1",
        "name": "Chicken Cheeseball",
        "price": "₹40",
        "description": "Layers of slow-cooked chickpeas, tamarind glaze, and crunchy sev for a savory meal in one bowl.",
        "more": "Ready in 15 minutes, served with fresh herbs, pickled onions, and a squeeze of lime.",
    },
    {
        "id": "item2",
        "name": "Chicken pakora",
        "price": "₹199",
        "description": "Crisp greens, roasted paneer, and mint chutney wrapped in a soft flatbread.",
        "more": "A fresh handheld option with zingy dressing and seasonal vegetables.",
    },
    {
        "id": "item3",
        "name": "Chicken wings",
        "price": "₹279",
        "description": "Creamy coconut curry with garden vegetables, jasmine rice, and toasted nuts.",
        "more": "A comforting, rich bowl that balances sweet coconut with aromatic spices.",
    },
    {
        "id": "item4",
        "name": "fish finger",
        "price": "₹249",
        "description": "Layers of slow-cooked chickpeas, tamarind glaze, and crunchy sev for a savory meal in one bowl.",
        "more": "Ready in 15 minutes, served with fresh herbs, pickled onions, and a squeeze of lime.",
    },
    {
        "id": "item5",
        "name": "fish pakora",
        "price": "₹199",
        "description": "Crisp greens, roasted paneer, and mint chutney wrapped in a soft flatbread.",
        "more": "A fresh handheld option with zingy dressing and seasonal vegetables.",
    },
    {
        "id": "item6",
        "name": "Coconut Karahi Bowl",
        "price": "₹279",
        "description": "Creamy coconut curry with garden vegetables, jasmine rice, and toasted nuts.",
        "more": "A comforting, rich bowl that balances sweet coconut with aromatic spices.",
    },
]

ITEM_LOOKUP = {item["id"]: item for item in ITEMS}

REVIEWS = [
    {"shop_id": "shop1", "author": "Priya", "stars": 5, "text": "The wraps came out hot, fast, and full of flavor."},
    {"shop_id": "shop2", "author": "Dev", "stars": 4, "text": "Excellent spice balance and a strong seafood menu."},
    {"shop_id": "shop3", "author": "Ishita", "stars": 5, "text": "Perfect stop for a fresh lunch and coffee break."},
    {"shop_id": "shop4", "author": "Rahul", "stars": 4, "text": "Comforting food, calm service, and generous portions."},
    {"shop_id": "shop1", "author": "Sana", "stars": 5, "text": "The dessert counter alone makes this place worth revisiting."},
    {"shop_id": "shop3", "author": "Arjun", "stars": 4, "text": "Bright interiors, healthy food, and quick table turnaround."},
]

CONTACT_REVIEWS = [
    {"name": "Maya", "stars": 5, "message": "Admin support was fast when I needed help with a large catering order."},
    {"name": "Kabir", "stars": 4, "message": "Good response time and clear follow-up from the customer support team."},
    {"name": "Simran", "stars": 5, "message": "Helpful team, polite communication, and smooth reservation handling."},
]


def stars(value: int) -> str:
    return "★" * value + "☆" * (5 - value)


@app.context_processor
def inject_helpers():
    return {"render_stars": stars, "shop_lookup": SHOP_LOOKUP}


@app.route("/")
def home():
    return render_template(
        "main.html",
        shops=SHOPS[:4],
        hero_shop=SHOPS[0],
        featured_items=ITEMS[:4],
        reviews=REVIEWS[:6],
        hero_image=url_for('static', filename='food.png'),
    )


@app.route("/shops")
def shops():
    return render_template(
        "shop.html",
        shops=SHOPS,
        hero_shop=SHOPS[0],
        hero_image=url_for('static', filename='food.png'),
    )


@app.route("/shops/<shop_id>")
def shop_detail(shop_id: str):
    shop = SHOP_LOOKUP.get(shop_id)
    if not shop:
        abort(404)
    related_reviews = [review for review in REVIEWS if review["shop_id"] == shop_id]
    return render_template(
        "shop_detail.html",
        shop=shop,
        reviews=related_reviews,
        hero_image=url_for('static', filename='food.png'),
    )


@app.route("/items")
def items():
    return render_template(
        "items.html",
        items=ITEMS,
        hero_image=url_for('static', filename='food.png'),
    )


@app.route("/items/<item_id>")
def item_detail(item_id: str):
    item = ITEM_LOOKUP.get(item_id)
    if not item:
        abort(404)
    return render_template(
        "item_detail.html",
        item=item,
        hero_image=url_for('static', filename='food.png'),
    )


@app.route("/reviews")
def reviews():
    return render_template("reviews.html", reviews=REVIEWS)


@app.route("/contact")
def contact():
    return render_template("contact.html", contact_reviews=CONTACT_REVIEWS)


if __name__ == "__main__":
    app.run(debug=True, port=8000)


# 
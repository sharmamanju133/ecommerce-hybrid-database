from pymongo import MongoClient
from faker import Faker
import random
from datetime import datetime

# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_nosql"]

fake = Faker()

# collections
products_col = db["products"]
reviews_col = db["reviews"]
logs_col = db["product_logs"]
activity_col = db["user_activity"]
wishlist_col = db["wishlist"]

# generate products
products = []
for i in range(1, 101):
    products.append({
        "product_id": i,
        "name": fake.word().capitalize(),
        "category": random.choice(["Electronics", "Clothing", "Books"]),
        "price": random.randint(100, 5000),
        "stock": random.randint(1, 200),
        "created_at": datetime.now()
    })

products_col.insert_many(products)

# generate reviews
reviews = []
for i in range(1, 101):
    reviews.append({
        "review_id": i,
        "product_id": random.randint(1, 100),
        "user": fake.name(),
        "rating": random.randint(1, 5),
        "comment": fake.sentence(),
        "date": datetime.now()
    })

reviews_col.insert_many(reviews)

# generate logs
logs = []
for i in range(1, 101):
    logs.append({
        "log_id": i,
        "product_id": random.randint(1, 100),
        "action": random.choice(["created", "updated", "deleted"]),
        "timestamp": datetime.now()
    })

logs_col.insert_many(logs)

# generate user activity
activities = []
for i in range(1, 101):
    activities.append({
        "activity_id": i,
        "user": fake.name(),
        "action": random.choice(["view", "add_to_cart", "purchase"]),
        "product_id": random.randint(1, 100),
        "time": datetime.now()
    })

activity_col.insert_many(activities)

# generate wishlist
wishlists = []
for i in range(1, 101):
    wishlists.append({
        "wishlist_id": i,
        "user": fake.name(),
        "products": [random.randint(1, 100) for _ in range(3)],
        "created_at": datetime.now()
    })

wishlist_col.insert_many(wishlists)

print("Data inserted successfully!")
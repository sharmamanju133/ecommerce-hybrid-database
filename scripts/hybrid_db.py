import mysql.connector
from pymongo import MongoClient


# Helper: Convert SQL Product ID → Mongo ID

def convert_product_id(sql_product_id):
    # Example: P101 → 101
    try:
        return int(sql_product_id.replace("P", ""))
    except:
        return None


# MySQL CONNECTION

mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce_db"
)

mysql_cursor = mysql_conn.cursor(dictionary=True)


# MongoDB CONNECTION

mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["ecommerce_nosql"]

products_col = mongo_db["products"]

print("Connected to both databases successfully")



# Example 1: User + Product

mysql_cursor.execute("SELECT * FROM Users LIMIT 1")
user = mysql_cursor.fetchone()

mongo_product_1 = products_col.find_one({"product_id": 1})

print("\n--- Hybrid Output Example 1 ---")
print("User from SQL:", user)
print("Product from MongoDB:", mongo_product_1)



# Example 2: Order + Product

mysql_cursor.execute("SELECT * FROM Orders LIMIT 1")
order = mysql_cursor.fetchone()

# static mapping (you can improve later)
mongo_product_2 = products_col.find_one({"product_id": 1})

print("\n--- Hybrid Output Example 2 ---")
print("Order from SQL:", order)
print("Product from MongoDB:", mongo_product_2)



# Example 3: OrderItems + Mongo Products

mysql_cursor.execute("SELECT * FROM OrderItems LIMIT 3")
order_items = mysql_cursor.fetchall()

print("\n--- Order Items with Product Details ---")

for item in order_items:
    mongo_id = convert_product_id(item["product_id"])
    mongo_product = products_col.find_one({"product_id": mongo_id})

    print(f"Order ID: {item['order_id']}")
    print(f"Product ID (SQL): {item['product_id']}")

    if mongo_product:
        print(f"Product Name: {mongo_product['name']}")
        print(f"Price: {mongo_product['price']}")
    else:
        print("Product Name: Not Found")
        print("Price: N/A")

    print(f"Quantity: {item['quantity']}")



# FINAL CLEAN OUTPUT

print("\nHYBRID DATABASE OUTPUT\n")

print("USER DETAILS (SQL)")
print(f"ID: {user['user_id']}")
print(f"Name: {user['name']}")
print(f"Email: {user['email']}")


print("ORDER DETAILS (SQL)")
print(f"Order ID: {order['order_id']}")
print(f"User ID: {order['user_id']}")
print(f"Total Amount: {order['total_amount']}")


print("PRODUCT DETAILS (MongoDB)")

if mongo_product_2:
    print(f"Product ID: {mongo_product_2['product_id']}")
    print(f"Name: {mongo_product_2['name']}")
    print(f"Category: {mongo_product_2['category']}")
    print(f"Price: {mongo_product_2['price']}")
else:
    print("Product not found in MongoDB")



print("FINAL COMBINED VIEW")

if mongo_product_2:
    print(f"{user['name']} purchased {mongo_product_2['name']} for ₹{order['total_amount']}")
else:
    print("Product details missing")



# RAW COMBINED VIEW

print("\n--- Combined Business View ---")

combined = {
    "user": user,
    "order": order,
    "product": mongo_product_2
}

for key, value in combined.items():
    print(f"{key.upper()}:", value)
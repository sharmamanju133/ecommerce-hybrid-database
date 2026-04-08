import mysql.connector
from faker import Faker
import random

fake = Faker()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce_db"
)

cursor = conn.cursor()


# 1. Generate Users

for _ in range(100):
    name = fake.name()
    email = fake.unique.email()
    
    cursor.execute("""
        INSERT INTO Users (name, email)
        VALUES (%s, %s)
    """, (name, email))

conn.commit()


# 2. Generate Addresses

for user_id in range(1, 101):
    cursor.execute("""
        INSERT INTO Addresses (user_id, city, country, postal_code)
        VALUES (%s, %s, %s, %s)
    """, (
        user_id,
        fake.city(),
        fake.country(),
        fake.postcode()
    ))

conn.commit()


# 3. Generate Categories

categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']

for cat in categories:
    cursor.execute("""
        INSERT INTO Categories (category_name)
        VALUES (%s)
    """, (cat,))

conn.commit()


# 4. Generate Products

for i in range(100):
    product_id = f"P{i+200}"
    category_id = random.randint(1, 5)
    price = random.randint(10, 1000)

    cursor.execute("""
        INSERT INTO Products (product_id, category_id, price)
        VALUES (%s, %s, %s)
    """, (product_id, category_id, price))

conn.commit()


# 5. Generate Orders

for _ in range(100):
    user_id = random.randint(1, 100)
    address_id = user_id
    total_amount = random.randint(20, 1000)

    cursor.execute("""
        INSERT INTO Orders (user_id, address_id, order_date, total_amount)
        VALUES (%s, %s, CURDATE(), %s)
    """, (user_id, address_id, total_amount))

conn.commit()


# 6. Generate OrderItems

for order_id in range(1, 101):
    for _ in range(random.randint(1, 3)):
        product_id = f"P{random.randint(200, 299)}"
        quantity = random.randint(1, 5)
        price = random.randint(10, 1000)

        cursor.execute("""
            INSERT INTO OrderItems (order_id, product_id, quantity, price)
            VALUES (%s, %s, %s, %s)
        """, (order_id, product_id, quantity, price))

conn.commit()


# 7. Generate Payments

methods = ['Credit Card', 'PayPal', 'Debit Card']

for order_id in range(1, 101):
    cursor.execute("""
        INSERT INTO Payments (order_id, amount, payment_method, payment_status)
        VALUES (%s, %s, %s, %s)
    """, (
        order_id,
        random.randint(20, 1000),
        random.choice(methods),
        'Completed'
    ))

conn.commit()


# 8. Generate Cart

for user_id in range(1, 101):
    cursor.execute("""
        INSERT INTO Cart (user_id)
        VALUES (%s)
    """, (user_id,))

conn.commit()


# 9. Generate CartItems

for cart_id in range(1, 101):
    for _ in range(random.randint(1, 3)):
        cursor.execute("""
            INSERT INTO CartItems (cart_id, product_id, quantity)
            VALUES (%s, %s, %s)
        """, (
            cart_id,
            f"P{random.randint(200, 299)}",
            random.randint(1, 3)
        ))

conn.commit()


# 10. Generate Shipments

statuses = ['Pending', 'Shipped', 'Delivered']

for order_id in range(1, 101):
    cursor.execute("""
        INSERT INTO Shipments (order_id, shipment_status, delivery_date)
        VALUES (%s, %s, CURDATE())
    """, (
        order_id,
        random.choice(statuses)
    ))

conn.commit()

print("Data generation completed successfully!")

cursor.close()
conn.close()
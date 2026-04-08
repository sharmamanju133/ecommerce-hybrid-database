# E-Commerce Hybrid Database Scripts

This folder contains Python scripts to generate and manage test data for a hybrid e-commerce database system that uses both **MySQL** (relational) and **MongoDB** (NoSQL).

## Overview

- **generate_sql_data.py** - Generates test data for the MySQL relational database
- **generate_mongo_data.py** - Generates test data for the MongoDB NoSQL database
- **hybrid_db.py** - Demonstrates querying and working with both databases simultaneously

## Prerequisites

### Required Software
- Python 3.x installed
- MySQL Server running on `localhost:3306`
- MongoDB running on `localhost:27017`

### Required Python Libraries

Install dependencies using pip:

```bash
pip install mysql-connector-python pymongo faker
```

Or install from a requirements.txt file:
```bash
pip install -r requirements.txt
```

## Database Setup

### MySQL Setup

1. Make sure MySQL Server is running
2. Create the database and user (or update connection credentials in the scripts):
   ```sql
   CREATE DATABASE ecommerce_db;
   ```
3. Create the required tables before running `generate_sql_data.py`:
   - Users (name, email, etc.)
   - Addresses (user_id, city, country, postal_code)
   - Categories (Electronics, Clothing, Books, Home, Sports)
   - Products (product_id, name, price, etc.)
   - Orders (user_id, product_id, quantity, order_date)

**Note:** Update the connection credentials in each script if your MySQL setup differs:
```python
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",        # Change if needed
    password="root",    # Change if needed
    database="ecommerce_db"
)
```

### MongoDB Setup

1. Make sure MongoDB is running on `localhost:27017`
2. The database `ecommerce_nosql` will be created automatically when the script runs
3. Collections are created as needed:
   - products
   - reviews
   - product_logs
   - user_activity
   - wishlist

**Note:** Update the connection URL in each script if your MongoDB setup differs:
```python
client = MongoClient("mongodb://localhost:27017/")
```

## Running the Scripts

### 1. Generate MySQL Data

```bash
python generate_sql_data.py
```

**What it does:**
- Inserts 100 test users with names and emails
- Creates addresses for each user (city, country, postal code)
- Populates product categories
- Generates product data
- Creates sample orders

**Output:** Test data in MySQL `ecommerce_db` database

### 2. Generate MongoDB Data

```bash
python generate_mongo_data.py
```

**What it does:**
- Creates 100 products with names, categories, prices, and stock levels
- Generates 100 reviews with ratings and comments
- Creates product logs for audit trails
- Generates user activity records
- Creates user wishlist entries

**Output:** Test data in MongoDB `ecommerce_nosql` database

### 3. Query Both Databases (Hybrid)

```bash
python hybrid_db.py
```

**What it does:**
- Connects to both MySQL and MongoDB
- Demonstrates querying data from SQL (Users)
- Demonstrates querying data from MongoDB (Products)
- Shows how to work with both databases in a single application

**Output:** 
- Confirms successful connections to both databases
- Displays sample data from SQL: User information
- Displays sample data from MongoDB: Product information

## Script Details

### generate_sql_data.py
- **Dependencies:** mysql-connector-python, faker
- **Generates:** 100 users, addresses, categories, products, and orders
- **Database:** MySQL (ecommerce_db)

### generate_mongo_data.py
- **Dependencies:** pymongo, faker
- **Generates:** 100 products, reviews, logs, user activity, wishlist entries
- **Database:** MongoDB (ecommerce_nosql)
- **Collections:** products, reviews, product_logs, user_activity, wishlist

### hybrid_db.py
- **Dependencies:** mysql-connector-python, pymongo
- **Purpose:** Demonstrates querying both databases
- **Includes:** SQL and MongoDB connection examples

## Troubleshooting

### MySQL Connection Error
- Ensure MySQL Server is running: `mysql --version`
- Check credentials (default: root/root)
- Verify database `ecommerce_db` exists
- Check if tables exist and are properly created

### MongoDB Connection Error
- Ensure MongoDB is running: Check MongoDB status in Services
- Verify MongoDB is listening on `localhost:27017`
- Check MongoDB logs for connection issues

### Missing Python Packages
```bash
pip install --upgrade mysql-connector-python pymongo faker
```

### Permission Denied Error
- Run terminal as Administrator (if on Windows)
- Or use virtual environment: `python -m venv venv` then activate

## Example Usage Workflow

```bash
# 1. Install dependencies
pip install mysql-connector-python pymongo faker

# 2. Start MySQL and MongoDB services
# (Ensure both are running)

# 3. Create MySQL database
# (Run CREATE DATABASE ecommerce_db; in MySQL)

# 4. Generate SQL test data
python generate_sql_data.py

# 5. Generate MongoDB test data
python generate_mongo_data.py

# 6. Query both databases
python hybrid_db.py
```

## Notes

- All scripts use **fake data** generated by the `Faker` library
- `generate_mongo_data.py` prints progress or completion status
- `generate_sql_data.py` inserts data into existing tables
- `hybrid_db.py` provides a template for hybrid database queries
- Modify the number of records by changing loop ranges in scripts


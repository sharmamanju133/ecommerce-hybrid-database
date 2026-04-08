CREATE DATABASE ecommerce_db;
USE ecommerce_db;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Addresses (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    city VARCHAR(100),
    country VARCHAR(100),
    postal_code VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

CREATE TABLE Products (
    product_id VARCHAR(50) PRIMARY KEY,
    category_id INT,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    address_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
);

CREATE TABLE OrderItems (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id VARCHAR(50),
    quantity INT NOT NULL,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

CREATE TABLE Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    amount DECIMAL(10,2),
    payment_method VARCHAR(50),
    payment_status VARCHAR(50),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

CREATE TABLE Cart (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE CartItems (
    cart_item_id INT AUTO_INCREMENT PRIMARY KEY,
    cart_id INT NOT NULL,
    product_id VARCHAR(50),
    quantity INT,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id)
);

CREATE TABLE Shipments (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    shipment_status VARCHAR(50),
    delivery_date DATE,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

-- Add Indexes

CREATE INDEX idx_user_email ON Users(email);

CREATE INDEX idx_orderitems_product ON OrderItems(product_id);

CREATE INDEX idx_products_category ON Products(category_id);

-- Insert Sample Data

INSERT INTO Users (name, email) VALUES
('John Doe', 'john@example.com'),
('Alice Smith', 'alice@example.com'),
('Bob Lee', 'bob@example.com');

INSERT INTO Addresses (user_id, city, country, postal_code) VALUES
(1, 'Berlin', 'Germany', '10115'),
(2, 'Munich', 'Germany', '80331'),
(3, 'Hamburg', 'Germany', '20095');

INSERT INTO Categories (category_name) VALUES
('Electronics'),
('Clothing'),
('Books');

INSERT INTO Products (product_id, category_id, price) VALUES
('P101', 1, 800),
('P102', 2, 50),
('P103', 3, 20);

INSERT INTO Orders (user_id, address_id, order_date, total_amount) VALUES
(1, 1, '2026-04-01', 850),
(2, 2, '2026-04-02', 50);

INSERT INTO OrderItems (order_id, product_id, quantity, price) VALUES
(1, 'P101', 1, 800),
(1, 'P102', 1, 50),
(2, 'P102', 1, 50);

INSERT INTO Payments (order_id, amount, payment_method, payment_status) VALUES
(1, 850, 'Credit Card', 'Completed'),
(2, 50, 'PayPal', 'Completed');

INSERT INTO Cart (user_id) VALUES
(1), (2);

INSERT INTO CartItems (cart_id, product_id, quantity) VALUES
(1, 'P103', 2),
(2, 'P101', 1);

INSERT INTO Shipments (order_id, shipment_status, delivery_date) VALUES
(1, 'Delivered', '2026-04-05'),
(2, 'Shipped', '2026-04-06');

-- Test SQL Queries

-- 1. View All Users
SELECT * FROM Users;

-- 2. User Orders (JOIN)
SELECT u.name, o.order_id, o.total_amount
FROM Users u
JOIN Orders o ON u.user_id = o.user_id;

-- 3. Full Order Details

SELECT u.name, p.product_id, oi.quantity, oi.price
FROM Users u
JOIN Orders o ON u.user_id = o.user_id
JOIN OrderItems oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id;

-- 4. Total Sales

SELECT SUM(total_amount) AS total_sales FROM Orders;


-- 5. Category-wise Sales

SELECT c.category_name, SUM(oi.price * oi.quantity) AS total_sales
FROM OrderItems oi
JOIN Products p ON oi.product_id = p.product_id
JOIN Categories c ON p.category_id = c.category_id
GROUP BY c.category_name;

-- 6. Orders per User

SELECT u.name, COUNT(o.order_id) AS total_orders
FROM Users u
LEFT JOIN Orders o ON u.user_id = o.user_id
GROUP BY u.name;


SELECT COUNT(*) FROM Users;

SELECT COUNT(*) FROM Orders;
SELECT COUNT(*) FROM Products;
SELECT COUNT(*) FROM OrderItems;
SELECT COUNT(*) FROM Payments;
SELECT COUNT(*) FROM Cart;
SELECT COUNT(*) FROM CartItems;
SELECT COUNT(*) FROM Shipments;


-- Top 5 Customers
SELECT u.name, SUM(o.total_amount) AS total_spent
FROM Users u
JOIN Orders o ON u.user_id = o.user_id
GROUP BY u.name
ORDER BY total_spent DESC
LIMIT 5;

-- Most Active Users (Cart + Orders)
SELECT u.name,
COUNT(DISTINCT o.order_id) AS orders,
COUNT(DISTINCT c.cart_id) AS carts
FROM Users u
LEFT JOIN Orders o ON u.user_id = o.user_id
LEFT JOIN Cart c ON u.user_id = c.user_id
GROUP BY u.name
ORDER BY orders DESC;
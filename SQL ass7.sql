CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);


DROP TABLE orders;

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount INT
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price INT
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert Sample Data 

INSERT INTO customers VALUES
(1, 'Diya', 'Ahmedabad'),
(2, 'Jiya', 'Surat'),
(3, 'Dhara', 'Vadodara'),
(4, 'Heli', 'Ahmedabad');

INSERT INTO products VALUES
(101, 'Laptop', 50000),
(102, 'Mobile', 20000),
(103, 'Headphones', 3000);

INSERT INTO orders VALUES
(1001, 1, '2024-01-10', 70000),
(1002, 2, '2024-02-15', 20000),
(1003, 1, '2024-03-05', 3000);

INSERT INTO order_items VALUES
(1001, 101, 1),
(1001, 102, 1),
(1002, 102, 1),
(1003, 103, 1);

-- Total orders per customer

SELECT c.name, COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.name;

-- Customers who never placed an order

SELECT name
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id FROM orders
);

-- Highest selling product

SELECT TOP 1 p.product_name, SUM(oi.quantity) AS total_sold
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;

-- Monthly sales report

 SELECT 
    DATENAME(MONTH, order_date) AS month_name,
    YEAR(order_date) AS year,
    SUM(amount) AS total_sales
FROM orders
GROUP BY YEAR(order_date), DATENAME(MONTH, order_date);

-- Customers with total purchase > ₹50,000

SELECT c.name, SUM(o.amount) AS total_purchase
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.name
HAVING SUM(o.amount) > 50000;

-- Top 3 cities by revenue

SELECT TOP 3 c.city, SUM(o.amount) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC;





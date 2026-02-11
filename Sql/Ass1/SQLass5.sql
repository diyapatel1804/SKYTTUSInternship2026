-- Create users table

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    total_amount INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users VALUES
(1, 'Diya', 'diya@gmail.com', 'diya123'),
(2, 'Jiya', 'jiya@gmail.com', 'jiya123'),
(3, 'Dhara', 'dhara@gmail.com', 'dhara123');

INSERT INTO orders VALUES
(101, 1, '2024-01-10', 5000),
(102, 1, '2024-01-15', 3000),
(103, 2, '2024-01-20', 7000);

-- Add foreign key between orders and users

ALTER TABLE orders
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id) REFERENCES users(user_id);

-- Create index on email column

CREATE INDEX idx_user_email
ON users(email);

-- Create view to display user order summary

CREATE VIEW user_order_summary AS
SELECT 
    u.user_id,
    u.name,
    u.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY u.user_id, u.name, u.email;

-- Check the view 

SELECT * FROM user_order_summary;




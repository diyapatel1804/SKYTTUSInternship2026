
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);

EXEC sp_helpindex orders;

-- Use EXPLAIN to analyze query
SELECT *
FROM orders
WHERE customer_id = 1;

-- Optimize a slow JOIN query

SELECT c.name, o.order_id, o.amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

-- Explain when index should NOT be used
-- Indexes should not be used when:
-- 1. Table is very small
-- 2. Column has very few unique values
-- 3. Data is frequently updated (INSERT/UPDATE/DELETE)
-- 4. Query returns large percentage of rows
-- 5. Index maintenance cost is higher than benefit


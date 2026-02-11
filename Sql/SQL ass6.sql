CREATE TABLE accounts (
    acc_id INT PRIMARY KEY,
    name VARCHAR(50),
    balance INT
);

INSERT INTO accounts VALUES
(1, 'Diya', 10000),
(2, 'Jiya', 8000);

SELECT * FROM accounts;

-- Start a transaction

BEGIN TRANSACTION;

-- Insert record into accounts

INSERT INTO accounts VALUES (3, 'Dhara', 5000);

SELECT * FROM accounts;

-- Rollback changes

ROLLBACK;

SELECT * FROM accounts;

-- Commit valid transaction

BEGIN TRANSACTION;

INSERT INTO accounts VALUES (3, 'Dhara', 5000);

COMMIT;

SELECT * FROM accounts;

-- Demonstrate transfer of money using transaction

BEGIN TRANSACTION;

UPDATE accounts
SET balance = balance - 2000
WHERE name = 'Diya';

UPDATE accounts
SET balance = balance + 2000
WHERE name = 'Jiya';

COMMIT;

SELECT * FROM accounts;






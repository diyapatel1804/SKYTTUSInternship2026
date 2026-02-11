CREATE TABLE students (
    student_id INT,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
);
INSERT INTO students VALUES
(1, 'Diya', 'CSE', 3, 85),
(2, 'Jiya', 'IT', 2, 72),
(3, 'Kavya', 'CSE', 4, 90),
(4, 'Dhara', 'ECE', 1, 65),
(5, 'Heli', 'CSE', 3, 78),
(6, 'Yesha', 'ME', 2, 88);

SELECT * FROM students;
SELECT name, department FROM students;
SELECT * FROM students WHERE marks > 75;
SELECT * FROM students WHERE department = 'CSE';
SELECT * FROM students ORDER BY marks DESC;
SELECT TOP 3 * FROM students ORDER BY marks DESC;




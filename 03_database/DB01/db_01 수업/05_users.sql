CREATE table users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age  INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

.mode csv
.import users.csv users

SELECT * FROM users WHERE age >= 30;
SELECT first_name FROM users WHERE age >= 30;
SELECT first_name, age FROM users WHERE age >= 30 AND last_name = '김';

SELECT MIN(age) FROM users;
-- 이씨 중에 가장 적은 나이를 가진 사람과 통장 잔고 
SELECT MIN(age), first_name  FROM users WHERE last_name = '이';
SELECT AVG(age) FROM users WHERE age >= 30;
SELECT first_name, MAX(balance) FROM users;
SELECT AVG(balance) FROM users WHERE age >= 30;
SELECT * FROM users WHERE last_name LIKE '김%';
SELECT first_name, age FROM users ORDER BY age, last_name LIMIT 10;
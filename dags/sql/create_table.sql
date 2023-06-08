

-- creating table employee
DROP TABLE IF EXISTS employee;
CREATE TABLE employee (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  age INT,
  department VARCHAR(100)
);

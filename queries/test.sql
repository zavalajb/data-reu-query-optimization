SELECT * FROM employees e 
WHERE e.department_id IN (SELECT department_id FROM departments WHERE location_id = 1700)

SELECT * FROM employees e 
WHERE e.department_id IN (SELECT department_id FROM departments WHERE location_id = 1700)
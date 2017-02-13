# GeneralSQL

## Querying Data

### Tables

* a data model in a RDBMS is stored within a **table**
* data may interact across tables
* `\d`: view the available tables

### Querying Data

* the first part in constructing a query: know where your data is coming from
* the next part: examine what data we can query
* `\d users`: view the table that the table name is `users`

construct a query: 

* the **table** we need to query
* the **data** we want from that table

the syntax for a query: 

* the data you want to retrieve
* where the data is coming from
* a semicolon `;` signals the end of your query 
* e.g.: `SELECT first_name, last_name, email FROM users;` (可以分2行写) 

### Filtering Data

can use a combination of filters to filter data

* the filter is first initially specified with the **where** condition
* can combine this with other conditions using either **and** or **or** clause

e.g.: find all users that created accounts in January of 2012

```
SELECT email, created_at
FROM users
WHERE created_at >= '2012-01-01'
  AND created_at < '2012-02-01'
```

## Joins

### What are they?

combine data from 2 different tables; you combine them depned on the type of join 

there are multiple ways to join data

### Joining some data

2 tables are related by keys

e.g.: find which products have been purchased recently

```
SELECT
    products.title,
    purchases.quantity
FROM
    products,
    purchases
WHERE
    products.id = purchases.product_id
LIMIT 5;
```

## Views

### What is a View

* consist of a stored query accessible as a virtual table in a relational database or a set of documents in a document-oriented database composed of the result set of a query or map and reduce functions (wikipedia)
* simply a logical table that automatically connects the pieces of underlying data
* it does not actually duplicate or persist the data as its viewed in a logical form

### Why use a View

* simplify your data model when providing it to others
* simplify working with your data for yourself (e.g.: ease the process of joining 2 sets of data in a similar way many times)

### A View in Action

e.g.: report against employees and their departments many times

```
CREATE OR REPLACE VIEW employee_view AS
SELECT
    employees.last_name,
    employees.salary,
    departments.department
FROM
    employees,
    employee_departments,
    departments
WHERE
    employees.id=employee_departments.employee_id
    AND departments.id=employee_departments.department_id
```

do above **once**, and then simply query the new table directly every time (传统的方式需要每一次都做上述操作)

```
SELECT *
FROM employee_view
```

## Window functions

### What are they

* a window function performs a calculation across a set of table rows that are somehow related to the current row
* this is comparable to the type of calculation that can be done with an aggregate function
* unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row - the row retain their separate identities
* the window function is able to access more than just the current row of the query result

### Window Functions in Action

e.g.: rank every individual over a certain grouping

```
SELECT
    last_name,
    salary,
    department,
    rank() OVER (
        PARTITION BY department
        ORDER BY salary
        DESC
    )
FROM
    employees;
```

find the highest paid person in each department

```
SELECT
    *
FROM
(
    SELECT
        last_name,
        salary,
        department,
        rank() OVER (
            PARTITION BY department
            ORDER BY salary
            DESC
        )
    FROM
        employees
)
sub_query
WHERE
    rank=1;
```

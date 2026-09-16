# Database Layer

The goal of this phase is to learn how databases work and apply them to Python projects before moving into backend development.

Instead of only studying SQL, I will **replace file-based storage in my existing Python projects with databases**.

---

## 🎯 Goals

* Learn SQL fundamentals
* Understand relational databases
* Learn PostgreSQL
* Understand database relationships
* Connect Python applications to databases
* Write SQL from Python
* Replace JSON/CSV storage with PostgreSQL
* Practice database design
* Prepare for FastAPI + PostgreSQL backend projects

---

# Phase 1 — SQL Fundamentals

### Learn

* Databases and tables
* Rows and columns
* Primary keys
* `CREATE`
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`
* `WHERE`
* `ORDER BY`
* `LIMIT`
* `DISTINCT`
* `LIKE`
* `IN`
* `BETWEEN`
* `NULL`

### Practice

Build databases manually using SQL.

Example:

```text
students
transactions
products
users
```

---

# Phase 2 — Database Relationships

### Learn

* Primary keys
* Foreign keys
* One-to-one relationships
* One-to-many relationships
* Many-to-many relationships
* `JOIN`
* `INNER JOIN`
* `LEFT JOIN`

Example:

```text
Student
   │
   └── Grades
```

```text
Category
   │
   └── Transactions
```

---

# Phase 3 — Intermediate SQL

### Learn

* `COUNT()`
* `SUM()`
* `AVG()`
* `MIN()`
* `MAX()`
* `GROUP BY`
* `HAVING`
* `CASE`
* Subqueries
* Constraints
* Indexes
* Transactions

Focus on writing queries that answer real application questions.

Example:

```text
What is the total income this month?
Which category has the highest expenses?
Which products are running low?
What is the average student grade?
```

---

# Phase 4 — PostgreSQL

Move from practicing SQL to using a real relational database system.

### Learn

* PostgreSQL installation
* Databases
* Tables
* Schemas
* Users and roles
* Constraints
* Indexes
* Transactions
* Backup and restore
* PostgreSQL tools

---

# Phase 5 — Python + PostgreSQL

Connect Python applications to PostgreSQL.

### Learn

```text
Python
   ↓
PostgreSQL Driver
   ↓
PostgreSQL
```

Practice:

* Database connections
* Cursors
* Executing SQL
* Parameters
* Fetching results
* `commit()`
* `rollback()`
* Transactions
* Error handling
* Closing connections

### Important

First learn to use **SQL directly from Python**.

ORMs will come later when learning backend development.

---

# Applying Databases to Python Projects

The main objective of this phase is to **upgrade my existing projects**.

---

## Project 1 — Student Management System

### Current

```text
Python
   ↓
JSON
```

### Upgrade

```text
Python
   ↓
PostgreSQL
```

### Database

```text
students
grades
```

### Practice

* Insert students
* Retrieve students
* Search students
* Update students
* Delete students
* Store grades
* Calculate averages
* Use foreign keys
* Use JOINs

---

## Project 2 — Personal Finance Tracker

### Current

```text
Python
   ↓
JSON + CSV
```

### Upgrade

```text
Python
   ↓
PostgreSQL
```

### Database

```text
categories
transactions
```

### Practice

* Add income
* Add expenses
* Store categories
* View transactions
* Calculate balance
* Calculate monthly spending
* Group expenses by category
* Query transactions by date
* Export database data to CSV

---

## Project 3 — Inventory Management System

Build a database-focused project based on a real business problem.

### Database

```text
products
categories
suppliers
purchases
sales
```

### Practice

* Product CRUD
* Categories
* Suppliers
* Stock quantity
* Purchases
* Sales
* Low-stock queries
* Sales reports
* Inventory calculations
* Multiple-table JOINs
* Transactions

This project prepares the database structure for a future supermarket backend.

---

# Database Project Workflow

For every project:

```text
1. Design the problem
        ↓
2. Design tables
        ↓
3. Define relationships
        ↓
4. Create PostgreSQL database
        ↓
5. Write SQL
        ↓
6. Connect Python
        ↓
7. Replace JSON/CSV storage
        ↓
8. Test CRUD operations
        ↓
9. Add more complex queries
        ↓
10. Document the database
```

---

# What I Should Be Able to Do Before Backend

I should be able to:

* Design a relational database
* Create tables
* Choose primary keys
* Use foreign keys
* Write CRUD queries
* Write JOIN queries
* Use aggregation
* Understand database relationships
* Use PostgreSQL
* Connect Python to PostgreSQL
* Handle database errors
* Use transactions
* Move a Python project from JSON/CSV to PostgreSQL
* Build a Python application that persists data in PostgreSQL

---

# Final Milestone

Build a Python project where:

```text
User
 ↓
Python Application
 ↓
PostgreSQL
 ↓
Persistent Data
```

No tutorial should be required for the basic CRUD and database operations.

After completing this phase:

```text
Python
   +
SQL
   +
PostgreSQL
   ↓
Backend Development
   ↓
FastAPI
```

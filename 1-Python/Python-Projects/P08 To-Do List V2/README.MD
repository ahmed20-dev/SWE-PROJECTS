# To-Do List V2

A command-line To-Do List application built to improve my **OOP design, input validation, and Python project structure**.

This is a V2 of my earlier To-Do List project. The goal is not to add many features, but to build the same type of application with a cleaner and more maintainable architecture.

## Goals

* Improve Object-Oriented Programming design
* Separate responsibilities between classes and modules
* Improve input validation and error handling
* Practice working with JSON persistence
* Build a cleaner Python project structure

## Features

* Add tasks
* View tasks
* Update tasks
* Delete tasks
* Mark tasks as completed
* Search tasks
* Filter tasks by status
* Filter tasks by priority
* Set task priority
* Set due dates
* Save tasks to JSON
* Load tasks from JSON

## Project Structure

```text
P08_Todo_List_V2/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── manager.py
│   ├── storage.py
│   └── validators.py
│
├── data/
│   └── tasks.json
│
├── tests/
│   └── test_tasks.py
│
├── README.md
└── .gitignore
```

## OOP Design

The application separates responsibilities into different components:

### `Task`

Represents a single task and its data.

### `TaskManager`

Handles task operations such as:

* Creating tasks
* Updating tasks
* Deleting tasks
* Completing tasks
* Searching and filtering

### `Storage`

Handles persistence:

* Loading tasks from JSON
* Saving tasks to JSON

### `Validators`

Handles user input and data validation.

## Task Data

Each task contains:

```text
ID
Title
Description
Priority
Due Date
Status
```

Example:

```text
ID: 1
Title: Learn PostgreSQL
Description: Practice basic CRUD operations
Priority: High
Due Date: 25-09-2026
Status: Pending
```

## Validation

The application validates:

* Empty task titles
* Invalid task IDs
* Non-existent task IDs
* Invalid menu choices
* Invalid priorities
* Invalid dates
* Invalid or corrupted stored data

The goal is to keep validation consistent rather than repeating the same checks throughout the application.

## Data Persistence

Tasks are stored in JSON.

The application should be able to:

```text
Task objects
    ↓
Dictionary data
    ↓
JSON file
```

and load them back:

```text
JSON file
    ↓
Dictionary data
    ↓
Task objects
```

## What I'm Practicing

### Python

* Classes and objects
* Instance attributes and methods
* `__init__`
* `__str__`
* Modules and imports
* JSON
* Exception handling
* Input validation
* Basic testing

### Software Engineering

* Separation of concerns
* Single responsibility
* Project structure
* Reusable components
* Maintainable code
* Basic testing

## Future Improvements

After completing V2, I plan to continue improving my Python projects and eventually replace JSON-based storage with **PostgreSQL**.

---

**Project focus:** OOP Design → Validation → Project Structure → Persistence

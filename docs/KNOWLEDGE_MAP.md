# Engineering Knowledge Map

> The technical knowledge I am building toward becoming a Full-Stack + AI Engineer.

This document is a **knowledge map**, not a checklist to finish all at once.

The goal is to understand the foundations, build projects with them, and gradually connect the different areas into complete software systems.

---

# 🗺️ The Big Picture

```text
                         Software Engineering
                                  │
          ┌───────────────────────┼───────────────────────┐
          ↓                       ↓                       ↓
       Python                 Databases                 Linux
          │                       │                       │
          └───────────────────────┼───────────────────────┘
                                  ↓
                              Backend
                                  ↓
                              Frontend
                                  ↓
                         Full-Stack Systems
                                  ↓
                         Deployment & Cloud
                                  ↓
                           System Design
                                  ↓
                            Data & ML
                                  ↓
                         AI Engineering
                                  ↓
                       AI-Powered Products
```

---

# 1. Python

## 1.1 Fundamentals

* [ ] Variables and data types
* [ ] Operators
* [ ] Conditions
* [ ] Loops
* [ ] Input and output
* [ ] Strings
* [ ] Lists
* [ ] Tuples
* [ ] Sets
* [ ] Dictionaries

## 1.2 Functions

* [ ] Defining functions
* [ ] Parameters and arguments
* [ ] Default arguments
* [ ] `*args`
* [ ] `**kwargs`
* [ ] Return values
* [ ] Scope
* [ ] Lambda functions
* [ ] Comprehensions

## 1.3 Data Structures

* [ ] Lists
* [ ] Stacks
* [ ] Queues
* [ ] Sets
* [ ] Dictionaries
* [ ] Searching
* [ ] Sorting
* [ ] Big-O fundamentals

## 1.4 Error Handling

* [ ] Exceptions
* [ ] `try / except`
* [ ] `else`
* [ ] `finally`
* [ ] Raising exceptions
* [ ] Custom exceptions
* [ ] Input validation

## 1.5 File Handling

* [ ] Reading files
* [ ] Writing files
* [ ] CSV
* [ ] JSON
* [ ] File paths
* [ ] `pathlib`

## 1.6 Object-Oriented Programming

* [ ] Classes
* [ ] Objects / instances
* [ ] Instance attributes
* [ ] Instance methods
* [ ] Class methods
* [ ] Static methods
* [ ] Constructors
* [ ] Encapsulation
* [ ] Inheritance
* [ ] Polymorphism
* [ ] Composition
* [ ] Abstraction

## 1.7 Python Project Structure

* [ ] Modules
* [ ] Packages
* [ ] Imports
* [ ] Virtual environments
* [ ] Environment variables
* [ ] Configuration
* [ ] Separation of concerns
* [ ] Dependency management

## 1.8 Professional Python

* [ ] Type hints
* [ ] Dataclasses
* [ ] Logging
* [ ] Testing with `pytest`
* [ ] Formatting
* [ ] Linting
* [ ] Debugging
* [ ] Documentation

---

# 2. Git & GitHub

## 2.1 Git Fundamentals

* [ ] Repository
* [ ] Working tree
* [ ] Staging area
* [ ] Commits
* [ ] Branches
* [ ] Merging
* [ ] Rebasing
* [ ] Remote repositories
* [ ] Pulling
* [ ] Pushing

## 2.2 Collaboration

* [ ] Pull requests
* [ ] Code review
* [ ] Merge conflicts
* [ ] Issues
* [ ] `.gitignore`
* [ ] Repository organization

## 2.3 Professional Workflow

* [ ] Meaningful commits
* [ ] Feature branches
* [ ] Pull request workflow
* [ ] Release/versioning basics
* [ ] GitHub Actions fundamentals

---

# 3. Databases

## 3.1 SQL Fundamentals

* [ ] Tables
* [ ] Rows and columns
* [ ] Primary keys
* [ ] Foreign keys
* [ ] `SELECT`
* [ ] `INSERT`
* [ ] `UPDATE`
* [ ] `DELETE`
* [ ] Filtering
* [ ] Sorting
* [ ] Aggregation
* [ ] `GROUP BY`
* [ ] `HAVING`

## 3.2 Relationships

* [ ] One-to-one
* [ ] One-to-many
* [ ] Many-to-many
* [ ] Joins
* [ ] `INNER JOIN`
* [ ] `LEFT JOIN`
* [ ] Self joins

## 3.3 PostgreSQL

* [ ] PostgreSQL installation
* [ ] Databases
* [ ] Schemas
* [ ] Roles and permissions
* [ ] Constraints
* [ ] Indexes
* [ ] Transactions
* [ ] Views
* [ ] PostgreSQL data types

## 3.4 Database Design

* [ ] Requirements → entities
* [ ] Entity relationships
* [ ] ER diagrams
* [ ] Normalization
* [ ] Constraints
* [ ] Index design
* [ ] Migrations
* [ ] Seed data

## 3.5 Python ↔ PostgreSQL

* [ ] Database drivers
* [ ] Connections
* [ ] Cursors
* [ ] Queries from Python
* [ ] Parameterized queries
* [ ] Transactions
* [ ] Connection pooling
* [ ] SQLAlchemy

---

# 4. Backend Engineering

## 4.1 Web Fundamentals

* [ ] Client / server model
* [ ] HTTP
* [ ] HTTPS
* [ ] HTTP methods
* [ ] Status codes
* [ ] Headers
* [ ] Cookies
* [ ] Sessions
* [ ] JSON
* [ ] REST

## 4.2 FastAPI

* [ ] Routes
* [ ] Path parameters
* [ ] Query parameters
* [ ] Request bodies
* [ ] Response models
* [ ] Pydantic
* [ ] Dependency injection
* [ ] Error handling
* [ ] Middleware
* [ ] API documentation

## 4.3 API Design

* [ ] REST conventions
* [ ] Resource design
* [ ] Pagination
* [ ] Filtering
* [ ] Sorting
* [ ] Validation
* [ ] Error responses
* [ ] API versioning

## 4.4 Authentication & Authorization

* [ ] Password hashing
* [ ] Authentication
* [ ] Authorization
* [ ] JWT
* [ ] Sessions
* [ ] Roles and permissions
* [ ] OAuth fundamentals

## 4.5 Backend Architecture

* [ ] Separation of concerns
* [ ] Routers
* [ ] Services
* [ ] Repositories
* [ ] Models
* [ ] Schemas
* [ ] Configuration
* [ ] Dependency management
* [ ] Background tasks

## 4.6 Backend Testing

* [ ] Unit tests
* [ ] Integration tests
* [ ] API tests
* [ ] Database testing
* [ ] Test fixtures
* [ ] Mocking
* [ ] Test coverage

---

# 5. Frontend Engineering

## 5.1 HTML

* [ ] Semantic HTML
* [ ] Forms
* [ ] Accessibility basics
* [ ] Page structure

## 5.2 CSS

* [ ] Selectors
* [ ] Box model
* [ ] Flexbox
* [ ] Grid
* [ ] Responsive design
* [ ] Mobile-first design
* [ ] CSS architecture

## 5.3 JavaScript

* [ ] Variables
* [ ] Functions
* [ ] Arrays
* [ ] Objects
* [ ] DOM
* [ ] Events
* [ ] Modules
* [ ] Promises
* [ ] Async/await
* [ ] Fetch API
* [ ] Error handling

## 5.4 React

* [ ] Components
* [ ] Props
* [ ] State
* [ ] Events
* [ ] Forms
* [ ] Hooks
* [ ] Routing
* [ ] API integration
* [ ] Authentication
* [ ] State management

## 5.5 Frontend Engineering

* [ ] Component architecture
* [ ] Loading states
* [ ] Error states
* [ ] Form validation
* [ ] Accessibility
* [ ] Performance
* [ ] Responsive interfaces

---

# 6. Full-Stack Engineering

The goal is to connect the previous areas into complete systems.

```text
React
  ↓
HTTP / REST API
  ↓
FastAPI
  ↓
Business Logic
  ↓
PostgreSQL
```

## Knowledge

* [ ] Frontend ↔ backend communication
* [ ] API contracts
* [ ] Authentication flow
* [ ] Authorization
* [ ] Database integration
* [ ] Error handling across the stack
* [ ] File uploads
* [ ] Background jobs
* [ ] Caching
* [ ] Application configuration
* [ ] End-to-end testing

## Product Engineering

* [ ] Requirements
* [ ] User flows
* [ ] MVP definition
* [ ] Database design
* [ ] API design
* [ ] UI design
* [ ] Implementation
* [ ] Testing
* [ ] Deployment
* [ ] User feedback
* [ ] Iteration

---

# 7. Linux

## Fundamentals

* [ ] Filesystem
* [ ] Permissions
* [ ] Processes
* [ ] Environment variables
* [ ] Shell commands
* [ ] Bash basics
* [ ] SSH
* [ ] Package management

## Development

* [ ] Running services
* [ ] Logs
* [ ] Processes
* [ ] Environment configuration
* [ ] Server management

---

# 8. Docker & Deployment

## Docker

* [ ] Images
* [ ] Containers
* [ ] Dockerfiles
* [ ] Volumes
* [ ] Networks
* [ ] Docker Compose
* [ ] Environment variables

## Deployment

* [ ] Application servers
* [ ] Reverse proxies
* [ ] HTTPS
* [ ] Domain names
* [ ] Cloud fundamentals
* [ ] Database deployment
* [ ] Environment separation

## CI/CD

* [ ] Automated testing
* [ ] Build pipelines
* [ ] Deployment pipelines
* [ ] GitHub Actions

---

# 9. Security

## Fundamentals

* [ ] Authentication
* [ ] Authorization
* [ ] Password security
* [ ] Secrets management
* [ ] HTTPS
* [ ] Input validation
* [ ] SQL injection
* [ ] XSS
* [ ] CSRF
* [ ] CORS

## Application Security

* [ ] Secure API design
* [ ] Rate limiting
* [ ] Access control
* [ ] Secure file uploads
* [ ] Dependency security
* [ ] Logging security events

---

# 10. System Design

## Fundamentals

* [ ] Scalability
* [ ] Availability
* [ ] Reliability
* [ ] Maintainability
* [ ] Performance
* [ ] Latency
* [ ] Throughput

## Architecture

* [ ] Monoliths
* [ ] Modular monoliths
* [ ] Microservices
* [ ] Service boundaries
* [ ] APIs
* [ ] Message queues
* [ ] Background workers

## Infrastructure

* [ ] Load balancing
* [ ] Caching
* [ ] CDNs
* [ ] Database scaling
* [ ] Replication
* [ ] Partitioning
* [ ] Object storage

## Reliability

* [ ] Logging
* [ ] Monitoring
* [ ] Metrics
* [ ] Health checks
* [ ] Backups
* [ ] Disaster recovery

---

# 11. Data Science

## Mathematics

Build the mathematical foundation as needed.

* [ ] Arithmetic
* [ ] Algebra
* [ ] Functions
* [ ] Basic probability
* [ ] Statistics
* [ ] Mean / median / mode
* [ ] Variance
* [ ] Standard deviation
* [ ] Correlation
* [ ] Basic linear algebra
* [ ] Basic calculus concepts

## Python Data Stack

* [ ] NumPy
* [ ] Pandas
* [ ] Matplotlib
* [ ] Data cleaning
* [ ] Data transformation
* [ ] Exploratory data analysis
* [ ] Data visualization

## Data Workflow

```text
Raw Data
   ↓
Cleaning
   ↓
Exploration
   ↓
Visualization
   ↓
Feature Engineering
   ↓
Modeling
   ↓
Evaluation
   ↓
Decision / Product
```

---

# 12. Machine Learning

## Fundamentals

* [ ] Supervised learning
* [ ] Unsupervised learning
* [ ] Regression
* [ ] Classification
* [ ] Clustering
* [ ] Features
* [ ] Labels
* [ ] Training
* [ ] Validation
* [ ] Testing

## Models

* [ ] Linear regression
* [ ] Logistic regression
* [ ] Decision trees
* [ ] Random forests
* [ ] Gradient boosting
* [ ] K-nearest neighbors
* [ ] Clustering

## Evaluation

* [ ] Train/test split
* [ ] Cross-validation
* [ ] Accuracy
* [ ] Precision
* [ ] Recall
* [ ] F1 score
* [ ] MAE
* [ ] MSE
* [ ] RMSE
* [ ] Confusion matrix

## Practical ML

* [ ] Feature engineering
* [ ] Data leakage
* [ ] Overfitting
* [ ] Underfitting
* [ ] Hyperparameter tuning
* [ ] Model pipelines
* [ ] Model persistence
* [ ] Model serving

---

# 13. AI Engineering

The focus here is not only training models.

The goal is to **build reliable software systems that use AI**.

## LLM Fundamentals

* [ ] Tokens
* [ ] Context windows
* [ ] Model APIs
* [ ] System prompts
* [ ] User prompts
* [ ] Structured outputs
* [ ] Function/tool calling
* [ ] Streaming

## Prompt Engineering

* [ ] Clear instructions
* [ ] Context management
* [ ] Few-shot examples
* [ ] Structured prompts
* [ ] Output validation
* [ ] Prompt evaluation

## Embeddings & Retrieval

* [ ] Embeddings
* [ ] Vector similarity
* [ ] Vector databases
* [ ] Chunking
* [ ] Metadata
* [ ] Retrieval

## RAG

```text
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
Retrieval
   ↓
LLM
   ↓
Answer
```

Learn:

* [ ] RAG architecture
* [ ] Retrieval strategies
* [ ] Context construction
* [ ] Evaluation
* [ ] Hallucination reduction

## AI Agents & Workflows

* [ ] Tool calling
* [ ] Agent loops
* [ ] Planning
* [ ] Memory
* [ ] Multi-step workflows
* [ ] Human-in-the-loop systems
* [ ] Agent evaluation

## AI + Software Engineering

* [ ] AI API integration
* [ ] Structured outputs
* [ ] AI service architecture
* [ ] Async AI requests
* [ ] Retries
* [ ] Rate limits
* [ ] Cost control
* [ ] Caching
* [ ] Evaluation
* [ ] Observability

---

# 14. AI Product Engineering

This is where software engineering, data, and AI come together.

```text
                Real User Problem
                       ↓
                 Product Design
                       ↓
              Full-Stack Application
                       ↓
              Data + Business Logic
                       ↓
                  AI Capability
                       ↓
                  Production
                       ↓
                  Real Users
                       ↓
                    Feedback
                       ↓
                   Iteration
```

## Capabilities

* [ ] Identify a real problem
* [ ] Interview users
* [ ] Define requirements
* [ ] Design an MVP
* [ ] Build the application
* [ ] Integrate AI
* [ ] Evaluate AI outputs
* [ ] Deploy
* [ ] Monitor
* [ ] Collect feedback
* [ ] Iterate

---

# 15. Professional Engineering

## Code Quality

* [ ] Readable code
* [ ] Small functions
* [ ] Clear naming
* [ ] Separation of concerns
* [ ] Reusable components
* [ ] Type safety
* [ ] Documentation

## Testing

* [ ] Unit testing
* [ ] Integration testing
* [ ] End-to-end testing
* [ ] Regression testing
* [ ] Test automation

## Engineering Practices

* [ ] Code review
* [ ] Issue tracking
* [ ] Documentation
* [ ] Version control
* [ ] Debugging
* [ ] Refactoring
* [ ] Technical debt management

---

# 16. Product & Business Skills

Software is useful only when it solves a meaningful problem.

## Problem Discovery

* [ ] Identify user problems
* [ ] Interview users
* [ ] Understand workflows
* [ ] Validate assumptions
* [ ] Define requirements

## Product Development

* [ ] MVP
* [ ] User stories
* [ ] Prioritization
* [ ] Feedback loops
* [ ] Product iteration
* [ ] Usage metrics

## Freelance / Professional Work

* [ ] Client communication
* [ ] Requirements gathering
* [ ] Scope definition
* [ ] Estimation
* [ ] Proposal writing
* [ ] Project delivery
* [ ] Maintenance

---

# 🔄 How I Learn

I don't expect to complete this map linearly.

For each important topic:

```text
Learn
  ↓
Practice
  ↓
Build
  ↓
Break
  ↓
Debug
  ↓
Understand
  ↓
Document
  ↓
Use in a larger project
```

I prioritize **building over collecting tutorials**.

---

# 🧱 Project Progression

My projects should gradually increase in complexity.

```text
Small Exercises
      ↓
Learning Projects
      ↓
Practical Tools
      ↓
Real-World Projects
      ↓
APIs & Backend Systems
      ↓
Full-Stack Applications
      ↓
Production Systems
      ↓
AI-Powered Products
```

The goal is not to make every project perfect.

The goal is for each project to introduce a new engineering capability.

---

# 🎯 End Goal

The end goal is not to know every framework, library, or AI model.

The goal is to become capable of taking a real problem through the complete engineering lifecycle:

```text
Problem
   ↓
Research
   ↓
Requirements
   ↓
Design
   ↓
Implementation
   ↓
Testing
   ↓
Deployment
   ↓
Real Users
   ↓
Feedback
   ↓
Improvement
```

Ultimately:

> **Build useful software, understand how it works, and continuously improve it based on real-world use.**

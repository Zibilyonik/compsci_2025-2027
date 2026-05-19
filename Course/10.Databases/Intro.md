# Topic A3 - Databases

## Introduction

Welcome to the Databases module! In this section, we'll explore how to organize, store, and retrieve data efficiently using databases. Databases are fundamental to modern software systems—from social media platforms to banking systems, they're everywhere. Understanding how to design and query databases is one of the most valuable skills in computer science.

## What is a Database?

A database is an organized collection of structured data stored on a computer. Think of it like a digital filing system that allows you to store, retrieve, and manage large amounts of information quickly and reliably. Instead of storing data in multiple separate files, databases allow you to organize data in a way that makes it easy to find what you need.

For example, instead of keeping student records in different spreadsheets, a school database might store all student information in one organized system where you can quickly look up a student by name, ID, or grade level.

## Why Databases Matter

**Efficiency**: You can retrieve specific information instantly rather than manually searching through files.

**Consistency**: Databases help ensure data is accurate and up-to-date across your entire system.

**Security**: Databases provide tools to protect sensitive information and control who can access it.

**Scalability**: Databases can handle millions of records without slowing down.

**Concurrency**: Multiple users can access and modify data simultaneously without conflicts.

## Relational Databases

In this course, we'll focus on **relational databases**, which organize data into tables (similar to spreadsheets). Each table contains rows (records) and columns (fields/attributes).

### Key Concepts

**Table**: A collection of related data organized in rows and columns.

- Example: A `Students` table with columns for StudentID, Name, Grade, and Email.

**Row**: A single record in a table.

- Example: One row might contain data for student "Alice Johnson" with StudentID 101.

**Column (Field)**: An attribute of the data.

- Example: The "Grade" column stores the grade level for each student.

**Primary Key**: A unique identifier for each row in a table.

- Example: StudentID uniquely identifies each student so there are no duplicates.

**Foreign Key**: A reference to a primary key in another table, creating relationships between tables.

- Example: A `Grades` table might use StudentID as a foreign key to connect student records with their grades.

## SQL (Structured Query Language)

SQL is the standard language used to communicate with databases. You use SQL to:

- **CREATE**: Build new tables and databases
- **INSERT**: Add new data to tables
- **SELECT**: Retrieve data from tables (the most common operation)
- **UPDATE**: Modify existing data
- **DELETE**: Remove data from tables

### Basic SQL Operations

**CREATE TABLE**: Define a new table with columns and data types.

```sql
CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY,
    Name TEXT,
    Grade INTEGER,
    Email TEXT
);
```

**INSERT**: Add a new student record.

```sql
INSERT INTO Students (StudentID, Name, Grade, Email)
VALUES (101, 'Alice Johnson', 11, 'alice@school.edu');
```

**SELECT**: Retrieve all students.

```sql
SELECT * FROM Students;
```

**SELECT with WHERE**: Find a specific student.

```sql
SELECT * FROM Students WHERE Name = 'Alice Johnson';
```

**UPDATE**: Change a student's grade.

```sql
UPDATE Students SET Grade = 12 WHERE StudentID = 101;
```

**DELETE**: Remove a student record.

```sql
DELETE FROM Students WHERE StudentID = 101;
```

## Database Relationships

Relational databases use relationships to connect data across multiple tables. This prevents data duplication and keeps information organized.

### One-to-Many Relationship

One record in a table can relate to many records in another table.

- Example: One teacher can teach many students.
- Implementation: The `Students` table has a `TeacherID` foreign key pointing to the `Teachers` table.

### Many-to-Many Relationship

Many records in one table can relate to many records in another table.

- Example: Many students can enroll in many courses.
- Implementation: A join table (`StudentCourses`) stores the relationships between students and courses.

## Data Types in SQL

When creating tables, you specify data types for each column:

- **INTEGER**: Whole numbers (1, 42, -5)
- **REAL**: Decimal numbers (3.14, 2.5)
- **TEXT**: Text strings ("Alice", "Hello World")
- **BLOB**: Binary data (images, files)
- **DATE**: Calendar dates (format: 2024-05-19 or use DATE functions)

## Constraints

Constraints enforce rules on data to maintain integrity:

- **PRIMARY KEY**: Ensures each row is unique
- **NOT NULL**: Requires a value (can't be empty)
- **UNIQUE**: Ensures no duplicate values in a column
- **FOREIGN KEY**: Maintains relationships between tables
- **DEFAULT**: Sets a default value if none is provided

## Introduction to SQLite

In this course, we'll use **SQLite**, a lightweight, file-based database system that's perfect for learning. Unlike larger systems like MySQL or PostgreSQL, SQLite doesn't require a separate server—the entire database is stored in a single `.sqlite` file.

### Key Advantages of SQLite

- **Simple**: No setup or installation required (in most cases)
- **Portable**: The database is a single file that you can share easily
- **Powerful**: Supports full SQL including joins, transactions, and constraints
- **Widely Used**: Found in countless applications, from smartphones to web browsers

## What You'll Learn

In this module, you will:

1. Design database schemas (table structures)
2. Create tables and define relationships
3. Write SQL queries to retrieve, insert, update, and delete data
4. Use filters and conditions to find specific information
5. Join tables to combine data from multiple sources
6. Understand database best practices and optimization

## Resources

For more information, check out:

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [Khan Academy Databases](https://www.khanacademy.org/computing/computer-programming)

Let's dive in and start querying!

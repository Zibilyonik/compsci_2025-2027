# SQL Exercise Module - Getting Started

## Module Overview

This module is designed for **IB DP1 Computer Science - Topic A3: Databases**. Students will learn SQL fundamentals using SQLite with a realistic school database containing 100 student records.

## Files Included

### 1. **Intro.md** - Database Concepts

Comprehensive introduction covering:

- What databases are and why they matter
- Relational database fundamentals
- Key concepts: tables, rows, columns, keys
- SQL operations: CREATE, INSERT, SELECT, UPDATE, DELETE
- Database relationships and constraints
- SQLite basics and advantages

### 2. **sql_exercises.py** - Interactive Exercise File

Step-by-step SQL exercises with 10 parts:

- **Part 1**: Connecting and exploring data
- **Part 2**: Basic SELECT queries and retrieving data
- **Part 3**: Filtering with WHERE clauses
- **Part 4**: Ordering and sorting data
- **Part 5**: Aggregate functions (COUNT, AVG, MIN, MAX)
- **Part 6**: Finding distinct/unique values
- **Part 7**: String operations and filtering
- **Part 8**: Multiple conditions (AND, OR logic)
- **Part 9**: Limiting and offsetting results
- **Part 10**: Challenge queries combining concepts

Each exercise includes:

- Clear instructions with comments
- Hints for students
- Sample output indicators
- Progressive difficulty from basic to advanced

### 3. **school_data.sqlite** - Practice Database

A SQLite database containing:

- **100 student records** across grades 9-12
- **Columns**: StudentID (primary key), FirstName, LastName, Grade, Email, Phone, EnrollmentDate, AverageGrade
- Realistic data for practice queries
- No relationships for basic exercises (perfect for beginners)

## Getting Started

### Prerequisites

- Python 3.x with SQLite support (built-in)
- A terminal or command line
- Text editor or IDE for viewing/editing .py files

### Running the Exercises

1. **Navigate to the module folder**:

   ```bash
   cd "10.Databases"
   ```

2. **Open the exercise file** in your editor:

   ```bash
   python sql_exercises.py
   ```

3. **Complete each TODO section** by writing SQL queries in the appropriate places

4. **Test your queries** by running the script frequently

### Example Workflow

```python
# Before:
# TODO: Find all students in Grade 11
print("\nStudents in Grade 11:")
# TODO: write query here

# After:
print("\nStudents in Grade 11:")
cursor.execute("SELECT * FROM Students WHERE Grade = 11")
for row in cursor.fetchall():
    print(row)
```

## Exercise Progression

**Beginner**: Parts 1-3 (Basic queries and filtering)

- Connect to database
- Retrieve all data
- Use WHERE clauses

**Intermediate**: Parts 4-7 (Advanced queries)

- Sort and order data
- Use aggregate functions
- Handle text searches

**Advanced**: Parts 8-10 (Complex queries)

- Combine multiple conditions
- Use limiting and offsets
- Write complex analytical queries

## Learning Outcomes

By completing this module, students will:

- ✓ Understand relational database design
- ✓ Write and execute basic to advanced SQL queries
- ✓ Filter, sort, and aggregate data
- ✓ Solve real-world data retrieval problems
- ✓ Build confidence working with databases

## Tips for Success

1. **Start Simple**: Begin with Part 1 and work sequentially
2. **Read the Data**: Use simple SELECT queries to understand data structure
3. **Test Incrementally**: Run your code after each change
4. **Use Comments**: Document what each query does
5. **Ask Questions**: If a query doesn't work, review the error message
6. **Practice Variations**: Try similar queries on different columns

## Common SQL Mistakes to Avoid

- Forgetting semicolons at end of SQL statements
- Using `=` instead of `==` in conditions (SQL uses single `=`)
- Forgetting quotes around text in WHERE clauses
- Case sensitivity in column names (SQLite is case-insensitive for names but case-sensitive for data)
- Forgetting `FROM` clause in SELECT statements

## Resources

- [SQLite Official Documentation](https://www.sqlite.org/docs.html)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [Mozilla SQL Basics](https://developer.mozilla.org/en-US/docs/Learn/Server-side/MySQL)

---

**Happy Querying!** Remember, the best way to learn databases is by writing lots of queries and experimenting. Don't be afraid to try things out!

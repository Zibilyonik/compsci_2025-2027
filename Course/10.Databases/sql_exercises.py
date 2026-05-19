# IB DP CompSci - Topic A3 - Database SQL Exercises

import sqlite3

# Database setup: Connect to the practice database
# If the database doesn't exist, it will be created
db_connection = sqlite3.connect("school_data.sqlite")
cursor = db_connection.cursor()

# ---------------------------------------------------------------------------
# PART 1 – CONNECTING AND EXPLORING
# ---------------------------------------------------------------------------

# TODO: Use cursor.execute() to display all data from the Students table
# HINT: Use SELECT * FROM Students;
print("=== PART 1: All Students ===")

# TODO: write query here


# ---------------------------------------------------------------------------
# PART 2 – BASIC SELECT QUERIES (RETRIEVING DATA)
# ---------------------------------------------------------------------------

print("\n=== PART 2: Basic SELECT Queries ===")

# TODO: Select only the FirstName, LastName and Email columns from the Students table
# Display the first 5 results
print("\nNames and Emails (first 5):")

# TODO: write query here


# TODO: Count how many students are in the table
print("\nTotal number of students:")

# TODO: write query here


# ---------------------------------------------------------------------------
# PART 3 – FILTERING WITH WHERE CLAUSES
# ---------------------------------------------------------------------------

print("\n=== PART 3: Filtering Data ===")

# TODO: Find all students in Grade 11
print("\nStudents in Grade 11:")

# TODO: write query here


# TODO: Find the student with ID 50
print("\nStudent with ID 50:")

# TODO: write query here


# ---------------------------------------------------------------------------
# PART 4 – ORDERING AND SORTING
# ---------------------------------------------------------------------------

print("\n=== PART 4: Sorting Data ===")

# TODO: Get all students ordered by their Grade (lowest to highest)
print("\nStudents ordered by grade (ascending):")

# TODO: write query here


# TODO: Get the top 10 students by grade (highest to lowest)
print("\nTop 10 highest grades:")

# TODO: write query here


# ---------------------------------------------------------------------------
# PART 5 – AGGREGATE FUNCTIONS
# ---------------------------------------------------------------------------

print("\n=== PART 5: Aggregate Functions ===")

# TODO: Calculate the average grade of all students
print("\nAverage grade across all students:")

# TODO: write query here


# TODO: Find the minimum (lowest) and maximum (highest) grades
print("\nLowest and highest grades:")

# TODO: write query here


# TODO: Find the average grade for Grade 11 students only
print("\nAverage grade for Grade 11 students:")

# TODO: write query here


# ---------------------------------------------------------------------------
# PART 6 – DISTINCT VALUES
# ---------------------------------------------------------------------------

print("\n=== PART 6: Finding Unique Values ===")

# TODO: List all unique grades in the database (no duplicates)
print("\nAll unique grade levels:")

# TODO: write query here


# TODO: Count how many different grades we have
print("\nNumber of different grades:")

# TODO: write query here


# ---------------------------------------------------------------------------
# PART 7 – STRING OPERATIONS
# ---------------------------------------------------------------------------

print("\n=== PART 7: String Filtering ===")

# TODO: Find all students whose first name starts with 'A'
print("\nStudents whose name starts with 'A':")

# TODO: write query here


# TODO: Find all students whose email contains 'example.com'
print("\nStudents with example.com email:")

# TODO: write query here


# ---------------------------------------------------------------------------
# PART 8 – COMBINING CONDITIONS
# ---------------------------------------------------------------------------

print("\n=== PART 8: Multiple Conditions (AND, OR) ===")

# TODO: Find students in Grade 12 with a grade average >= 85
print("\nGrade 12 students with average >= 85:")

# TODO: write query here


# TODO: Find students who either have grade 10 OR have a last name starting with 'S'
print("\nGrade 10 students OR last name starts with 'S':")

# TODO: write query here


# ---------------------------------------------------------------------------
# PART 9 – LIMITING RESULTS
# ---------------------------------------------------------------------------

print("\n=== PART 9: Limiting Results ===")

# TODO: Get the first 15 students from the database
print("\nFirst 15 students:")

# TODO: write query here


# TODO: Skip the first 20 students and get the next 10
# (HINT: Use LIMIT and OFFSET)
print("\nStudents 21-30:")

# TODO: write query here


# ---------------------------------------------------------------------------
# PART 10 – CHALLENGE QUERIES
# ---------------------------------------------------------------------------

print("\n=== PART 10: Challenge ===")

# TODO: Find the top 5 students by average grade
# Display their ID, Name, and Grade in descending order
print("\nTop 5 students by grade:")

# TODO: write query here


# TODO: Count how many students are in each grade
# Display the grade and the count
print("\nNumber of students per grade:")

# TODO: write query here


# TODO: Find students whose name contains 'Smith' or email ends with '.edu'
# ORDER them by Grade descending
print("\nStudents with 'Smith' in name or .edu email (ordered by grade):")

# TODO: write query here


# ---------------------------------------------------------------------------
# CLEANUP
# ---------------------------------------------------------------------------

# Close the database connection
db_connection.close()
print("\n✓ Database connection closed.")

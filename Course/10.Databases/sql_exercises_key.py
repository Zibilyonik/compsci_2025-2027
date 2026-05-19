# IB DP CompSci - Topic A3 - Database SQL Exercises - SOLUTION KEY

import sqlite3

# Database setup
db_connection = sqlite3.connect("school_data.sqlite")
cursor = db_connection.cursor()

# ---------------------------------------------------------------------------
# PART 1 – CONNECTING AND EXPLORING
# ---------------------------------------------------------------------------

print("=== PART 1: All Students ===")
cursor.execute("SELECT * FROM Students")
results = cursor.fetchall()
print(f"Total records retrieved: {len(results)}")
for row in results[:3]:  # Show first 3 for verification
    print(row)
print()


# ---------------------------------------------------------------------------
# PART 2 – BASIC SELECT QUERIES (RETRIEVING DATA)
# ---------------------------------------------------------------------------

print("=== PART 2: Basic SELECT Queries ===")

print("\nNames and Emails (first 5):")
cursor.execute("SELECT FirstName, LastName, Email FROM Students LIMIT 5")
for row in cursor.fetchall():
    print(row)

print("\nTotal number of students:")
cursor.execute("SELECT COUNT(*) FROM Students")
count = cursor.fetchone()[0]
print(f"Count: {count}")
print()


# ---------------------------------------------------------------------------
# PART 3 – FILTERING WITH WHERE CLAUSES
# ---------------------------------------------------------------------------

print("=== PART 3: Filtering Data ===")

print("\nStudents in Grade 11:")
cursor.execute("SELECT StudentID, FirstName, LastName, Grade FROM Students WHERE Grade = 11")
for row in cursor.fetchall()[:3]:  # Show first 3
    print(row)
print(f"(showing first 3 of {cursor.rowcount} total)")

print("\nStudent with ID 50:")
cursor.execute("SELECT * FROM Students WHERE StudentID = 50")
row = cursor.fetchone()
print(row)
print()


# ---------------------------------------------------------------------------
# PART 4 – ORDERING AND SORTING
# ---------------------------------------------------------------------------

print("=== PART 4: Sorting Data ===")

print("\nStudents ordered by grade (ascending):")
cursor.execute("SELECT StudentID, FirstName, LastName, Grade, AverageGrade FROM Students ORDER BY AverageGrade ASC LIMIT 5")
for row in cursor.fetchall():
    print(row)
print("(showing first 5)")

print("\nTop 10 highest grades:")
cursor.execute("SELECT StudentID, FirstName, LastName, AverageGrade FROM Students ORDER BY AverageGrade DESC LIMIT 10")
for row in cursor.fetchall():
    print(row)
print()


# ---------------------------------------------------------------------------
# PART 5 – AGGREGATE FUNCTIONS
# ---------------------------------------------------------------------------

print("=== PART 5: Aggregate Functions ===")

print("\nAverage grade across all students:")
cursor.execute("SELECT AVG(AverageGrade) FROM Students")
avg = cursor.fetchone()[0]
print(f"Average: {avg:.2f}")

print("\nLowest and highest grades:")
cursor.execute("SELECT MIN(AverageGrade), MAX(AverageGrade) FROM Students")
min_g, max_g = cursor.fetchone()
print(f"Lowest: {min_g:.2f}, Highest: {max_g:.2f}")

print("\nAverage grade for Grade 11 students:")
cursor.execute("SELECT AVG(AverageGrade) FROM Students WHERE Grade = 11")
avg_11 = cursor.fetchone()[0]
print(f"Average: {avg_11:.2f}")
print()


# ---------------------------------------------------------------------------
# PART 6 – FINDING UNIQUE VALUES
# ---------------------------------------------------------------------------

print("=== PART 6: Finding Unique Values ===")

print("\nAll unique grade levels:")
cursor.execute("SELECT DISTINCT Grade FROM Students ORDER BY Grade")
grades = [row[0] for row in cursor.fetchall()]
print(grades)

print("\nNumber of different grades:")
cursor.execute("SELECT COUNT(DISTINCT Grade) FROM Students")
distinct_count = cursor.fetchone()[0]
print(f"Count: {distinct_count}")
print()


# ---------------------------------------------------------------------------
# PART 7 – STRING OPERATIONS
# ---------------------------------------------------------------------------

print("=== PART 7: String Filtering ===")

print("\nStudents whose name starts with 'A':")
cursor.execute("SELECT StudentID, FirstName, LastName FROM Students WHERE FirstName LIKE 'A%'")
for row in cursor.fetchall()[:5]:
    print(row)
print(f"(showing first 5 of {cursor.rowcount} total)")

print("\nStudents with example.com email:")
cursor.execute("SELECT StudentID, FirstName, Email FROM Students WHERE Email LIKE '%.com'")
for row in cursor.fetchall()[:5]:
    print(row)
print(f"(showing first 5)")
print()


# ---------------------------------------------------------------------------
# PART 8 – COMBINING CONDITIONS
# ---------------------------------------------------------------------------

print("=== PART 8: Multiple Conditions (AND, OR) ===")

print("\nGrade 12 students with average >= 85:")
cursor.execute("SELECT StudentID, FirstName, LastName, Grade, AverageGrade FROM Students WHERE Grade = 12 AND AverageGrade >= 85")
for row in cursor.fetchall():
    print(row)
print(f"Total: {cursor.rowcount}")

print("\nGrade 10 students OR last name starts with 'S':")
cursor.execute("SELECT StudentID, FirstName, LastName, Grade FROM Students WHERE Grade = 10 OR LastName LIKE 'S%'")
for row in cursor.fetchall()[:5]:
    print(row)
print(f"(showing first 5 of {cursor.rowcount} total)")
print()


# ---------------------------------------------------------------------------
# PART 9 – LIMITING RESULTS
# ---------------------------------------------------------------------------

print("=== PART 9: Limiting Results ===")

print("\nFirst 15 students:")
cursor.execute("SELECT StudentID, FirstName, LastName FROM Students LIMIT 15")
for i, row in enumerate(cursor.fetchall(), 1):
    print(f"{i}. {row}")

print("\nStudents 21-30:")
cursor.execute("SELECT StudentID, FirstName, LastName FROM Students LIMIT 10 OFFSET 20")
for i, row in enumerate(cursor.fetchall(), 21):
    print(f"{i}. {row}")
print()


# ---------------------------------------------------------------------------
# PART 10 – CHALLENGE QUERIES
# ---------------------------------------------------------------------------

print("=== PART 10: Challenge ===")

print("\nTop 5 students by grade:")
cursor.execute("SELECT StudentID, FirstName, LastName, AverageGrade FROM Students ORDER BY AverageGrade DESC LIMIT 5")
for rank, row in enumerate(cursor.fetchall(), 1):
    print(f"{rank}. {row}")

print("\nNumber of students per grade:")
cursor.execute("SELECT Grade, COUNT(*) FROM Students GROUP BY Grade ORDER BY Grade")
for grade, count in cursor.fetchall():
    print(f"Grade {grade}: {count} students")

print("\nStudents with 'Smith' in name or .edu email (ordered by grade):")
cursor.execute("SELECT StudentID, FirstName, LastName, Email, Grade FROM Students WHERE LastName LIKE '%Smith%' OR Email LIKE '%.edu' ORDER BY Grade DESC")
for row in cursor.fetchall():
    print(row)
print()


# ---------------------------------------------------------------------------
# CLEANUP
# ---------------------------------------------------------------------------

db_connection.close()
print("✓ Database connection closed.")
print()
print("=" * 60)
print("SOLUTION KEY VERIFICATION COMPLETE")
print("=" * 60)

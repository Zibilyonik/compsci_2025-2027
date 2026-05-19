-- IB DP CompSci - Topic A3 - Pure SQL Exercises
-- This file contains SQL-only exercises. No Python required!
-- 
-- HOW TO USE:
-- 1. Copy each query and paste it into your SQL client
-- 2. Replace TODO sections with your SQL code
-- 3. Run each query and verify the results
--
-- See SQL_TOOLS_GUIDE.md for instructions on which application to use
-- ============================================================================

-- ============================================================================
-- PART 1: BASIC DATA RETRIEVAL
-- ============================================================================

-- Exercise 1.1: Get all students
-- TODO: Write a query to select all columns for all students
SELECT * FROM Students;


-- Exercise 1.2: Get first 10 students with just name and email
-- TODO: Write a query to select only FirstName, LastName, and Email for the first 10 students
SELECT FirstName, LastName, Email FROM Students LIMIT 10;


-- Exercise 1.3: Count total number of students
-- TODO: Write a query to count how many students are in the database
SELECT COUNT(*) FROM Students;


-- ============================================================================
-- PART 2: FILTERING WITH WHERE
-- ============================================================================

-- Exercise 2.1: Find all Grade 12 students
-- TODO: Write a query to find all students in Grade 12
SELECT * FROM Students WHERE Grade = 12;


-- Exercise 2.2: Find students with average grade above 90
-- TODO: Write a query to find students whose AverageGrade is greater than 90
SELECT FirstName, LastName, AverageGrade FROM Students WHERE AverageGrade > 90;


-- Exercise 2.3: Find students in Grade 11 with average below 70
-- TODO: Write a query using AND to find Grade 11 students with low grades
SELECT FirstName, LastName, Grade, AverageGrade FROM Students WHERE Grade = 11 AND AverageGrade < 70;


-- Exercise 2.4: Find students in either Grade 9 or Grade 12
-- TODO: Write a query using OR to find Grade 9 OR Grade 12 students
SELECT FirstName, LastName, Grade FROM Students WHERE Grade = 9 OR Grade = 12;


-- ============================================================================
-- PART 3: SORTING AND ORDERING
-- ============================================================================

-- Exercise 3.1: List students sorted by average grade (highest first)
-- TODO: Write a query to sort students by AverageGrade in descending order
SELECT FirstName, LastName, AverageGrade FROM Students ORDER BY AverageGrade DESC;


-- Exercise 3.2: List all students sorted alphabetically by last name
-- TODO: Write a query to sort students by LastName in ascending order
SELECT FirstName, LastName FROM Students ORDER BY LastName ASC;


-- Exercise 3.3: Top 5 highest performing students
-- TODO: Write a query to get the top 5 students by average grade
SELECT FirstName, LastName, AverageGrade FROM Students ORDER BY AverageGrade DESC LIMIT 5;


-- ============================================================================
-- PART 4: AGGREGATE FUNCTIONS
-- ============================================================================

-- Exercise 4.1: Average grade of all students
-- TODO: Write a query to calculate the average (mean) of all AverageGrades
SELECT AVG(AverageGrade) FROM Students;


-- Exercise 4.2: Highest and lowest grades
-- TODO: Write a query to find both the MAX and MIN AverageGrade
SELECT MAX(AverageGrade), MIN(AverageGrade) FROM Students;


-- Exercise 4.3: Count students per grade
-- TODO: Write a query to count how many students are in each grade
-- HINT: Use GROUP BY Grade
SELECT Grade, COUNT(*) FROM Students GROUP BY Grade ORDER BY Grade;


-- Exercise 4.4: Average grade by grade level
-- TODO: Write a query to find the average AverageGrade for each Grade
-- HINT: Use GROUP BY Grade and AVG()
SELECT Grade, AVG(AverageGrade) FROM Students GROUP BY Grade ORDER BY Grade;


-- ============================================================================
-- PART 5: TEXT OPERATIONS AND PATTERNS
-- ============================================================================

-- Exercise 5.1: Find students whose first name starts with 'M'
-- TODO: Write a query using LIKE to find FirstNames starting with 'M'
SELECT FirstName, LastName FROM Students WHERE FirstName LIKE 'M%';


-- Exercise 5.2: Find all students with Polish email domain
-- TODO: Write a query using LIKE to find emails ending with '.edu.pl'
SELECT FirstName, LastName, Email FROM Students WHERE Email LIKE '%.edu.pl';


-- Exercise 5.3: Count students by email domain
-- TODO: Write a query to count how many students have .edu.pl domain
-- HINT: Use LIKE in WHERE clause with COUNT()
SELECT COUNT(*) FROM Students WHERE Email LIKE '%.edu.pl';


-- Exercise 5.4: Find names with specific pattern
-- TODO: Write a query to find students whose last name contains 'ski' or 'ska'
-- HINT: Use LIKE with wildcards
SELECT FirstName, LastName FROM Students WHERE LastName LIKE '%ski' OR LastName LIKE '%ska';


-- ============================================================================
-- PART 6: DISTINCT VALUES
-- ============================================================================

-- Exercise 6.1: List all unique grades
-- TODO: Write a query to find all distinct Grade values
SELECT DISTINCT Grade FROM Students ORDER BY Grade;


-- Exercise 6.2: How many different grade levels exist?
-- TODO: Write a query to count the number of distinct grades
SELECT COUNT(DISTINCT Grade) FROM Students;


-- Exercise 6.3: List unique first names
-- TODO: Write a query to get all distinct first names (no duplicates)
SELECT DISTINCT FirstName FROM Students ORDER BY FirstName;


-- ============================================================================
-- PART 7: COMPLEX QUERIES (COMBINING CONCEPTS)
-- ============================================================================

-- Exercise 7.1: Students with above-average grades
-- TODO: Write a query to find students whose AverageGrade is above the overall average
-- HINT: Use a subquery with AVG() in the WHERE clause
SELECT FirstName, LastName, AverageGrade FROM Students 
WHERE AverageGrade > (SELECT AVG(AverageGrade) FROM Students)
ORDER BY AverageGrade DESC;


-- Exercise 7.2: Grade 12 students sorted by performance
-- TODO: Write a query to get Grade 12 students, sorted by average grade (highest first)
SELECT FirstName, LastName, AverageGrade FROM Students 
WHERE Grade = 12 
ORDER BY AverageGrade DESC;


-- Exercise 7.3: Students enrolled in the last year
-- TODO: Write a query to find students enrolled after 2025-01-01
-- HINT: Use DATE comparison in WHERE clause
-- NOTE: EnrollmentDate is a proper DATE type, so comparison works directly
SELECT FirstName, LastName, EnrollmentDate FROM Students 
WHERE EnrollmentDate > '2025-01-01'
ORDER BY EnrollmentDate DESC;


-- Exercise 7.4: Best performing students in each grade
-- TODO: Write a query to find the highest average grade for each grade level
-- HINT: Use GROUP BY with MAX()
SELECT Grade, MAX(AverageGrade) FROM Students GROUP BY Grade ORDER BY Grade;


-- ============================================================================
-- PART 8: CHALLENGE QUERIES
-- ============================================================================

-- Challenge 8.1: Statistics summary
-- TODO: Write a query to show:
-- - Total students, Average grade, Highest grade, Lowest grade
-- Use multiple aggregate functions
SELECT 
    COUNT(*) as TotalStudents,
    ROUND(AVG(AverageGrade), 2) as AverageGrade,
    MAX(AverageGrade) as HighestGrade,
    MIN(AverageGrade) as LowestGrade
FROM Students;


-- Challenge 8.2: Students between grade 85-90 in Grade 11
-- TODO: Find Grade 11 students with average grades between 85 and 90 (inclusive)
-- HINT: Use BETWEEN operator
SELECT FirstName, LastName, AverageGrade FROM Students 
WHERE Grade = 11 AND AverageGrade BETWEEN 85 AND 90
ORDER BY AverageGrade DESC;


-- Challenge 8.3: Count by grade with filtering
-- TODO: Count students in each grade, but only show grades with 20+ students
-- HINT: Use GROUP BY with HAVING clause
SELECT Grade, COUNT(*) as StudentCount FROM Students 
GROUP BY Grade 
HAVING COUNT(*) >= 20
ORDER BY Grade;


-- Challenge 8.4: Top student per grade
-- TODO: Find the top student (highest average grade) in each grade level
-- HINT: This is complex! You'll need GROUP BY and MAX()
SELECT Grade, MAX(AverageGrade) as TopGrade FROM Students 
GROUP BY Grade 
ORDER BY Grade;


-- ============================================================================
-- BONUS: ADVANCED QUERIES (FOR EXTRA PRACTICE)
-- ============================================================================

-- Bonus 1: Students with names starting with vowels
-- TODO: Find students whose first name starts with A, E, I, O, or U
SELECT FirstName, LastName FROM Students 
WHERE FirstName LIKE 'A%' 
   OR FirstName LIKE 'E%' 
   OR FirstName LIKE 'I%' 
   OR FirstName LIKE 'O%' 
   OR FirstName LIKE 'U%'
ORDER BY FirstName;


-- Bonus 2: Calculate grade distribution percentage
-- TODO: For each grade, show the count and percentage of total students
SELECT 
    Grade,
    COUNT(*) as StudentCount,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM Students), 1) as Percentage
FROM Students
GROUP BY Grade
ORDER BY Grade;


-- Bonus 3: Find all-rounders (high grades in all levels)
-- TODO: Find the average grade for students, list those with average > 85
SELECT 
    FirstName, 
    LastName, 
    Grade,
    AverageGrade
FROM Students
WHERE AverageGrade > 85
ORDER BY AverageGrade DESC, Grade;


-- ============================================================================
-- REFLECTION QUESTIONS
-- ============================================================================
-- After completing these exercises, think about these questions:
--
-- 1. What's the difference between COUNT(*) and COUNT(DISTINCT grade)?
-- 2. Why would you use WHERE vs HAVING?
-- 3. What happens if you forget the GROUP BY clause when using COUNT()?
-- 4. How would you find the students with the EXACT average grade?
-- 5. Can you combine LIKE patterns in one query efficiently?
--
-- ============================================================================

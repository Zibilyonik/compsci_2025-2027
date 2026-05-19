# Topic A3: Databases - Complete Module Index

## 📚 What's in This Module?

This folder contains everything your students need to learn SQL and databases for the IB DP Computer Science curriculum.

## 📂 Files Overview

### 1. **Intro.md** - Conceptual Foundation
- Comprehensive introduction to databases
- Relational database concepts
- SQL fundamentals
- Key terminology and relationships
- Perfect for understanding the "WHY" behind databases

**Start here first!** Read this for context before coding.

---

### 2. **README.md** - Getting Started Guide
- Module overview
- How to use the exercise files
- Learning progression (Beginner → Intermediate → Advanced)
- Tips for success
- Common mistakes to avoid

**Read this before attempting exercises.**

---

### 3. **sql_exercises.py** - Python-Based Interactive Exercises
- 10-part progressive exercise set
- Beginner to advanced difficulty
- Students write SQL queries inside Python
- Connects to `school_data.sqlite`
- Provides immediate visual feedback

**Great for:** Learning SQL while staying in Python environment

**How to use:**
```bash
python sql_exercises.py
```

Then fill in each TODO section with SQL queries.

---

### 4. **sql_queries.sql** - Pure SQL Exercise File ⭐ NEW
- 8 sections of SQL-only exercises
- 20+ individual practice queries
- No Python required - pure SQL
- Bonus challenges included
- Reflection questions for deeper learning

**Great for:** Getting real SQL experience outside Python

**How to use:** See SQL_TOOLS_GUIDE.md

---

### 5. **SQL_TOOLS_GUIDE.md** - Tool Recommendations ⭐ NEW
- **4 different ways** to run SQL queries:
  1. DB Browser for SQLite (Easiest - Recommended)
  2. SQLite Command Line (Most Direct)
  3. VS Code with SQLite Extension
  4. Online SQLite Editors (No Installation)

- Pros/cons of each approach
- Step-by-step setup instructions
- Comparison table
- Troubleshooting guide

**Essential reading** for students to know how to run SQL queries.

---

### 6. **sql_exercises_key.py** - Instructor Solution Key
- Complete working solutions to all Python-based exercises
- Can be run to verify approach
- Shows best practices for SQL in Python
- For teacher reference only

---

### 7. **school_data.sqlite** - Practice Database ⭐
- 100 realistic student records
- 35% Polish names (with correct gender grammar: -ski/-ska)
- 65% international names (Korean, Indian, Japanese, Turkish, Georgian, Spanish, German, North African)
- All emails use: `example.student.edu.pl`
- 7 columns: StudentID, FirstName, LastName, Grade, Email, EnrollmentDate, AverageGrade

---

## 🎯 Recommended Learning Path

### Week 1 - Conceptual Understanding
1. Read **Intro.md** (database concepts)
2. Read **README.md** (how to use materials)
3. Watch SQL tutorials (external resources)

### Week 2 - SQL Basics with Python
1. Choose a tool from **SQL_TOOLS_GUIDE.md**
2. Run simple queries from **sql_queries.sql**
3. Complete Part 1 of **sql_exercises.py**

### Week 3 - Intermediate SQL
1. Complete Parts 2-5 of **sql_exercises.py**
2. Work through **sql_queries.sql** sections 2-5
3. Compare results with **sql_exercises_key.py**

### Week 4 - Advanced SQL
1. Complete Parts 6-10 of **sql_exercises.py**
2. Work through Challenge sections in **sql_queries.sql**
3. Create your own queries

### Week 5 - Pure SQL Practice
1. Use a SQL tool (DB Browser or CLI)
2. Complete all exercises in **sql_queries.sql**
3. Reflect on questions at the end

---

## 💡 Quick Start

### Option A: Python-Based (Beginner-Friendly)
```bash
cd Course\10.Databases
python sql_exercises.py
```

### Option B: Pure SQL (Real SQL Experience)
1. Read SQL_TOOLS_GUIDE.md
2. Download DB Browser for SQLite
3. Open `school_data.sqlite`
4. Copy queries from `sql_queries.sql`
5. Run and learn!

---

## 📊 Database Structure

### Students Table
```
StudentID (INTEGER) - Primary Key
FirstName (TEXT)    - Student's first name
LastName (TEXT)     - Student's last name
Grade (INTEGER)     - Grade level (9-12)
Email (TEXT)        - School email
EnrollmentDate (DATE) - When student enrolled (YYYY-MM-DD format)
AverageGrade (REAL) - Academic average (60-100)
```

### Sample Records
```
1  | Stanislaw | Nowak     | 9  | stanislaw.nowak123@example.student.edu.pl | 2026-05-02 | 91.65
2  | Yuki      | Aslan     | 11 | yuki.aslan456@example.student.edu.pl      | 2022-04-18 | 98.71
5  | Beata     | Zielinska | 12 | beata.zielinska789@example.student.edu.pl | 2022-11-29 | 94.61
```

---

## 🔧 Tools Required

### Minimum (Just for Python exercises):
- Python 3.x (built-in sqlite3 module)
- Text editor

### Recommended (For pure SQL exercises):
- **DB Browser for SQLite** (free, easy) - https://sqlitebrowser.org/
- OR Command line `sqlite3` (usually pre-installed)

### Optional:
- VS Code with SQLite extension
- Online SQLite editor (no installation)

---

## 📈 Difficulty Progression

### sql_exercises.py
- **Part 1**: Connecting and exploring (EASY)
- **Part 2**: Basic SELECT queries (EASY)
- **Part 3**: Filtering with WHERE (EASY)
- **Part 4**: Ordering and sorting (MEDIUM)
- **Part 5**: Aggregate functions (MEDIUM)
- **Part 6**: Distinct values (MEDIUM)
- **Part 7**: String operations (MEDIUM)
- **Part 8**: Multiple conditions (MEDIUM)
- **Part 9**: Limiting results (MEDIUM)
- **Part 10**: Challenge queries (HARD)

### sql_queries.sql
- **Part 1**: Basic retrieval (EASY)
- **Part 2**: Filtering (EASY)
- **Part 3**: Sorting (MEDIUM)
- **Part 4**: Aggregates (MEDIUM)
- **Part 5**: Text operations (MEDIUM)
- **Part 6**: Distinct values (MEDIUM)
- **Part 7**: Complex queries (HARD)
- **Part 8**: Challenges (HARD)
- **Bonus**: Advanced queries (VERY HARD)

---

## ✅ Learning Outcomes

By completing this module, students will:

- ✓ Understand relational database design principles
- ✓ Write basic to advanced SQL SELECT queries
- ✓ Filter, sort, and aggregate data effectively
- ✓ Handle text patterns and string operations
- ✓ Use GROUP BY and HAVING clauses
- ✓ Write subqueries and complex logic
- ✓ Solve real-world data retrieval problems
- ✓ Use multiple SQL tools and environments
- ✓ Apply proper SQL syntax and conventions
- ✓ Understand the difference between Python and pure SQL

---

## 🚀 Extension Activities

### For Advanced Students:
1. Create new tables (e.g., Teachers, Courses, Enrollments)
2. Write queries with JOINs (when covered later)
3. Create views for common queries
4. Write INSERT and UPDATE statements
5. Explore database normalization

### Real-World Applications:
1. Query your school's actual database (with permission)
2. Analyze sports statistics with SQL
3. Explore public datasets (Kaggle, data.gov)
4. Build reports with SQL queries

---

## 🐛 Troubleshooting

### "Module sqlite3 not found"
- Python wasn't installed properly
- Reinstall Python with sqlite3 included

### "Cannot open database file"
- Wrong file path
- Database not in the right folder
- Check: `10.Databases\school_data.sqlite`

### SQL queries return empty results
- Check column names (must match exactly)
- Verify WHERE conditions are correct
- Test with simpler queries first

### "Syntax error in SQL statement"
- Missing semicolon at end
- Misspelled keyword
- Missing quotes around text
- Check query carefully

### See SQL_TOOLS_GUIDE.md for more solutions

---

## 📖 External Resources

- **SQLite Official:** https://www.sqlite.org/
- **W3Schools SQL:** https://www.w3schools.com/sql/
- **Khan Academy:** https://www.khanacademy.org/computing/
- **DB Browser Help:** https://sqlitebrowser.org/help/
- **SQL Tutorial:** https://www.sqlitetutorial.net/

---

## 📝 Assessment Suggestions

### Quizzes:
- Write queries to solve specific problems
- Identify errors in given queries
- Explain what each query does

### Projects:
- Create a database and write queries
- Analyze the school_data.sqlite database
- Answer specific research questions with SQL

### Practical Exams:
- Students given queries to write
- Must write pure SQL (no Python)
- Time-limited (45-90 minutes)

---

## 👨‍🏫 Teacher Notes

### Setup Time
- ~10 minutes to copy files
- No special installation needed
- Database is pre-loaded with 100 records

### First Class
- Have students read Intro.md and README.md
- Show them how to run sql_exercises.py
- Demonstrate a simple query

### Pacing Suggestions
- 5 weeks for comprehensive coverage
- 3 weeks for accelerated track
- Can be parallelized with other topics

### Student Assessment
- Python exercises (sql_exercises.py): Can auto-grade by output
- Pure SQL (sql_queries.sql): Verify query results
- Compare with solution keys provided

---

## 📋 Checklist for Setup

- [ ] Verified all 7 files are present
- [ ] Tested database connectivity
- [ ] Verified 100 student records exist
- [ ] Tested python sql_exercises.py
- [ ] Installed or provided DB Browser/SQLite tool
- [ ] Students can read all documentation
- [ ] SQL_TOOLS_GUIDE.md shared with students

---

## 🎓 IB DP Alignment

This module covers:
- **Topic A3: Databases**
  - Relational database concepts
  - Database design principles
  - SQL query fundamentals
  - Data retrieval and manipulation

Supporting skills for:
- **Internal Assessment** - Data management component
- **Paper 1 & 2** - Database questions and case studies
- **Computational Thinking** - Structured data representation

---

## Version History

- v1.0 - Initial module creation
  - Intro.md
  - README.md
  - sql_exercises.py
  - sql_exercises_key.py
  - school_data.sqlite
  
- v1.1 - Added pure SQL support
  - sql_queries.sql (NEW)
  - SQL_TOOLS_GUIDE.md (NEW)
  - This index document (NEW)
  - Polish grammar corrections (ski→ska for females)
  - Internationalized student names

---

**Happy Teaching! 🎉**

Questions or suggestions? Refer to the individual guide files or contact the module maintainer.

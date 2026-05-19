# SQL Tools Guide - How to Run Pure SQL Exercises

This guide shows you **three different ways** to run the SQL exercises from `sql_queries.sql`. Choose the one that works best for you!

## Option 1: DB Browser for SQLite (Easiest - Recommended)

**What is it?** A free, user-friendly GUI application for working with SQLite databases.

**Pros:**
- ✓ No command line needed
- ✓ Visual interface (point and click)
- ✓ See results in a nice table format
- ✓ Can edit and view database structure
- ✓ Works on Windows, Mac, and Linux

**Cons:**
- ✗ Needs to be installed

### Installation

1. Go to https://sqlitebrowser.org/
2. Download the version for your operating system
3. Install it (just like any other application)

### How to Use

1. **Open the database:**
   - Launch DB Browser for SQLite
   - Click "Open Database"
   - Navigate to: `Course\10.Databases\school_data.sqlite`
   - Click "Open"

2. **Run SQL queries:**
   - Click the "Execute SQL" tab at the top
   - Copy a query from `sql_queries.sql`
   - Paste it into the SQL editor
   - Click the "Execute" button (play icon) or press Ctrl+Enter
   - See results below!

3. **Tips:**
   - You can run one query at a time
   - Use Ctrl+Enter to quickly execute
   - Results show in a nice table
   - You can scroll right to see more columns

### Example Workflow

```
1. Open DB Browser → Open school_data.sqlite
2. Click "Execute SQL" tab
3. Paste this query:
   SELECT FirstName, LastName, Grade FROM Students LIMIT 5;
4. Press Ctrl+Enter
5. See results in the table below!
```

---

## Option 2: SQLite Command Line (Most Direct)

**What is it?** The official SQLite command-line tool. Already installed on most computers!

**Pros:**
- ✓ No extra software to install
- ✓ Direct database access
- ✓ Very fast
- ✓ Used by professionals

**Cons:**
- ✗ Requires command line knowledge
- ✗ Results are text-based (not visual tables)

### How to Use

1. **Open Command Prompt (Windows) or Terminal (Mac/Linux)**
   
2. **Navigate to the database folder:**
   ```bash
   cd "F:\Onur Projects\compsci_2025-2027\Course\10.Databases"
   ```

3. **Start SQLite:**
   ```bash
   sqlite3 school_data.sqlite
   ```
   
   You should see:
   ```
   SQLite version 3.x.x
   sqlite>
   ```

4. **Run a query:**
   ```sql
   SELECT FirstName, LastName, Grade FROM Students LIMIT 5;
   ```
   
   Then press Enter. Results appear as text.

5. **Exit SQLite:**
   ```sql
   .exit
   ```

### Useful Commands

```sql
-- List all tables
.tables

-- Show table structure
.schema Students

-- Set output format to pretty table
.mode column
.headers on

-- Run a whole SQL file
.read sql_queries.sql

-- Export results to file
.output results.txt
SELECT * FROM Students;
.output stdout
```

### Example Session

```
$ sqlite3 school_data.sqlite
SQLite version 3.40.0
sqlite> SELECT COUNT(*) FROM Students;
100
sqlite> SELECT FirstName, LastName FROM Students LIMIT 3;
Magdalena | Krol
Maria | Szymanska
Ahmed | Youssef
sqlite> .exit
```

---

## Option 3: VS Code with SQLite Extension

**What is it?** Use VS Code (if you have it) with a SQLite extension.

**Pros:**
- ✓ Built into your coding environment
- ✓ Integrates with your projects
- ✓ Good if you already use VS Code

**Cons:**
- ✗ Only works if VS Code is installed
- ✗ Extension must be installed

### Setup

1. **Open VS Code**

2. **Install SQLite Extension:**
   - Click Extensions (left sidebar)
   - Search for "SQLite"
   - Install "SQLite" by alexcvzz
   - Reload VS Code

3. **Open the database:**
   - Press Ctrl+Shift+P
   - Type "SQLite: Open Database"
   - Select `school_data.sqlite`

4. **Run queries:**
   - Open `sql_queries.sql` in VS Code
   - Select a query
   - Press Ctrl+Shift+P → "SQLite: Run Query"
   - Results show in output panel

---

## Option 4: Online SQLite Editors (No Installation)

**What is it?** Web-based SQLite tools you can use in your browser.

**Pros:**
- ✓ No installation needed
- ✓ Works anywhere with internet
- ✓ Very simple

**Cons:**
- ✗ Can't directly access your local file
- ✗ Need to upload database first
- ✗ Limited features

### Popular Online Tools

1. **sqliteonline.com**
   - Go to https://sqliteonline.com
   - Click "File" → "Import"
   - Upload `school_data.sqlite`
   - Write SQL queries in the editor
   - Click "Run"

2. **db.sqlstudio.com**
   - Similar process
   - Upload your database
   - Write and run queries

### Note for Online Tools
These are good for quick testing but slower than local tools. For classroom use, DB Browser or command line is faster.

---

## Comparison Table

| Tool | Ease of Use | Setup Time | Visual | Speed | Best For |
|------|------------|-----------|--------|-------|----------|
| **DB Browser** | ⭐⭐⭐⭐⭐ | 5 min | ✓ | Fast | Beginners |
| **SQLite CLI** | ⭐⭐⭐ | 0 min | ✗ | Very Fast | Power users |
| **VS Code** | ⭐⭐⭐⭐ | 2 min | ✓ | Fast | Developers |
| **Online** | ⭐⭐⭐⭐⭐ | 0 min | ✓ | Slow | Quick tests |

---

## Recommended Path for Students

### Beginners:
1. **Start with:** DB Browser for SQLite (easiest, visual)
2. **Then try:** SQLite CLI (more powerful)

### Advanced:
1. **Use:** Command line (sqlite3) for speed
2. **Or:** VS Code if doing other coding

### Laptops with no admin rights:
- Use **Online SQLite editors** (no installation needed)

---

## Tips for Success

### When running `sql_queries.sql`:

1. **Copy one query at a time**
   - Don't copy the whole file
   - Copy individual exercises

2. **Replace TODO sections**
   - Find lines with `TODO:`
   - Write your SQL code to replace them
   - Test your code

3. **Read error messages**
   - If you get an error, read it carefully
   - Common errors: Missing semicolons, misspelled column names

4. **Check syntax**
   - SQL keywords are usually UPPERCASE
   - Column names must match exactly (case-sensitive for data)
   - Don't forget semicolons at the end

### Common Issues & Solutions

**Problem:** "sqlite3 command not found"
- **Solution:** SQLite might not be in your PATH
- **Try:** Use DB Browser instead

**Problem:** "Cannot open database"
- **Solution:** Wrong file path
- **Try:** Use the full path or navigate to the folder first

**Problem:** Results look weird (all in one line)
- **Solution:** Terminal formatting issue
- **Try:** Use DB Browser or add `.mode column` in sqlite3

**Problem:** "No such column: FirstName"
- **Solution:** Column name typo or doesn't exist
- **Try:** Check spelling matches the database

---

## Learn More

- **SQLite Official:** https://www.sqlite.org/cli.html
- **DB Browser Help:** https://sqlitebrowser.org/help/
- **W3Schools SQL:** https://www.w3schools.com/sql/

---

## Quick Start Checklist

For DB Browser (recommended):
- [ ] Download and install DB Browser
- [ ] Open `school_data.sqlite` with DB Browser
- [ ] Click "Execute SQL" tab
- [ ] Copy first query from `sql_queries.sql`
- [ ] Paste and run it
- [ ] See results!

For Command Line:
- [ ] Open Command Prompt/Terminal
- [ ] Navigate to `10.Databases` folder
- [ ] Run `sqlite3 school_data.sqlite`
- [ ] Copy a query and run it
- [ ] Type `.exit` to quit

---

**Ready to practice SQL?** Pick a tool above and get started! 🚀

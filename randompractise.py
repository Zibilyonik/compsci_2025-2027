DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS teacher;
PRAGMA foreign_keys = ON;
CREATE TABLE teacher(
    teacherID INTEGER NOT NULL,
    teacherName TEXT NOT NULL,
    teacherSubject TEXT NOT FULL,
    PRIMARY KEY(teacherID)
);
CREATE TABLE student(
studentID INTEGER NOT NULL PRIMARY KEY,
studentName TEXT NOT NULL,
homeroomTeacherID INTEGER NOT NULL,
FOREIGN KEY (homeroomTeacherID) REFERENCES teacher(teacherID)
);
INSERT INTO teacher VALUES (0, "Kirill", "Maths"),(1,"Bjorn","History"),(2,"Imane", "German");
INSERT INTO student VALUES (0, "Miguel", 1),(1, "Lorainne", 2),(2, "Nadir", 0),(3, "Sam", 2),(4, "Mine", 1); 
ALTER TABLE teacher DROP COLUMN teacherName;
SELECT * FROM student WHERE homeroomTeacherID = 1;
SELECT * FROM student JOIN teacher ON student.homeroomTeacherID = teacher.teacherID;


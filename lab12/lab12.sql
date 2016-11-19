.read sp16data.sql
.read fa16data.sql

CREATE TABLE obedience AS
  SELECT seven, denero FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE students.smallest > 8 ORDER BY smallest asc LIMIT 20;

CREATE TABLE greatstudents AS
  SELECT this.date, this.number, this.pet, this.color, last.color
        FROM students AS this, sp16students AS last
    WHERE this.date = last.date AND this.number = last.number AND this.pet = last.pet;

CREATE TABLE sevens AS
   SELECT s.seven FROM students AS s, checkboxes AS c
    WHERE s.number = 7 AND c.'7' = 'True' AND s.time = c.time;;

CREATE TABLE matchmaker AS
   SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b
    WHERE a.time < b.time AND a.pet = b.pet AND a.song = b.song;

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes WHERE height > min AND height <= max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT child FROM dogs, parents WHERE name = parent ORDER BY -height;



-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  WITH
    siblings(first, second) AS (
      SELECT a.child, b.child FROM parents AS a, parents AS b
        WHERE a.parent = b.parent AND a.child < b.child
    )
  SELECT first || " and " || second || " are " || a.size || " siblings"
    FROM siblings, size_of_dogs AS a, size_of_dogs AS b
    WHERE a.size = b.size AND a.name = first AND b.name = second;



-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks AS
  WITH
    sums(names, total, n, max) AS (
      SELECT name, height, 1, height FROM dogs UNION
      SELECT names || ", " || name, total+height, n+1, height FROM sums, dogs
        WHERE n < 4 AND max < height
    )
  SELECT names, total FROM sums WHERE n=4 AND total>=170 ORDER BY total;



-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
CREATE TABLE non_parents AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE ints AS
    WITH i(n) AS (
        SELECT 1 UNION
        SELECT n+1 FROM i limit 100
    )
    SELECT n FROM i;


CREATE TABLE divisors AS
    WITH factors(i, j) AS (
        SELECT i.n,
        (SELECT count(j.n) FROM ints AS j WHERE i.n % j.n = 0 AND j.n <= 100)
        FROM ints AS i
    )
    SELECT i, j FROM factors;




CREATE TABLE primes AS
  SELECT i FROM divisors WHERE j = 2 ORDER BY i ASC;

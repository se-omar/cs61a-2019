.read lab13.sql

CREATE TABLE su19favpets AS
  SELECT pet, count(*) as count from students group by pet order by count desc, pet limit 10;


CREATE TABLE su19dog AS
  SELECT pet, count(*) as count from students where pet = "dog" group by pet;


CREATE TABLE obedienceimages AS
  SELECT seven, instructor, count(*) as count
  from students 
  where seven = '7'
  group by instructor;

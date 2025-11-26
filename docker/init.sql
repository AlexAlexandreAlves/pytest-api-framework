CREATE TABLE IF NOT EXISTS people (
    id SERIAL PRIMARY KEY,
    fname VARCHAR(100),
    age INT
);

INSERT INTO people (fname, age) VALUES ('Alice', 30);
INSERT INTO people (fname, age) VALUES ('Bob', 25);
INSERT INTO people (fname, age) VALUES ('Charlie', 35);
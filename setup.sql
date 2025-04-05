CREATE TABLE [book] (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL
);

CREATE TABLE [student] (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL UNIQUE
);

INSERT INTO book([name], author, genre) VALUES 
('Life of Nhi', 'Theng', 'History'), 
('Life of Theng', 'Nhi', 'Drama');

INSERT INTO student ([name], username, [password]) VALUES ('Nhi', 'nhinguyen', '81dc9bdb52d04dc20036dbd8313ed055');


import sqlite3
conn = sqlite3.connect('database.db')
conn.execute("DROP TABLE users")
conn.execute('CREATE TABLE Users (CPF TEXT NOT NULL PRIMARY KEY,Nome TEXT,quiz INTEGER,quizz INTEGER,quizzz INTEGER,quizzzz INTEGER,quizzzzz INTEGER)')
conn.close()
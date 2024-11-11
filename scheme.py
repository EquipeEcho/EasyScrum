import sqlite3
conn = sqlite3.connect('database.db')
print('certo')
conn.execute('CREATE TABLE Users (CPF TEXT,Nome TEXT,Q_I INTEGER,Q_II INTEGER,Q_III INTEGER,Q_IV INTEGER,Q_V INTEGER)')
print('certo2')
conn.close()
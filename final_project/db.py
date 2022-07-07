import sqlite3

conn = sqlite3.connect("database.db")
print("Opened db successfully")

onn.execute('''CREATE TABLE INFO 
(name TEXT,
hobby TEXT);''')
print("Table created successfully")
conn.close()
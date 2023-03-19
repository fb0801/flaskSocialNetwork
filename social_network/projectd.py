import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE posts (
    id INT primary key,
    uname text not null, 
    content text not null
);''')
print ("Table created successfully")

conn.close()
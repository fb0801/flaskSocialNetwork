import sqlite3 
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    conn = sqlite3.connect('test.db') #connect to db
    cur = conn.cursor() #grab what we need from db
    cur.execute('INSERT into posts (uname, content) values(?,?)', (name, content)) #sql stmt

    conn.commit()
    conn.close() 

def get_posts():
     conn = sqlite3.connect(path.join(ROOT, 'test.db'))
     cur = conn.cursor()
     cur.execute("SELECT * from posts") 
     posts = cur.fetchall()
     return posts

import sqlite3
import os

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    conn = sqlite3.connect('test.db') #connect to db
    cur = conn.cursor() #grab what we need from db
    cur.execute('INSERT into posts (name, content) values(?,?)', (name, content)) #sql stmt

    conn.Commit()
    conn.close() 

def get_posts():
     conn = sqlite3.connect(path.join(ROOT, 'test.db'))
     cur = conn.cursor()
     cur.execute("SELECT * from posts") 
     posts = cur.fetchall()
     return posts

import sqlite3

def show_all():
    conn = sqlite3.connect('test.db') #connect to db
    c = conn.cursor()

    #query db
    c.execute("SELECT * FROM posts")
    print("Success")

    #c.execute("INSERT INTO posts VALUES (1, 'Paul', 'California')")

    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit() #commit command

    conn.close() #close connection 


show_all()
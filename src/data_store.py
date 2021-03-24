import sqlite3

con = sqlite3.connect('passwords.db')


def add_password(website_name, password, user_name):
    cur = con.cursor()
    cur.execute("INSERT INTO passwords VALUES ('" + website_name + "','" + password + "','" + user_name + "') ")
    con.commit()


def get_password(website_name):
    cur = con.cursor()
    cur.execute("SELECT * FROM passwords WHERE website = '" + website_name + "'")
    return cur.fetchall()


def get_password_with_username(username):
    cur = con.cursor()
    cur.execute("SELECT * FROM passwords WHERE username = '" + username + "'")
    return cur.fetchall()


def get_all_passwords():
    cur = con.cursor()
    cur.execute("SELECT * from passwords")
    return cur.fetchall()


def setup():
    cur = con.cursor()
    cur.execute("CREATE TABLE if not exists passwords(website text, username text, password text)")
    con.commit()


def cleanup():
    con.close()

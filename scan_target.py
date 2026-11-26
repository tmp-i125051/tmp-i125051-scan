import sqlite3, subprocess, os

def get_user(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '%s'" % name)
    return cur.fetchone()

def run_cmd(user_input):
    return subprocess.check_output(user_input, shell=True)

def load(path):
    return eval(open(path).read())

if __name__ == "__main__":
    conn = sqlite3.connect("app.db")
    print(get_user(conn, "admin"))

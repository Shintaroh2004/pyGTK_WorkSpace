import sqlite3

class MainModel():
    def __init__(self):
        self.cur:sqlite3.Cursor = sqlite3.connect("./src/model/test.db").cursor()

    def select(self):
        self.cur.execute("select * from personal;")
        print(self.cur.fetchall())
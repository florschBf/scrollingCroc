import sqlite3
from os.path import exists

class DbController:

    def __init__(self, db_file, scene):
        try:
            conn = sqlite3.connect(db_file)
            print (conn)
        except:
            print("db error, no highscore")

    def init_db(self):
        cursor = conn.cursor()




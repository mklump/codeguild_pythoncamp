"""
Fills an SQL database from a text file: glossary.txt

sqlite> SELECT gl_term FROM glossary ORDER by gl_term COLLATE NOCASE;
.NET
Agile
AJAX
Apache
Apache Foundation
...

sqlite> select gl_definition from glossary where gl_term = "Tk";
a GUI tool kit, written in tcl.
"""

import sqlite3 as sql
import time
import os

FILE = "/Users/kurner/Downloads/glossary.txt"  # adjust as needed

def create_DB():

    # https://www.sqlite.org/lang_droptable.html
    DB.c.execute("""DROP TABLE IF EXISTS Glossary""")
    DB.c.execute("""CREATE TABLE Glossary
        (gl_term text PRIMARY KEY,
         gl_definition text,
         updated_at int,
         updated_by text)""")

class DB:

    backend  = 'sqlite3'
    user_initials  = 'KTU'
    timezone = int(time.strftime("%z", time.localtime()))
    target_path = '/Users/kurner/Documents/classroom_labs'
    db_name = ":memory:"
    db_name = os.path.join(target_path, 'glossary.db')

    @classmethod
    def mod_date(cls):
        return time.mktime(time.gmtime())  # GMT time

    @classmethod
    def connect(cls):
        if cls.backend == 'sqlite3':
            DB.conn = sql.connect(DB.db_name)
            DB.c = DB.conn.cursor()
        elif cls.backend == 'mysql':
            DB.conn = sql.connect(host='localhost',
                                  user='root', port='8889')
            DB.c = DB.conn.cursor()

    @classmethod
    def disconnect(cls):
        DB.conn.close()

    @classmethod
    def save_term(cls, *the_data):
        print(the_data)
        query = ("INSERT INTO Glossary "
        "(gl_term, gl_definition, updated_at, updated_by) "
        "VALUES ('{}', '{}', {}, '{}')".format(*the_data))
        # print(query)
        DB.c.execute(query)
        DB.conn.commit()

class DBcontext:

    def __enter__(self):
        DB.connect()

    def __exit__(self, *stuff_happens):
        DB.disconnect()
        if stuff_happens[0]:
            print(stuff_happens)
            return False
        return True

with DBcontext() as dbx:

    create_DB()

    with open(FILE, 'r', encoding='UTF-8') as gloss:
        lines = gloss.readlines()

    for line in lines:
        if len(line.strip()) == 0:
            continue
        term, definition = line.split(":", 1)
        right_now = DB.mod_date()
        DB.save_term(term[2:].strip(), definition.strip(), right_now, DB.user_initials)

print("Done!")
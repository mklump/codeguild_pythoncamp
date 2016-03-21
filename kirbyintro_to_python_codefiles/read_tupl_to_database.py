"""
Fills an SQL database from a text file: glossary.txt

sqlite> SELECT bk_name FROM glossary ORDER by bk_name COLLATE NOCASE;
.NET
Agile
AJAX
Apache
Apache Foundation
...

sqlite> select bk_url from glossary where bk_name = "Tk";
a GUI tool kit, written in tcl.
"""

import sqlite3 as sql
import time
import os
from collections import namedtuple

Bmk = namedtuple('Bookmark', 'place url')

# tuple of tuples
tuples = (
    ("Guild Programming Courses @ DropBox", "http://bit.ly/1TrSJFB"),
    ("Anaconda.org", "http://anaconda.org"),
    ("Python.org", "http://python.org"),
    ("Python Docs", "https://docs.python.org/3/"),
    ("'New Math' by Tom Lehrer (animated)","https://youtu.be/UIKGV2cTgqA"),
    ("Spaghetti Code", "http://c2.com/cgi/wiki?SpaghettiCode"),
    ("Structured Programming", "http://c2.com/cgi/wiki?StructuredProgramming"),
    ("Map of Languages", "http://archive.oreilly.com/pub/a/oreilly//news/languageposter_0504.html"),
    ("XKCD", "http://xkcd.com"),
    ("PDX Code Guild", "https://pdxcodeguild.com/"),
    ("Will 'Geeks' Rule? CBS News (world domination meme)","http://www.cbsnews.com/news/will-geeks-rule-the-world/"),
    ("Django","https://docs.djangoproject.com/"),
    ("PythonAnywhere","https://www.pythonanywhere.com/"),
    ("CodeAcademy: Python","https://www.codecademy.com/learn/python"),
    ("Unicode on Youtube", "https://www.youtube.com/watch?v=Z_sl99D2a18"),
    ("In Defense of Ada", "http://www.grunch.net/synergetics/adaessay.html"),
    ("Grace Hopper on Letterman", "https://www.youtube.com/watch?v=1-vcErOPofQ"),
    ("The Mind of a Genius: John von Neumann", "https://www.youtube.com/watch?v=XZ9tt72feL8"),
    ("World Domination meme", "https://www.google.com/search?q=linux+world+domination&safe=off&source=lnms&tbm=isch"),
    ("Warriors of the Net", "https://www.youtube.com/watch?v=PBWhzz_Gn10"),
    ("LAMP stack", "https://www.google.com/search?q=lamp+stack&safe=off&biw=787&bih=535&source=lnms&tbm=isch"),
    ("LAMP stack (Wikipedia)","https://en.wikipedia.org/wiki/LAMP_(software_bundle)"),
    ("In the Beginning was the Command Line", "http://c2.com/cgi/wiki?InTheBeginningWasTheCommandLine"),
    ("First Wiki","http://c2.com/cgi-bin/wiki" ),
    ("'Meme' on Wikipedia", "https://en.wikipedia.org/wiki/Meme"),
    ("Financial Data Visualization","http://finviz.com/map.ashx"),
    ("Human Development Index","http://hdr.undp.org/en/content/human-development-index-hdi"),
    ("Inside The Eye","http://ngm.nationalgeographic.com/2016/02/evolution-of-eyes-text"),
    ("Top 10 Languages to Learn in 2016", "https://youtu.be/Z56GLRXxh88"),
    ("Pretty Good Python Summary by Derek Banas", "https://youtu.be/N4mEzFDjqtA"),
    ("How To Think Like a Computer Scientist - Free Book","http://www.greenteapress.com/thinkpython/thinkCSpy.pdf"),
    ("SQL Syntax", "https://www.google.com/search?q=sql+syntax&safe=off&biw=787&bih=535&source=lnms&tbm=isch"),
    ("Python Cookbook","http://chimera.labs.oreilly.com/books/1230000000393/index.html"),
    ("Learn Python the Hard Way","http://learnpythonthehardway.org/book/"),
    ("What Is Code?","http://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/"),
    ("Become a Better Programmer Through Mundane Programming","http://mundaneprogramming.github.io/slides/#/"),
    )

# lets make these namedtuples instead OK?
# *tup explodes each tuple into two positionals, what Bmk expects
bookmarks = [Bmk(*tup) for tup in tuples] # list comprehension!
    
#for bmk in bookmarks:
#    # Bookmark(place='Anaconda.org', url='http://anaconda.org')
#    print(bmk)   # notice format of output
#    print("-")

FILE = "./BookMarkNamedTuple.txt"  # adjust as needed

def create_DB():

    # https://www.sqlite.org/lang_droptable.html
    DB.c.execute("""DROP TABLE IF EXISTS BookMarkNamedTuple""")
    DB.c.execute("""CREATE TABLE BookMarkNamedTuple
        (bk_name text PRIMARY KEY,
         bk_url text,
         updated_at int,
         updated_by text)""")

class DB:

    backend  = 'sqlite3'
    user_initials  = 'KTU'
    timezone = int(time.strftime("%z", time.localtime()))
    target_path = './'
    db_name = ":memory:"
    db_name = os.path.join(target_path, 'BookMarkNamedTuple.db')

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
        query = ("INSERT INTO BookMarkNamedTuple "
        "(bk_name, bk_url, updated_at, updated_by) "
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

   # with open(FILE, 'r', encoding='UTF-8') as gloss:
   #     lines = gloss.readlines()

for bmk in bookmarks:
	# Bookmark(place='Anaconda.org', url='http://anaconda.org')
	print(bmk)   # notice format of output
	print("-")
	if bmk != None and 0 != len(bmk.place.strip()) and 0 != len(bmk.url.strip()): #Nothing not defined only None object type.
		term, definition = line.split(":", 1)
		right_now = DB.mod_date()
		DB.save_term(term[2:].strip(), definition.strip(), right_now, DB.user_initials)

print("Done!")
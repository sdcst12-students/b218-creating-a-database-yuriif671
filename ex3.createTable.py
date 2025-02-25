#!python3
"""
The queries are the commands that we might type in to the command line.
When we have a query, we execute it.  The results are available to the cursor,
so we can fetch them and store them into a variable.

Commands are issued to a database using queries.  These are text commands
that are used to make requests to the database.  We will be learning commands to:
create tables
delete tables (you don't really want to do this very often)
retrieve information from a table
insert records into a table
modify records in a table
delete records in a table
We are going to create a new table in the database
"""

import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = """
create table if not exists customers (
    id integer primary key autoincrement,
    name tinytext,
    email tinytext,
    cnum int);
"""
cursor.execute(query)

"""
This program makes use of a multiline string literal from lines 25-31
Note that the triple " is used just like a regular ", but can create a
string literal that spans multiple lines. We do this for readability
as the spacing in the sql command doesnt really matter.

Why do you think it might be important to only create a table if it
doesn't exist?
In the good old days, people used to keep a rolodex of cards.  These would
be cards that each contained information.  We can think of a table as
containing many of these cards.  We start with an id, which is a unique
identifier to help us keep track of the cards.  Each record also has
reserved information, almost like a python dictionary.  We specify what
kind of data it contains.  Here, our record stores 3 pieces of information
(in addition to the id): name, email and cnum

The different data types in mysql can be found here:
https://www.w3schools.com/sql/sql_datatypes.asp
"""
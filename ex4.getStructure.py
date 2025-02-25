#!python3
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
cursor.execute('PRAGMA table_info(npc);')
"""
This pragma returns one row for each column in the named table. Columns in the result set include the 
column name, 
data type, 
whether or not the column can be NULL, 
and the default value for the column. 
The "pk" column in the result set is zero for columns that are not part of the primary key, 
and is the index of the column in the primary key for columns that are part of the primary key.

We won't be using the pragma command much, but this is useful for helping you remember how your
table is constructed if you forget."""
result = cursor.fetchall()
print(result)
for i in result:
    print(i)
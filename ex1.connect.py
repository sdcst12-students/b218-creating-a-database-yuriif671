#!python3

import sqlite3

"""
This creates a connection to a file that will contain the database.
The connection is attached to a variable that will serve as the handler
for all of our database commands or queries.  You can print the connection
to see the status of of the connection object and see if it was successful.
"""

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)
#!python3

import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = "select sqlite_version();"
cursor.execute(query)
result = cursor.fetchall()
print(type(result))
print(result)
for i in result:
    print(i)
"""
Let's analyze the code from lines 9-15
cursor = connection.cursor()
    First, we create a cursor for the connection we have established.  You
    can think of the cursor as a command prompt for a command line program,
    like the terminal we use for Python and Visual Studio Code.  
query = "select sqlite_version();"
    While setting your query into a variable is not necessary, sometimes we
    build the query by creating a string using variables, and it's nice to be
    able to print it out to see what the query have built is.
cursor.execute(query)
    We use the execute method for the cursor to run the query.  Note that
    here we used a variable, but you could type in an actual command, like:
    cursor.execute('select sqlite_version();')
    Note that in sql, we end every command with a ;
result = cursor.fetchall()
    Once we have executed the query, we need to grab the results. Here, we are
    storing them into a variable.
    The fetchall() method grabs all of the results and creates them as a list
    of tuples.  We can iterate through the list and look at each tuple.
"""


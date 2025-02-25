#!python3
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = "select * from npc"
"""
Note that instead of selecting ALL of the data, we can be more specific about what we select and
where we select from:
Try the following queries instead:

select name from customers
select name,cnum from customers
select name from customers where cnum > 10
select name from customers order by name asc
select * from customers order by cnum desc
"""
cursor.execute(query)
result = cursor.fetchall()
print(result)
for i in result:
    print(i)
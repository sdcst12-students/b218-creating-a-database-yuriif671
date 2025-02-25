#!python3
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
cursor.execute('delete from customers') 
#note, you don't want to delete the table data regularly, this is just for demo purposes
data = [
    ['Joe Mantenga','joe@sdss.ca',12345],
    ['Hanna Montana','miley@cyrus.com',32],
    ['Amanda Huggenkis','cool1@gmail.com',12],
    ['Michael Jackson','singer@thriller.com',1],
    ['Peter Nesmith','bassist@monkees.org',89]
    ]
for i in data:
    query = f"insert into customers (name,email,cnum) values ('{i[0]}','{i[1]}',{i[2]});"
    print(query)
    cursor.execute(query)
connection.commit()
query = "select * from customers"
cursor.execute(query)
result = cursor.fetchall()
print(result)
for i in result:
    print(i)
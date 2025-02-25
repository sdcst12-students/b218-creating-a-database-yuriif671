import sqlite3


ids = []
connection = sqlite3.connect('dbase.db')
cursor = connection.cursor()

q = 'pragma table_info(npc);'
cursor.execute(q)
result = cursor.fetchall()
#print(result)

q = 'select * from npc where level<3 order by level desc;'
#q = 'select * from npc where level>3 and level < 6 order by level asc limit 20;'
#q = "select * from npc where class='Samurai' order by strength asc"
#q = "select * from npc where class like '%an%'"
#q = "select * from npc where hp>20 and class='Ranger'"
#q = "select * from npc where gold>30 and (class = 'Ranger' or class='Samurai')"
#q = "select id,class,level from npc where gold>50"
#q = "select id from npc where gold>50"
cursor.execute(q)
result = cursor.fetchall()
print(f"There are {len(result)} results")
input("Press ENTER to see all results")
for i in result:
    print(i)
    ids.append(i[0])
print("\nID's of search results")
print(ids)

for i in ids:
    q = f"select * from npc where id={i}"
    cursor.execute(q)
    result = cursor.fetchone()
    print(result)
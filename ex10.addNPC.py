#!python3
import sqlite3
import random
file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
def r(n=1):
    # this rolls n number of 6 sided dice and returns the sum
    # eg r(4) rolls 4 dice and adds them together
    sum = 0
    for i in range(n):
        sum = sum + random.randint(1,6)    
    return sum

for i in range(1000):
    STR = r(3)
    INT = r(3)
    WIS = r(3)
    DEX = r(3)
    CON = r(3)
    CHA = r(3)
    LVL = r(2)
    HP = round((r(LVL)+r(LVL)+r(LVL))/3+LVL)
    GOLD = r(LVL)
    CLASS = random.choice(["Warrior","Ranger","Knight","Sorcerer","Sage","Priest","Thief","Bard","Barbarian","Monk","Assassin","Jester","Samurai"])
    
    
    query = f"insert into npc (strength,intelligence,wisdom,dexterity,constitution,charisma,class,level,hp,gold) values ({STR},{INT},{WIS},{DEX},{CON},{CHA},'{CLASS}',{LVL},{HP},{GOLD});"
    print(query)
    cursor.execute(query)

connection.commit()

import sqlite3

conn = sqlite3.connect("veterinarian.db")
cursor = conn.cursor()

#customers
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT,
        lname TEXT,
        phone TEXT,
        email TEXT UNIQUE,
        address TEXT,
        city TEXT,
        postalcode TEXT
    )
''')

# pets
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        type TEXT,
        breed TEXT,
        birthdate DATE,
        ownerID INTEGER,
        FOREIGN KEY (ownerID) REFERENCES customers(id) ON DELETE CASCADE
    )
''')

# visists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ownerid INTEGER,
        petid INTEGER,
        details TEXT,
        cost REAL,
        paid REAL,
        FOREIGN KEY (ownerid) REFERENCES customers(id) ON DELETE CASCADE,
        FOREIGN KEY (petid) REFERENCES pets(id) ON DELETE CASCADE
    )
''')

conn.commit()
conn.close()

def add_customer():
    conn = sqlite3.connect("veterinarian.db")
    cursor = conn.cursor()
    
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    postalcode = input("Enter postal code: ")
    
    cursor.execute("SELECT id FROM customers WHERE phone = ? OR email = ?", (phone, email))
    existing_customer = cursor.fetchone()
    
    if existing_customer:
        print("There is already a username with the same phone number or email")
        conn.close()
        return
    
    cursor.execute("SELECT id, fname, lname FROM customers WHERE lname = ?", (lname,))
    matching_customers = cursor.fetchall()
    
    if matching_customers:
        print("Customers with the same last name found:")
        for customer in matching_customers:
            print(f"ID: {customer[0]}, Name: {customer[1]} {customer[2]}")
        confirm = input("Do you still want to add? (Y/n): ")
        if confirm != "Y":
            print("Customer not added.")
            conn.close()
            return
    
    cursor.execute('''
        INSERT INTO customers (fname, lname, phone, email, address, city, postalcode)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (fname, lname, phone, email, address, city, postalcode))
    
    conn.commit()
    conn.close()
    print("Customer added successfully.")

def search_customer():
    conn = sqlite3.connect("veterinarian.db")
    cursor = conn.cursor()
    
    search_term = input("\nEnter any field value to find customer: ")
    
    cursor.execute('''
        SELECT * FROM customers
        WHERE fname = ? OR lname = ? OR phone = ? OR email = ? OR city = ? OR address = ? OR postalcode = ?
    ''', (search_term,) * 7)
    
    results = cursor.fetchall()
    
    if results:
        print("Matches:")
        for i in results:
            print(i)
    else:
        print("No matches found")
    
    conn.close()

###\
action = input("What do you wanna do? Add customer or search customer? (add/search): ")
if action == "add":
    add_customer()
elif action == "search":
    search_customer()
else:
    print("'add' or 'search' only")
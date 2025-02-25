## SDSS Computing Studies Python Assignment
### Assignment #xx (Total Marks xx)

Objectives:
* Write a query to update information in a table

Data is never static. Data changes. One of the important aspects of a database is the ability to change the contents of it.  For example, your bank keeps a record of how much money you have in your savings and loans accounts. These need to be regularly updated as you add/remove money.  Your Doctor needs to keep track of your contact information and send you emails to your current phone number or email address.  You really don't want those going to the wrong place!

Today we will look at updating the information in a record.


Step 1: Build your Query
Structure:
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
The keyword "update" tells us that we are going to modify the contents of a record or row.
You can choose to update only some pieces of information in a record; you don't have to update all of the information.
You do need to specific which record to update.  This is where having a primary key is really important.

Imagine that there are 2 people with the same name, which is entirely possible. Maybe James Smith occurs in your table twice, but they are 2 different people!  You only want to change the phone number for the James Smith that lives at  12345 Sesame Street, and not the one that lives at 999 Lucky Way.

This is the process you might follow:
1. List all of the James Smith's with their contact information
2. Find the ID (or Customer ID Number) for the correct James Smith and remember it (store it in a variable)
3. Update the phone number where the ID matches the correct James Smith

Example:
Consider the following results when you search for fname='James' and lname='Smith'

table: customers
 id  fname   lname   address                 phone               email
 93  James   Smith   12345 Sesame Street     6048331313          jsmith@gmail.com
104  James   Smith   999 Lucky Way           6049879887          jamess@gmail.com

```
update customers
set phone=6048331212
where id=93
```

Assignment:
Create a database for a veterinarian.  You will need to create your own tables and choose the variable types that best suit these fields/columns.
There will be 3 tables:
customers
    id : primary key integer
    fname: first name 
    lname: last name
    phone: phone number
    email: email address
    address: phyiscal address
    city: city where they live
    postalcode: their postal code


pets
    id: primary key integer
    name: pet name
    type: dog or cat
    breed: description of breed (example German Sheperd, Mixed, Persion)
    birthdate: birthdate of pet (could be used to calculate their age)
    ownerID: to match the ID number in customers ID

visits
    id: primary key integer
    ownerid: the id of the owner who brought in their pet. Matches primary key of owner table
    petid: the id of the pet that was brought in. Matches primary key of pets table
    details: details what the visit was about.  Could be quite lengthy!
    cost: how much was the visit
    paid: how much has been paid so far, used to find outstanding debts


Create a program that allows you to interface with this database. 
We will be doing this in parts over the next few classes.

Part 1.
Create a function that will add a new customer.  
Ask the user for their relevant details and add them to the customers table
Optional enhancements.
Ideas for Check for duplicates:
* Check to see if there is already a username with the same phone number or email before adding and warn that the customer already exists
* List all users with the same last name and ask for confirmation before adding

Create a function that will allow you to search for a customer by any part of their record.
Example: search for all customers with a specific last name
Optional Enhancements.
* search for all users that partially match a specific last name
* search for multiple criteria

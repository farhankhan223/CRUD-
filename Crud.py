import pymysql as p

# Importing pymysql to establish a connection between our SQL database and this Python program.

def getconnect():
    # Function to establish a database connection.
    return p.connect(host="localhost", user="root", password="", database="employee") 

def insertrec(data): 
    # Function to insert records into the database.
    db = getconnect() 
    cr = db.cursor() 
    
    sql = "insert into employee values (%s, %s, %s, %s, %s)"

    cr.execute(sql, data) 
    db.commit()
    db.close()
    print("Data Inserted Successfully...!")

def updaterec(data): 
    # Function to update records in the database.
    db = getconnect()
    cr = db.cursor()
    sql = "update employee set FirstName=%s, LastName=%s, Email=%s, Address=%s where id=%s"
    cr.execute(sql, data)
    db.commit()
    db.close()
    print("Data updated successfully...!")

def deleterec(ids): 
    # Function to delete records from the database.
    db = getconnect()
    cr = db.cursor()
    sql = "delete from employee where id=%s"
    cr.execute(sql, ids)
    db.commit()
    db.close()
    print("Data deleted successfully..!")

def readdata(): 
    # Function to read and display all records from the database.
    db = getconnect()
    cr = db.cursor()
    sql = "select * from employee"
    cr.execute(sql)
    data = cr.fetchall()
    a, b, c, d, e = "id", "FirstName", "LastName", "Email", "Address" 
    print(f"\n\n{a:^5} {b:^15} {c:^15} {d:^20} {e:^30} ") 
    
    for i, fn, ln, e, a in data:
        print(f"{i:^5} {fn:^15} {ln:^15} {e:^20} {a:^30}\n")
    db.commit()
    db.close()

while True: 
    print("\n", " CRUD Database App ".center(40, "-"))
    print("\nUser Wants to - \n 1. Insert Records in Table \n 2. Update a record \n 3. Delete a record  \n 4. Display all records from table")
    n = input("Enter Your Operation: ")

    if(n=="1"):
        # Insert records
        ids = int(input("\nEnter the ID: "))
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        if fname.isalpha() and lname.isalpha():
            pass
        else:
            print("Names can only contain alphabets")
            continue
        email = input("Enter Email: ")
        add = input("Enter address: ")

        data = [ids, fname, lname, email, add]
        insertrec(data)
        continue

    if(n=="2"):
        # Update records
        ids = int(input("\nEnter ID of the record to update: "))
        fname = input("Enter updated First Name: ")
        lname = input("Enter updated Last Name: ")
        if fname.isalpha() and lname.isalpha():
            pass
        else:
            print("Names can only contain alphabets")
            continue
        email = input("Enter updated Email: ")
        add = input("Enter updated address: ")

        data = [fname, lname, email, add, ids]
        updaterec(data)
        continue

    if(n=="3"):
        # Delete records
        ids = int(input("\nEnter ID of the record you want to Delete: "))
        deleterec(ids)
        continue

    if(n=="4"):
        # Read and display all records
        readdata()
        continue

    else: 
        break

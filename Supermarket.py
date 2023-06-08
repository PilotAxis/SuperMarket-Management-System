#Importing Required Modules for the program

from os import system
from datetime import date

#Importing mysql connector

import mysql.connector as connector

#Creating database

def create_database():
    con = connector.connect(host="localhost", user="root", password="ahmed")
    c = con.cursor()
    c.execute("CREATE DATABASE IF NOT EXISTS SUPERMARKET;")
create_database()

#Creating table-1 ITEMS

def create_table1():
    con = connector.connect(host="localhost", user="root", password="ahmed", database="SUPERMARKET")
    c = con.cursor()
    c.execute("CREATE TABLE items(Item_id int(10) PRIMARY KEY, Item_name varchar(100), Price int(10))")
create_table1()

#Creating table-2 STOCK

def create_table2():
    con = connector.connect(host="localhost", user="root", password="ahmed", database="SUPERMARKET")
    c= con.cursor()
    c.execute("CREATE TABLE stock(Item_id int(10) PRIMARY KEY, Item_name varchar(100), Price int(10),Quantity int(10),Total_Price int(10))")
create_table2()

#Creating table-3 TRANSACTION

def create_table3():
    con = connector.connect(host="localhost", user="root", password="ahmed", database="SUPERMARKET")
    c= con.cursor()
    c.execute("CREATE TABLE transaction(Item_id int(10) PRIMARY KEY,Sell_Date Date,Price int(10),Sold_Quantity int(10),Amount_Generated varchar(100))")
create_table3()


#Making Connection

con = connector.connect(host="localhost", user="root", password="ahmed", database="SUPERMARKET")



#  function name    : check_item
#  purpose          : To check if Item with given Id exist or not 
def check_item (Item_id):
    sql = 'select * from items where Item_id=%s'
    data = (Item_id,)
    c = con.cursor(buffered=True)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False



#  function name    : Add_item
#  purpose          : To add item
def Add_item():
    print("{:>60}".format("____Add Item Record____"))
    Id = input("Enter Item Id: ")
    if check_item(Id) == True:
        print("Item Id Already Exists\nTry Again")
        press = input("Press Any key to continue...")
        Add_item()
    Name = input("Enter Item Name: ")
    Price = int(input("Enter Item price: "))
    data1 = (Id, Name, Price)
    msql1= 'insert into items values(%s,%s,%s)' 
    c = con.cursor()
    c.execute(msql1, data1)
    data2 = (Id, Name, Price)
    msql2= 'insert into stock(Item_id,Item_name,Price) values(%s,%s,%s)' 
    c = con.cursor()
    c.execute(msql2, data2)
    data3 = (Id, Price)
    msql3= 'insert into transaction(Item_id,Price)values(%s,%s)' 
    c = con.cursor()
    c.execute(msql3, data3)
    con.commit()
    print("Successfully Added Item Records")
    choice = input("Press Enter to Continue...")
    Item_menu()



#  function name    : Modify_Item
#  purpose          : To modify item records
def Modify_Item():
    print("{:>60}".format("____Modify Item Record____"))
    Id = input("Enter Item Id: ")
    if (check_item(Id) == False):
        print("Item ID Does Not Exists\nTry Again...")
        press = input("Press Any Key to Continue...")
        Item_menu()
    else:
        print("What do you want to Update? ")
        print("1. Name")
        print("2. Price")
        print("3. Go Back To Item Menu")
        ch = int(input("Enter your Update Preference Number from Above (1,2): "))
        if ch == 1:
            Name = input("Enter item Name: ")
            sql1 = 'UPDATE items set Item_name = %s where Item_id = %s'
            data1 = (Name, Id)
            c = con.cursor()
            c.execute(sql1, data1)
            sql2 = 'UPDATE stock set Item_name = %s where Item_id = %s'
            data2 = (Name, Id)
            c = con.cursor()
            c.execute(sql2, data2)
            con.commit()
            print("Updated item Name")
            print("1. Want to Update more Records\n2. Go back to ItemMenu")
            ch = int(input("Press 1 or 2: "))
            if ch == 1:
                Modify_Item()
            else:
                Item_menu()
        elif ch == 2:
            Price = int(input("Enter item price: "))
            sql1 = 'UPDATE items set Price = %s where Item_id = %s'
            data1 = (Price, Id)
            c = con.cursor()
            c.execute(sql1, data1)
            sql2 = 'UPDATE stock set  Price = %s where Item_id = %s'
            data2 = (Price, Id)
            c = con.cursor()
            c.execute(sql2, data2)
            sql3 = 'UPDATE transaction set Price = %s where Item_id = %s'
            data3 = (Price, Id)
            c = con.cursor()
            c.execute(sql3, data3)
            con.commit()
            print("Updated item price")
            print("1. Want to Update more Records\n2. Go back to Item Menu")
            ch= int(input("Press 1 or 2: "))
            if ch == 1:
                Modify_Item()
            else:
                print("{:>60}".format('Going Back To Item Menu'))
                Item_menu()
        elif ch == 3:
            print("{:>60}".format('Going Back To Item Menu'))
            Item_menu()
        else:
           print("Invalid Choice\nTry Again")
           Modify_Item()



#  function name    : Display_Item
#  purpose          : Display Item records of particular item
def Display_Item():
    print("{:>60}".format("____Search Item Record____"))
    Id = input("Enter Item Id: ")
    if (check_item(Id) == False):
        print("Item ID Does Not Exists\nTry Again...")
        press = input("Press Any Key to Continue...")
        Item_menu()
    else:
        sql = 'select * from items where Item_id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("---------------------------------")
            print("Item Id: ", i[0])
            print("Item Name: ", i[1])
            print("Item Price: ", i[2])
            print("----------------------------------")
            print("\n")
        press = input("Press Enter to continue...")
        Item_menu()



#  function name    : List_item()
#  purpose          : Display all Item records
def List_item():
    print("{:>60}".format("____Displaying All Item Records____"))
    sql = 'select * from items'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("----------------------------------")
        print("Item Id: ", i[0])
        print("Item Name: ", i[1])
        print("Item Price: ", i[2])
        print("----------------------------------")
        print("\n")
    press = input("Press Enter to continue...")
    Item_menu()    



#  function name    : Delete_item
#  purpose          : Delete a specified item record
def Delete_item():
    print("{:>60}".format("____Remove Item Record____"))
    Id = input("Enter Item Id: ")
    if (check_item(Id) == False):
        print("Item ID Does Not Exists\nTry Again...")
        press = input("Press Any Key to Continue...")
        Item_menu()
    else:
        sql1 = 'delete from items where Item_id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql1, data)
        sql2 = 'delete from stock where Item_id = %s'
        c = con.cursor()
        c.execute(sql2, data)
        sql3 = 'delete from transaction where Item_id= %s'
        c = con.cursor()
        c.execute(sql3, data)
        con.commit()
        print("Item Record Removed")
        press = input("Press Enter To Continue...")
        Item_menu()



#  function name    : Add_stock
#  purpose          : To add stock
def Add_stock():
    print("{:>60}".format("____Add Stock Record____"))
    Id = input("Enter Item Id: ")
    if check_item(Id) == True:
        print("Item Id Already Exists\nTry Again")
        press = input("Press Any key to continue...")
        Add_stock()
    Name = input("Enter Item Name: ")
    Price = int(input("Enter Item price: "))
    Quantity=int(input("Enter Item Quantity: "))
    Totalp=Price*Quantity
    data1 = (Id, Name, Price,Quantity,Totalp)
    msql1= 'insert into stock values(%s,%s,%s,%s,%s)' 
    c = con.cursor()
    c.execute(msql1, data1)
    data2 = (Id, Name, Price)
    msql2= 'insert into items(Item_id,Item_name,Price) values(%s,%s,%s)' 
    c = con.cursor()
    c.execute(msql2, data2)
    data3 = (Id, Price)
    msql3= 'insert into transaction(Item_id,Price) values(%s,%s)' 
    c = con.cursor()
    c.execute(msql3, data3)
    con.commit()
    print("Successfully Added Stock Records")
    choice = input("Press Any Key to Continue...")
    Stock_menu()



#  function name    : Modify_stock
#  purpose          : To modify Stock records
def Modify_stock():
    print("{:>60}".format("____Modify Stock Record____"))
    Id = input("Enter Item Id: ")
    if (check_item(Id) == False):
        print("Item ID Does Not Exists\nTry Again...")
        press = input("Press Any Key to Continue...")
        Stock_menu()
    else:
        print("What do you want to Update? ")
        print("1. Name")
        print("2. Price")
        print("3. Quantity")
        print("4. Go Back To Stock Menu")
        ch = int(input("Enter your Update Preference Number from Above (1,2,3,): "))
        if ch == 1:
            Name = input("Enter item Name: ")
            sql1 = 'UPDATE stock set Item_name = %s where Item_id = %s'
            data = (Name, Id)
            c = con.cursor()
            c.execute(sql1, data)
            sql2= 'UPDATE items set Item_name = %s where Item_id = %s'
            data = (Name, Id)
            c = con.cursor()
            c.execute(sql2, data)
            con.commit()
            print("Updated item Name")
            print("1. Want to Update more Records\n2. Go back to ItemMenu")
            ch = int(input("Press 1 or 2: "))
            if ch == 1:
                Modify_stock()
            else:
                Stock_menu()
        elif ch == 2:
            Price = int(input("Enter item price: "))
            sql1 = 'UPDATE  stock set Price = %s where Item_id = %s'
            data = (Price, Id)
            c = con.cursor()
            c.execute(sql1, data)
            sql2 = 'UPDATE items set Price = %s where Item_id = %s'
            c = con.cursor()
            c.execute(sql2, data)
            sql3 = 'UPDATE transaction set Price = %s where Item_id = %s'
            c = con.cursor()
            c.execute(sql3, data)
            sql4 = 'UPDATE  stock set Total_Price= Price*Quantity where Item_id = %s'
            data1= (Id,)
            c = con.cursor()
            c.execute(sql4, data1)
            con.commit()
            print("Updated item price")
            print("1. Want to Update more Records\n2. Go back to Menu")
            ch= int(input("Press 1 or 2: "))
            if ch == 1:
                Modify_stock()
            else:
                Stock_menu()
        elif ch == 3:
            Quantity = int(input("Enter item Quantity: "))
            sql = 'UPDATE  stock set Quantity = %s where Item_id = %s'
            data = (Quantity, Id)
            c = con.cursor()
            c.execute(sql, data)
            sql1 = 'UPDATE  stock set Total_Price= Price*Quantity where Item_id = %s'
            data1= (Id,)
            c = con.cursor()
            c.execute(sql1, data1)
            con.commit()
            print("Updated Quantity")
            print("1. Want to Update more Records\n2. Go back to Menu")
            ch= int(input("Press 1 or 2: "))
            if ch == 1:
                Modify_stock()
            else:
                Stock_menu()
        elif ch == 4:
            print("{:>60}".format('Going Back To Stock Menu'))
            Stock_menu()
        else:
            print("Invalid Choice\nTry Again")
            Modify_stock()



#  function name    : Display_stock
#  purpose          : Display Stock records of particular item
def Display_stock():
    print("{:>60}".format("____Search Stock Record____"))
    Id = input("Enter Item Id: ")
    if (check_item(Id) == False):
        print("Item ID Does Not Exists\nTry Again...")
        press = input("Press Any Key to Continue...")
        Stock_menu()
    else:
        sql = 'select * from stock where Item_id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("---------------------------------")
            print("Item Id: ", i[0])
            print("Item Name: ", i[1])
            print("Item Price: ", i[2])
            print("Item Quantity: ", i[3])
            print("Total Price: ", i[4])
            print("----------------------------------")
            print("\n")
        press = input("Press Enter to continue...")
        Stock_menu()



#  function name    : List_stock
#  purpose          : Display all stock records
def List_stock():
    print("{:>60}".format("____Displaying All Stock Records____"))
    sql = 'select * from stock'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("----------------------------------")
        print("Item Id: ", i[0])
        print("Item Name: ", i[1])
        print("Item Price: ", i[2])
        print("Item Quantity: ", i[3])
        print("Total Price: ", i[4])
        print("----------------------------------")
        print("\n")
    press = input("Press Enter to continue...")
    Stock_menu()    



#  function name    : Delete_stock
#  purpose          : Delete a specified stock record
def Delete_stock():
    print("{:>60}".format("____Remove Stock Record____"))
    Id = input("Enter Item Id: ")
    if (check_item(Id) == False):
        print("Item ID Does Not Exists\nTry Again...")
        press = input("Press Any Key to Continue...")
        Stock_menu()
    else:
        sql1 = 'delete from items where Item_id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql1, data)
        sql2 = 'delete from stock where Item_id = %s'
        c = con.cursor()
        c.execute(sql2, data)
        sql3 = 'delete from transaction where Item_id = %s'
        c = con.cursor()
        c.execute(sql3, data)
        con.commit()
        print("Item Record Removed")
        press = input("Press Any key To Continue...")
        Stock_menu()



#  function name    : Add_transaction
#  purpose          : To add Transaction record
def Add_transaction():
    print("{:>60}".format("____Add Transaction Record____"))
    Id = input("Enter Item Id: ")
    if check_item(Id) == True:
        print("Item Id Already Exists\nTry Again")
        press = input("Press Any key to continue...")
        Add_transaction()
    Date=input('Enter sell Date (yyyy-mm-dd) :')
    Price = int(input("Enter Item price: "))
    SoldQuantity=int(input("Enter Sold Quantity: "))
    AmountGen=Price*SoldQuantity
    data1 = (Id, Date, Price,SoldQuantity,AmountGen)
    msql1= 'insert into transaction values(%s,%s,%s,%s,%s)' 
    c = con.cursor()
    c.execute(msql1, data1)
    data2 = (Id, Price)
    msql2= 'insert into stock(Item_id,Price) values(%s,%s)' 
    c = con.cursor()
    c.execute(msql2, data2)
    data3 = (Id, Price)
    msql3= 'insert into items(Item_id,Price) values(%s,%s)' 
    c = con.cursor()
    c.execute(msql3, data3)
    con.commit()
    print("Successfully Added transaction Records")
    choice = input("Press Any Key to Continue...")
    Transaction_menu()



#  function name    : Modify_transaction
#  purpose          : To modify Transaction records
def Modify_transaction():
    print("{:>60}".format("____Modify Transaction Record____"))
    Id = input("Enter Item Id: ")
    if (check_item(Id) == False):
        print("Item ID Does Not Exists\nTry Again...")
        press = input("Press Any Key to Continue...")
        Transaction_menu()
    else:
        print("What do you want to Update? ")
        print("1. Sell Date")
        print("2. Price")
        print("3. Sold Quantity")
        print("4. Go Back To Transaction Menu")
        ch = int(input("Enter your Update Preference Number from Above (1,2,3): "))
        if ch == 1:
            Date=input('Enter sell Date (yyyy-mm-dd) :')
            sql= 'UPDATE transaction set Sell_Date = %s where Item_id = %s'
            data = (Date, Id)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            print("Updated Sell Date")
            print("1. Want to Update more Records\n2. Go back to Transaction Menu")
            ch= int(input("Press 1 or 2: "))
            if ch == 1:
                Modify_transaction()
            else:
                Transaction_menu()
        elif ch == 2:
            Price = int(input("Enter item price: "))
            sql1 = 'UPDATE  transaction set Price = %s where Item_id = %s'
            data = (Price, Id)
            c = con.cursor()
            c.execute(sql1, data)
            sql2 = 'UPDATE stock set Price = %s where Item_id = %s'
            c = con.cursor()
            c.execute(sql2, data)
            sql3 = 'UPDATE items set Price = %s where Item_id = %s'
            c = con.cursor()
            c.execute(sql3, data)
            sql4 = 'UPDATE  transaction set Amount_Generated= Price*Sold_Quantity where Item_id = %s'
            data1= (Id,)
            c = con.cursor()
            c.execute(sql4, data1)
            con.commit()
            print("Updated item price")
            print("1. Want to Update more Records\n2. Go back to Menu")
            ch= int(input("Press 1 or 2: "))
            if ch == 1:
                Modify_transaction()
            else:
                Transaction_menu()
        elif ch == 3:
            Quantity = int(input("Enter sold item Quantity: "))
            sql = 'UPDATE  transaction set Sold_Quantity = %s where Item_id = %s'
            data = (Quantity, Id)
            c = con.cursor()
            c.execute(sql, data)
            sql1 = 'UPDATE  transaction set Amount_Generated= Price*Sold_Quantity where Item_id = %s'
            data1= (Id,)
            c = con.cursor()
            c.execute(sql1, data1)
            con.commit()
            print("Updated Sold Quantity")
            print("1. Want to Update more Records\n2. Go back to Menu")
            ch= int(input("Press 1 or 2: "))
            if ch == 1:
                Modify_transaction()
            else:
                Transaction_menu()
        elif ch == 4:
            print("{:>60}".format('Going Back To Transaction Menu'))
            Transaction_menu()
        else:
            print("Invalid Choice\nTry Again")
            Modify_transaction()



#  function name    : Display_transaction
#  purpose          : Display transaction records of particular item
def Display_transaction():
    print("{:>60}".format("____Search Transaction Record____"))
    Id = input("Enter Item Id: ")
    if (check_item(Id) == False):
        print("Item ID Does Not Exists\nTry Again...")
        press = input("Press Any Key to Continue...")
        Transaction_menu()
    else:
        sql = 'select * from transaction where Item_id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("---------------------------------")
            print("Item Id: ", i[0])
            print("Sell Date: ", i[1])
            print("Item Price: ", i[2])
            print("Sold Quantity : ", i[3])
            print("Amount Generated: ", i[4])
            print("----------------------------------")
            print("\n")
        press = input("Press Any key to continue...")
        Transaction_menu()



#  function name    : List_transaction
#  purpose          : Display all transaction records
def List_transaction():
    print("{:>60}".format("____Displaying All Transaction Records____"))
    sql = 'select * from transaction'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("----------------------------------")
        print("Item Id: ", i[0])
        print("Sell Date: ", i[1])
        print("Item Price: ", i[2])
        print("Sold Quantity : ", i[3])
        print("Amount Generated: ", i[4])
        print("----------------------------------")
        print("\n")
    press = input("Press Any key to continue...")
    Transaction_menu()    



#  function name    : Delete_transaction
#  purpose          : Delete a specified transaction record
def Delete_transaction():
    print("{:>60}".format("____Remove transaction Record____"))
    Id = input("Enter Item Id: ")
    if (check_item(Id) == False):
        print("Item ID Does Not Exists\nTry Again...")
        press = input("Press Any Key to Continue...")
        Transaction_menu()
    else:
        sql1 = 'delete from transaction where Item_id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql1, data)
        sql2 = 'delete from items where Item_id = %s'
        c = con.cursor()
        c.execute(sql2, data)
        sql3 = 'delete from stock where Item_id = %s'
        c = con.cursor()
        c.execute(sql3, data)
        con.commit()
        print("Item Record Removed")
        press = input("Press Any key To Continue...")
        Transaction_menu()



#   function      : Date_wise_sell
#   purpose       : Create a report on date wise sell or sell between two dates
def Date_wise_sell():
    print("{:>60}".format("____Date Wise Sell Record____"))
    start_date = input('Enter start Date (yyyy-mm-dd) :')
    end_date   = input('Enter End Date (yyyy-mm-dd) :')
    sql = 'select * from transaction where Sell_Date between "{}" and "{}"'.format(start_date,end_date)
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("----------------------------------")
        print("Item Id: ", i[0])
        print("Sell Date: ", i[1])
        print("Item Price: ", i[2])
        print("Sold Quantity : ", i[3])
        print("Amount Generated: ", i[4])
        print("----------------------------------")
        print("\n")
    press = input("Press Any key to continue...")
    Transaction_menu()    


#  function name    : Transaction_menu
#  purpose          : Display transaction menu on the screen
def Transaction_menu():
    system("cls")
    print("{:>60}".format(" T R A N S A C T I O N  M E N U "))
    print('-'*120)
    print('1.   Add Transaction')
    print('2.   Modify Transaction')
    print('3.   Display Transaction(particular item)')
    print('4.   List Transactions(all dates)')
    print('5.   Delete Transaction')
    print('6.   Display Sell (Date wise)')
    print('7.   Back to main Menu')
    choice = int(input('\n\nEnter your choice (1..7): '))
    if choice==1:
        Add_transaction()
    elif choice==2:
        Modify_transaction()
    elif choice==3:
        Display_transaction()
    elif choice==4:
        List_transaction()
    elif choice==5:
        Delete_transaction()
    elif choice==6:
        Date_wise_sell()
    elif choice==7:
        main_menu()
    else:
        print("Invalid Choice!")
        press = input("Press Any key to continue...")
        Transaction_menu()



#  function name    : Stock_menu
#  purpose          : Display stock menu on the screen
def Stock_menu():
    system("cls")
    print("{:>60}".format(" S T O C K   M E N U "))
    print('-'*120)
    print('1.   Add Stock ')
    print('2.   Modify Stock')
    print('3.   Display Stock(particular item)')
    print('4.   List Stock(all items)')
    print('5.   Delete stock item')
    print('6.   Back to main Menu')
    choice = int(input('\n\nEnter your choice (1..6): '))
    if choice==1:
        Add_stock()
    elif choice==2:
        Modify_stock()
    elif choice==3:
        Display_stock()
    elif choice==4:
        List_stock()
    elif choice==5:
        Delete_stock()
    elif choice==6:
        main_menu()
    else:
        print("Invalid Choice!")
        press = input("Press Any key to continue...")
        Stock_menu()



#  function name    : Item_menu
#  purpose          : Display item menu on the screen
def Item_menu():
    system("cls")
    print("{:>60}".format(" I T E M   M E N U "))
    print('-'*120)
    print('1.   Add Item ')
    print('2.   Modify Item')
    print('3.   Display Item(particular item)')
    print('4.   List Item (all items)')
    print('5.   Delete Item')
    print('6.   Back to main Menu')
    choice = int(input('\n\nEnter your choice (1..6): '))
    if choice==1:
        Add_item()
    elif choice==2:
        Modify_Item()
    elif choice==3:
        Display_Item()
    elif choice==4:
        List_item()
    elif choice==5:
        Delete_item()
    elif choice==6:
        main_menu()
    else:
        print("Invalid Choice!")
        press = input("Press Any key to continue...")
        Item_menu()


#  function name    : main_menu
#  purpose          : Display main menu on the screen
def main_menu():
    system("cls")
    print("{:>60}".format("-----------------------------------------"))
    print("{:>60}".format("***** SUPERMARKET MANAGEMENT SYSTEM *****"))
    print("{:>60}".format("-----------------------------------------"))
    print('1.   Item Menu')
    print('2.   Stock Menu')
    print('3.   Transaction Menu')
    print('4.   Exit')
    choice = int(input('\n\nEnter your choice {1/2/3/4}: '))
    if choice==1:
        system("cls")
        Item_menu()
    elif choice==2:
        system("cls")
        Stock_menu()
    elif choice==3:
        system("cls")
        Transaction_menu()
    elif choice==4:
        system("cls")
        print("{:>60}".format("Exiting..."))
    else:
        print("Invalid Choice!")
        press = input("Press Any key to continue...")
        main_menu()
           
    
#Calling menu funtion
main_menu()





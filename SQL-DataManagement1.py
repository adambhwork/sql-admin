import time
import pyodbc

print( "**************************************" )
print( "********DATABASE MANAGEMENT**********" )
print( "************by Adam Bhogal*************" )
print( "**************************************" )

options = ["1.Change Customer Name", "2.Show Customer Details - By 'Country'", "3.Show Customer Details - By 'Customer ID'","4.Add Customer Record"]
for i in options:
    print( i )

time.sleep( 1 )


def adminchoice():
    print()
    choice = int( input( "What do you want to do? " ) )
    if choice == 1:
        changename()
    if choice == 2:
        search_country()
    if choice == 3:
        search_id()
    if choice == 4:
        adddata()
   



def changename():
    import pyodbc
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 11 for SQL Server};SERVER=UKL060\SQLEXPRESS;DATABASE=TSQL2012;UID=sa;PWD=Welcome1234' )
    cursor = cnxn.cursor()
    custid = int( input( "CustID: " ) )
    company = input( "Name of Company: " )
    cursor.execute( "UPDATE Sales.Customers set companyname = '{}' WHERE custid='{}'".format( company, custid ) )
    cnxn.commit()
    cursor.close()
    cnxn.close()
    print( "*****Change Successful*****" )


def search_country():
   country=input("Which country customers?")
   cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=UKL060\SQLEXPRESS;DATABASE=TSQL2012;UID=sa;PWD=Welcome1234')
   cursor=cnxn.cursor()
   cursor.execute("SELECT * FROM [TSQL2012].[Sales].[Customers] WHERE country = '{}'".format(country))
   rows=cursor.fetchall()
   for row in rows:
      print('------------------------------------')
      print ("CUSTID:",row[0])
      print  ("COMPANY:",row[1])
      print ("CONTACT:",row[2])
      print ( "JOB TITLE:",row[3])
      print ("CITY:",row[5])
      print('------------------------------------')



def search_id():
   searchref=int(input("What is the Product ID you want?"))
   import pyodbc
   cnxn = pyodbc.connect( 'DRIVER={ODBC Driver 11 for SQL Server};SERVER=UKL060\SQLEXPRESS;DATABASE=TSQL2012;UID=sa;PWD=Welcome1234' )
   cursor=cnxn.cursor()
   cursor.execute( "SELECT * FROM [TSQL2012].[Sales].[Customers] where custid ={}".format( searchref ) )
   rows=cursor.fetchall()
   for row in rows:
      print('------------------------------------')
      print ("CUSTID:",row[0])
      print  ("COMPANY:",row[1])
      print ("CONTACT:",row[2])
      print ( "JOB TITLE:",row[3])
      print ( "ADDRESS:",row[4])
      print ("CITY:",row[5])
      print ( "REGION:",row[6])
      print ( "POSTAL CODE:",row[7])
      print ( "COUNTRY:",row[8])
      print ( "PHONE:",row[9])
      print ( "INFO:",row[10])
      print ( "COMP FINANCE:",row[11])
      print('------------------------------------')


def adddata():
    import pyodbc
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 11 for SQL Server};SERVER=UKL060\SQLEXPRESS;DATABASE=TSQL2012;UID=sa;PWD=Welcome1234' )
    cursor = cnxn.cursor()
    custid=int(input("ID: " ))
    companyname= input( "Name of Customer: " )
    contactname=input("Contact name: ")
    contacttitle=input("Job Title: ")
    city=input("City: ")
    country=input("Country: ")
    cursor.execute('INSERT INTO [TSQL2012].[Sales].[Customers] VALUES (%s,%s, %s,%s,%s, %s)',(custid,companyname,contactname,contacttitle, city,country))
    cnxn.commit()
    print ("Record Added")

adminchoice()



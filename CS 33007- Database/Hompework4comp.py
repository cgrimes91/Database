
#0. import necessary packages
import os
import pymysql
import pandas as pd
import matplotlib.pyplot as plt

#1. Connect to the university database
def MakeConnection(host, port, user, password, database):
	conn=""
	try:
		conn = pymysql.connect(
		host=host,
		port=int(port),
		user=user,
		passwd=password,
		db=database)
		print("Connected to Database Successfully");
	except pymysql.Error as e:
		print("Error %d: %s" % (e.args[0], e.args[1]))
	finally:
		return conn;


#2. Using pymsql and pandas, execute at least two different 'select' queries. To print a dataframe 'df' of pandas, write 'print(df)'
import pymysql as db


HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = ""
DB = "university"

connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
try:
    dbhandler = connection.cursor()
    dbhandler.execute("select * from takes;")
    result = dbhandler.fetchall()
    for row in result:
        for cell in row:
            print (cell, " ",)
        print ("\n")

except Exception as e:
    print (e)


connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
try:
    dbhandler = connection.cursor() 
    dbhandler.execute("select * from student;")
    result = dbhandler.fetchall()
    for row in result:
        for cell in row:
            print (cell, " ",)
        print ("\n")

except Exception as e:
    print (e)

#3. Execute a query that inserts a record in the instructor table.
connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
try:
    dbhandler = connection.cursor()
    dbhandler.execute("insert into instructor values ('35045', 'Gray', 'Music', 45666) ;")
    connection.commit()
except Exception as e:
    print (e)

#4. Execute a query to update the salary by 10% for the instructors of the finance department.
connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
try:
    dbhandler = connection.cursor()
    dbhandler.execute("update instructor set salary= salary* 1.1 where dept_name= 'Finance';")
    connection.commit()
except Exception as e:
    print (e)

#5. call and execute the function you have written in question 1 of this homework. [hint: select the function name with the appropriate parameters.]
connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
try:
    dbhandler = connection.cursor()
    dbhandler.execute("select * from takes where grade_count(105, 'A')>0 ;")

except Exception as e:
    print (e)

#6 Draw a pie chart to show the number of instructors in each department.

intructor_fields = {}
dept_name =[]


intructor_fields["Accounting"]=0;
intructor_fields["Astronomy"]=0;
intructor_fields["Athletics"]=0;
intructor_fields["Biology"]=0;
intructor_fields["Comp. Sci."]=0;
intructor_fields["Cybernetics"]=0;
intructor_fields["Elec. Eng."]=0;
intructor_fields["English"]=0;
intructor_fields["Finance"]=0;
intructor_fields["Geology"]=0;
intructor_fields["Languages"]=0;
intructor_fields["Marketing"]=0;
intructor_fields["Mech. Eng."]=0;
intructor_fields["Music"]=0;
intructor_fields["Physics"]=0;
intructor_fields["Pol. Sci."]=0;
intructor_fields["Psychology"]=0;
intructor_fields["Statistics"]=0;

def classify(val):
   if val == 'Accounting':
      intructor_fields["Accounting"] +=1;
   elif val == 'Astronomy':
      intructor_fields["Astronomy"] +=1;
   elif val == 'Athletics':
      intructor_fields["Athletics"] += 1;
   elif val == 'Biology':
      intructor_fields["Biology"] += 1;
   elif val == 'Comp. Sci.':
      intructor_fields["Comp. Sci."] +=1;
   elif val == 'Cybernetics':
      intructor_fields["Cybernetics"] += 1;
   elif val == 'Elec. Eng.':
      intructor_fields["Elec. Eng."] += 1;
   elif val == 'English':
      intructor_fields["English"] +=1;
   elif val == 'Finance':
      intructor_fields["Finance"] += 1;
   elif val == 'Geology':
      intructor_fields["Geology"] += 1;
   elif val == 'Languages':
      intructor_fields["Languages"] +=1;
   elif val == 'Marketing':
      intructor_fields["Marketing"] += 1;
   elif val == 'Mech. Eng.':
      intructor_fields["Mech. Eng."] += 1;
   elif val == 'Music':
      intructor_fields["Music"] += 1;
   elif val == 'Physics':
      intructor_fields["Physics"] += 1;
   elif val == 'Pol. Sci.':
      intructor_fields["Pol. Sci."] +=1;
   elif val == 'Psychology':
      intructor_fields["Psychology"] += 1;
   elif val == 'Statistics':
      intructor_fields["Statistics"] += 1;

db = pymysql.connect("localhost","root","","university")
cursor = db.cursor()

sql = "SELECT * FROM instructor"

try:

   cursor.execute(sql)

   results = cursor.fetchall()
   num_col = len(results[0])
   for row in results:
        classify(row[2])
        dept_name.append(row[2])
except:
   print ("Error: unable to fecth data")


db.close()

plt.figure()
plt.pie(intructor_fields.values(), labels=intructor_fields.keys())
plt.show()


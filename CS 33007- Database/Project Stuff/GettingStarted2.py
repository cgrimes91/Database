import pymysql

# Open database connection
db = pymysql.connect("localhost","root","root","university" )


# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM instructor"


print ("ID \t\t\t Name \t\t\t Dept_name \t\t\t salary")
#print "ID","Name","Dept_name","salary"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      name = row[1]
      dept_name = row[2]
      salary = row[3]
      # Now print fetched result
      print ("|%s\t\t\t |%s\t\t\t |%s\t\t\t |%d," % \
             (id, name, dept_name, salary ))
except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()

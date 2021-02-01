
###########################################################
# This script is to fetch data from database and display  #
# as graph and pie chart                                  #
###########################################################



import pymysql
import matplotlib.pyplot as plt # you must have matplotlib installed

salary_ranges = {} # python empty dictionary , stores key:value pair
salary =[] # python list

# initialzing the dictionary for 4 classes of salary ranges, salary ranges stored
# as string which is key intial number of instructors in the salary range is 0 are key
salary_ranges["<=60000"]=0;
salary_ranges["60001-70000"]=0;
salary_ranges["70001-80000"]=0;
salary_ranges[">80000"]=0;


def classify(val): # function takes salary value and increments value of the key/salary-range where the salary falls into
   if val<=60000:
      salary_ranges["<=60000"] +=1;
   elif val>60000 and val<=70000:
      salary_ranges["60001-70000"] +=1;
   elif val>70000 and val<=80000:
      salary_ranges["70001-80000"] += 1;
   else:
      salary_ranges[">80000"] += 1;

db = pymysql.connect("localhost","root","root","university" ) # connecting to the database using pymysql interface.
# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM instructor"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   num_col = len(results[0])
   for row in results:
        classify(row[3]) # determining range of the salary
        salary.append(row[3]) # creating the list of all salary from the instructor table
except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()

plt.figure()
plt.pie(salary_ranges.values(), labels=salary_ranges.keys())
plt.show()

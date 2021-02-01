import pymysql;

def modification_query(query, conn, operation_name):
	try:
		cursorObj = conn.cursor();
		cursorObj.execute(query);
		conn.commit();
		print(operation_name+" was successful")
	except pymysql.Error as e:
		print("Error %d: %s" % (e.args[0], e.args[1]))

def insert_records(query,conn):
	modification_query(query, conn,"Insertion");
	
def delete_records(query,conn):
	modification_query(query, conn,"deletion");


def update_records(query,conn):
	modification_query(query, conn,"update");

def createview(query, conn):
	modification_query(query, conn,"creating view");

def createtable(query, conn):
	modification_query(query, conn,"creating table");
def addContraints(query,conn):
	modification_query(query, conn, "Adding contraints");


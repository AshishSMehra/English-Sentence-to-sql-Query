import sqlite3

# Establish a connection to SQLite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record, create table 
cursor=connection.cursor()

## Create the table 
table_info = """
CREATE TABLE STUDENT_INFO(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25));
"""

cursor.execute(table_info)

# Insert Some more records 
cursor.execute('''Insert Into STUDENT_INFO values('Ashish', 'Data Scientist', 'A')''')
cursor.execute('''Insert Into STUDENT_INFO values('Devesh', 'Software Developer', 'A')''')
cursor.execute('''Insert Into STUDENT_INFO values('Tanuja', 'Cyber Security', 'A')''')
cursor.execute('''Insert Into STUDENT_INFO values('Hardeep', 'UX Design', 'A')''')
cursor.execute('''Insert Into STUDENT_INFO values('Rahul', 'Data Analyst', 'A')''')
cursor.execute('''Insert Into STUDENT_INFO values('Pawan', 'Data Scientist', 'A')''')
cursor.execute('''Insert Into STUDENT_INFO values('Neeraj', 'Backend Developer', 'A')''')
cursor.execute('''Insert Into STUDENT_INFO values('Neeraja', 'Data Scientist', 'A')''')


# Display All the records 
print("The Inserted records are")
data=cursor.execute('''Select * from STUDENT_INFO''')
for row in data:
  print(row)

# Commit your changes in the Database 
connection.commit()
connection.close()
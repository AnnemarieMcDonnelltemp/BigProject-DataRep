import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
  database="book"
)

cursor = db.cursor()
sql="insert into book (title,author,price) values (%s,%s,%s)"
values = ('The Dutch House','Ann Patchett',14)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)
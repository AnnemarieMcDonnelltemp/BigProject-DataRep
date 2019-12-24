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
sql="delete from book where id = 7"
values = (1)

cursor.execute(sql, values)

db.commit()
print("delete done")
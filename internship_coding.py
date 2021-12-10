import mysql.connector as con
import sys

try:
    db = con.connect(
      host="localhost",
      user="root",
      passwd=""
    )
    print("Connection Successful.")
except: print("Could not connect! Try again."); sys.exit()

cursor = db.cursor()
database, table = 'mulesoft', 'movies'

try:
    cursor.execute("create database "+database+"")
except: pass
try:
    cursor.execute("CREATE TABLE "+database+"."+table+" ( `id` INT NOT NULL AUTO_INCREMENT ,\
                    `name` VARCHAR(100) NULL , `actor` VARCHAR(100) NULL , `actress` VARCHAR(100) NULL , `release`\
                    VARCHAR(25) NULL , `director` VARCHAR(100) NULL , PRIMARY KEY (`id`))")
except: pass

val1 = ('Bahubali', 'Prabas', 'Anushka Shetty', '2015', 'S. S. Rajamouli')
val2 = ('Dilwale Dulhania Le Jayenge', 'Shah Rukh Khan', 'Kajol', '1995', 'Aditya Chopra')

vals = [val1, val2]
try:
  count = 0
  for _ in range(len(vals)):
    cursor.execute("INSERT INTO "+database+"."+table+"(`name`, `actor`, `actress`, `release`, `director`) VALUES\
                    (%s,%s,%s,%s,%s)", vals[_])
    count+=1
except: print("Couldn't insert data."); sys.exit()
print("Inserted "+str(count)+" items successfully.\n")

cursor.execute("select * from "+database+"."+table+"")
print("Retrieving database:")
for data in cursor:
  print(data)
db.commit()
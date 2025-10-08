import sqlite3 

coon = sqlite3.connect("database.db")

coon.commit()
coon.execute() #записать изменения 
coon.close() #закрывать БД
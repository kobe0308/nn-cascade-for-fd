#data_proce.py
import sqlite3
import param

con = sqlite3.connect(param.aflw_db_path)
cursor = con.cursor()

sqlcomm = 'select FaceImages.filepath from FaceImages'

cursor.execute(sqlcomm)

result = cursor.fetchall()
#print(result)

for ret in result:
	print(ret)




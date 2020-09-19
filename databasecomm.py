import psycopg2
import os
import urllib.parse as up

up.uses_netloc.append("postgres")
url = 'postgres://rciudlch:f1cUXgsORypockj4aiu2o3ZsM2QiUTl4@john.db.elephantsql.com:5432/rciudlch'
conn = psycopg2.connect(url)

cursor = conn.cursor()
msg1 = """INSERT INTO ENTRYUSER (ID,NAME,GENDER,AGE,DISEASE)
                VALUES(2,'UTKARSH','M',19,'HEALTHY');"""
cursor.execute(msg1)
conn.commit()


conn.close()

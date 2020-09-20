import psycopg2
import os
import urllib.parse as up


def databaseadd(name, gender, age, disease):
    print(name, gender, age, disease)
    up.uses_netloc.append("postgres")
    url = "postgres://rciudlch:f1cUXgsORypockj4aiu2o3ZsM2QiUTl4@john.db.elephantsql.com:5432/rciudlch"
    conn = psycopg2.connect(url)
    print("true")
    cursor = conn.cursor()

    msg1 = "INSERT INTO ENTRYUSER (NAME,GENDER,AGE,DISEASE)  VALUES('" + \
        name+"','"+gender+"',"+age+",'"+disease+"');"
    print(msg1)
    cursor.execute(msg1)
    conn.commit()

    conn.close()

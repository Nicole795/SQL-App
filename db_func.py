import mysql.connector

def db ():
    return mysql.connector.connect(
        port="33066", user="root", password="insecure", database="demo"
    )

def update (mydb: object,sql:str):
    cursor = mydb.cursor()
    cursor.execute(sql)
    mydb.commit()

def query(mydb:object,sql:str):
    cursor = mydb.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


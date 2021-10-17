import sqlite3
from sqlite3 import Error

def conectar():
    dbname= 'mydatabase.db'
    conn= sqlite3.connect(dbname)
    return conn

def getUsers():
    conn= conectar()
    cursor= conn.execute("select * from usuuser;")
    resultados= list(cursor.fetchall())
    conn.close()
    return resultados

def addUser(user, pwd, pwdh):
    try :
        conn=conectar()
        conn.execute("insert into Producto (useruser, pwduser, pwdhashuser values(?,?,?);", (user, pwd, pwdh))
        conn.commit()
        conn.close()
        return True
    except Error as error:
        print(error)
        return False

def getUser(user):
    try : 
        conn= conectar()
        SQLstmt="select * from usuuser where useruser=?;"
        cursor= conn.execute(SQLstmt,  (user,))
        resultado= cursor.fetchone()
        return resultado
    except Error as error:
        return error

if __name__=='__main__':
    valor= getUser('wbarrios')
    print(valor)



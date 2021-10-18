from flask import Flask, request, render_template, jsonify, make_response, session
from forms import FormaLogin
import os
import db

app= Flask(__name__)
app.secret_key= os.urandom(32)

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        usu= session['username']
        clave= session['password']
        opcion= session['opcion']
        print("Acceso anterior con Username: "+ usu +" ingresado con clave "+clave + " en el programa " + opcion)
    formaL= FormaLogin()
    return render_template('login.html', form=formaL)

@app.route('/login', methods=('GET','POST'))
def login():
    formaL= FormaLogin()
    if request.method=='POST':
        usu= formaL.username.data
        pwd= formaL.password.data
        session.clear()
        session['username']= usu
        session['password']= pwd
        session['opcion']= 'Menu Login 001'
        resultSet= db.getUser(usu)
        if resultSet==None:
           return jsonify({"mensaje":"Usuario no Existe"}) 
        else : 
            u0= resultSet[0]
            u1= resultSet[1]
            if (usu==u0 and pwd==u1):
            # Creacion de una cookie
                cookieUser= make_response(render_template("ingreso.html", user= usu))
                cookieUser.set_cookie('_user', usu)
                return cookieUser
            else :
                return jsonify({"mensaje":"Usuario con Password Errado"})
    else :
        return render_template("login.html", form=formaL)

@app.route('/cookie')
def obtenerCookie():
    valor= request.cookies.get('_user')
    return "<h2>La Cookie almacenada Administrador es "+valor+"</h2>"

# Main program
if __name__=="__main__":
    app.run(debug=True)
    
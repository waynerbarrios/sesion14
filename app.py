from flask import Flask, request, render_template, jsonify, make_response, session
from forms import FormaLogin
import os
import utils
import config
from flask_sqlalchemy import SQLAlchemy
from models import *

app= Flask(__name__)
app.config.from_object(config)
app.secret_key= os.urandom(32)
db = SQLAlchemy(app)

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
        objUser = db.session.query(usuuser).filter_by(useruser=usu).first()
        if objUser!=None:
            session.clear()
            session['username']= usu
            session['password']= pwd
            session['opcion']= 'Menu Login 001'
            if usu==objUser.useruser and pwd==objUser.pwduser:
                # Creacion de una cookie
                cookieUser= make_response(render_template("ingreso.html", user= usu))
                cookieUser.set_cookie('Administrador', usu)
                return cookieUser
            else :
                return jsonify({"mensaje":"Acceso negado!  Clave Incorrecta!"})
        else : 
            return jsonify({"mensaje":"Usuario no se encuentra en la BDD"})
    else :
        return render_template("login.html", form=formaL)

@app.route('/cookie')
def obtenerCookie():
    valor= request.cookies.get('Administrador')
    return "<h2>La Cookie almacenada Administrador es "+valor+"</h2>"

@app.route('/add')
def callAddUser():
    formaU= FormaLogin()
    return render_template("addLogin.html", form=formaU)

@app.route('/addUser', methods=('GET', 'POST'))
def createUser():
    formaU=FormaLogin()
    if request.method=='POST':
        u0= formaU.username.data
        u1= formaU.password.data
        u2= utils.hash_pwd(u1)
        usuario= usuuser(u0, u1, u2)
        db.session.add(usuario)
        db.session.commit()
        return "<h1>Registro creado sin errores!</h1>"
    else : 
        return render_template("addLogin.html", form=formaU)

if __name__=="__main__":
    app.run(debug=True)
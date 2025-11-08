from flask import Flask, render_template, request, redirect, session
from datetime import *
from cargarDatos import guardar_usuario, obtener_usuarios

app = Flask("app.py")
app.secret_key = "K5XEUwU"      

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.html")
@app.route("/registrar")
def registro():
    return render_template("registro.html")

@app.route("/registro" , methods = ["POST"])
def registrar():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    if name and email and password:
        print("Usuario registrado con éxito!")
        #Poner lógica para guardar en DB.
        guardar_usuario(name, email, password)
        return redirect("/login")
    else:
        return "Error: Faltan datos en el formulario", 400

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logged", methods = ['POST'])
def logged():
    name = request.form.get("name")
    password = request.form.get("password")
    #Obtener datos y comparar para dar acceso.    
    if name and password:
        users_in_db = obtener_usuarios()
        for i in users_in_db:
            if name == i['nombre']:
                if password == i['password']:
                    session['user_name'] = i['nombre']
                    session['user_email'] = i['email']
                    return redirect("/dashboard")
                else:
                    return "ERROR, contraseña incorrecta"
        return "ERROR, usuario no válido."
    else:
        return "ERROR, datos incompletos o vacíos."

@app.route("/dashboard")
def dashboard():
    if 'user_name' in session:
        return render_template("dashboard.html", username = session['user_name'], email = session['user_email'])
    else:
        return redirect("/login")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

app.run(host='0.0.0.0', port=5000, debug=False)
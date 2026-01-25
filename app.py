from flask import Flask, render_template, request
import math
import forms
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key = 'clave_secreta'
csrf = CSRFProtect()

@app.route('/')
def index():
    title = "IDGS804 -Intro Flask"
    listado =['Juan', 'Ana', 'Pedro', 'Luisa']
    return render_template('index.html', title=title, listado=listado)

@app.route('/saludo1')
def saludo1():
    return render_template("saludo1.html")


@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    distancia = None

    if request.method == 'POST':
        x1 = float(request.form['x1'])
        y1 = float(request.form['y1'])
        x2 = float(request.form['x2'])
        y2 = float(request.form['y2'])
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return render_template("distancia.html", distancia=distancia)

@app.route('/saludo2')
def saludo2():
    return render_template("saludo2.html")

@app.route("/hola")
def func():
    return "Hola, mundoooo - Hola"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>Numero: {n}</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>Hola, {username}! Tu Id es:{id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma es: {n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:parm>")
def func2(parm="Juan"):
    return f"<h1>Hola,{parm}</h1>"

@app.route("/operas")
def operas():
    return '''
    <form method="post">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required>
        <br><br>

        <label for="apellido">Apellido paterno:</label>
        <input type="text" id="apellido" name="apellido" required>
        <br><br>

        <input type="submit" value="Enviar">
    </form>
    '''
@app.route("/OperasBas")
def OperasBas():
    return render_template("operasBas.html")


@app.route("/operasBas", methods=['GET', 'POST'])
def operasbas():
        res = None
        if request.method == 'POST':           
          n1=request.form.get('num1')
          n2=request.form.get('num2')

          if request.form.get('operacion') =='suma':
              res=float(n1)+float(n2)
              
          if request.form.get('operacion') =='resta':
              res=float(n1)-float(n2)
              
          if request.form.get('operacion') =='multiplicar':
              res=float(n1)* float(n2)
              
        if request.form.get('operacion') =='dividir':
              res=float(n1)/ float(n2)
              

        return render_template('operasBas.html',res=res,)


@app.route("/resultado", methods=['GET', 'POST'])
def result1():
    n1=request.form.get('num1')
    n2=request.form.get('num2')
    return f"<h1>La suma es: {float(n1)+float(n2)}</h1>"

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    mat=0
    nom=''
    ape=''
    email=''
    alumno_clas=forms.UserForm(request.form)
    if request.method=='POST':
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data
    return render_template("alumnos.html",
    form=alumno_clas,
    mat=mat,
    nom=nom,
    ape=ape,
    email=email)
    
if __name__ == '__main__':
    app.run(debug=True)


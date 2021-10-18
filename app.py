from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import FlaskForm

app= Flask(__name__,template_folder='template')

@app.route('/')
def model():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    camara = request.form.get('cap')
    encendido= request.form.get('enc')
    apagado= request.form.get('apg')
    print(camara)
    #return render_template('index.html')
    return camara,encendido,apagado

app.run(debug=True)
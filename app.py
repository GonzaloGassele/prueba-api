from flask import Flask
from flask import render_template
from flask import request
from run import system
from model import detect

app= Flask(__name__,template_folder='template')

@app.route('/')
def model():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def api():
    camara = request.form.get('cap')
    encendido= request.form.get('enc')
    apagado= request.form.get('apg')
    detect(camara)
    return render_template('index.html')


app.run(debug=True)
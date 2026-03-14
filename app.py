from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    nome = "Kim"
    dados = {"profissão": "Operador CNC", "empresa": "Zini"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == "__main__":
    app.run()
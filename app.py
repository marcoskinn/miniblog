from flask import Flask
from flask import render_template, request, flash, redirect

#https://miniblog-livid-nine.vercel.app/

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha-palavra-secreta"

@app.route("/")
@app.route('/index')
def index():
    nome = "Kim"
    dados = {"profissão": "Operador CNC", "empresa": "Zini"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autentificar', methods=['POST'])
def autentificar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario == 'admin' and senha == 'senha123':
        return f"usuario: {usuario} e senha: {senha}"
    else:
        flash("Dados inválidos")
        flash("Usuário ou senha inválidos")
        return redirect('/login')

if __name__ == "__main__":
    app.run()
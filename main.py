from flask import Flask, render_template, request, session, url_for, redirect
from random import randint

app = Flask(__name__)
app.secret_key = 'chave_secreta'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['nome'] = request.form.get('nomeForm')
        return redirect(url_for('jogo'))
    return render_template('index.html')

@app.route('/jogo', methods=['GET', 'POST'])
def jogo():
    nome = session.get('nome')
    if "numero_secreto" not in session:
        session["numero_secreto"] = randint(1, 100)
        session["tentativas"] = 0
    
    mensagem = ""
    if request.method == "POST":
        palpite = int(request.form["palpite"])
        session["tentativas"] += 1
        if palpite == session["numero_secreto"]:
            mensagem = f"PARABÉNS! Você acertou em {session['tentativas']} tentativas!"
            session.clear()
        elif palpite < session["numero_secreto"]:
            mensagem = "O número é maior"
        else:
            mensagem = "O número é menor"

    return render_template('jogo.html', mensagem=mensagem, nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
# coding: utf-8
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask("projeto")
# criando uma chave de criptografia
app.secret_key = '*WY#E@HDHWAKDJ213231Shdjahda8w342'


# rota raiz
@app.route("/")
def ola_mundo():
    #criar uma variável com o meu nome
    nome="Gabriel Marchione"
    produtos = [
    {"nome": "Ração", "preco": 199.99},
    {"nome": "Playstation", "preco": 1999.99}]
    return render_template("alo.html", n=nome, aProdutos=produtos), 200


# rota teste
@app.route("/teste")
@app.route("/teste/<variavel>")
def funcao_teste(variavel = ""):
    return "nova rota teste<br>Variável : {}".format(variavel), 200


# rota formulario
@app.route("/form")
def form():
    return render_template("form.html"), 200


# rota tratamento do formulario
@app.route("/form_recebe", methods=["GET", "POST"])
def form_recebe():
    nome = ""
    if request.method == "POST":
        nome = request.form["nome"]
        return "Nome: {}".format(nome), 200
    else:
        return "Não pode chamar direto no GET", 200


# rota form de login
@app.route("/login")
def login():
    return render_template("login.html"), 200


# rota para validar o formulario
@app.route("/login_validar", methods=["POST"])
def login_validar():
    if request.form["usuario"] == "poyatos" and request.form["senha"] == "12345":
        session["usuario"] = request.form["usuario"]
        session["codigo"] = 1
    else:
        return "Usuário/senha inválidos, digite novamente.", 200

app.run()
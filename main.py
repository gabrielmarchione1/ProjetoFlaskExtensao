# coding: utf-8
from flask import Flask, render_template

app = Flask("projeto")

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

app.run()
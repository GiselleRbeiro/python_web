from flask import Flask, render_template

app = Flask("Meu app")

posts = [
    {
        "titulo": "Minha primeira postagem",
        "texto": "teste"
        },
    {
        "titulo": "segundo post",
        "texto": "outro teste"
        },
]
@app.route("/")
def exibir_entradas():
    entradas = posts 
    return render_template("exibir_entradas.html", entrada=entradas)
from flask import Flask , render_template
from random import randint

app = Flask (__name__)

@app.route("/")
def route():
    numero = randint(1 , 3)
    humor = " "
    imagem = " "
    if numero == 1:
        humor = "Doido"
        imagem = "/static/doido.png"
    else:
        humor = "Serio"
        imagem = "/static/serio.png"

    return render_template('index.html' , humor = humor , imagem = imagem)

if (__name__ == "__main__"):
    app.run(debug= True)



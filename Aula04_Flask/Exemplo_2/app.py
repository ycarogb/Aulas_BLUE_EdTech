from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def route():
    nome = "Marcio"
    idade = 15
    if idade >= 18:
        maiorDeIdade = True
    else:
        maiorDeIdade = False
    cidade = "São Paulo"
    imagem = "https://file5s.ratemyserver.net/mobs/1251.gif"
    return render_template('index.html' , nome = nome , idade = idade , cidade = cidade , imagem = imagem , maiorDeIdade = maiorDeIdade)

if (__name__ == "__main__"):
    app.run (debug= True)

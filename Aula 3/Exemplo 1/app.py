from flask import Flask

app = Flask(__name__) #define um objeto "Flask", nesse caso, é o app

@app.route("/")
def hello_world():
    return "<h1> E vamos de Flask! </h1> <br> <h3>Primeira aplicação usando Flask</h3><br><h3>consegui atualizar automaticamente</h3>"

@app.route("/rota2/")
def rota2():
    return "<h1> página 2 </h1>"


if (__name__ == "__main__"):
    app.run(debug = True)

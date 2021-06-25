from flask import Flask
from bp import bp #importa as funções das rotas


app = Flask(__name__)
app.register_blueprint(bp)

if (__name__ == "__main__"):
    app.run (debug = True)


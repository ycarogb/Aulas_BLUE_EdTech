from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)



#Configurações de acesso ao banco de dados
#incluir dados do Elephant ou de qualqer outra plataforma, inclusive da rede local

user = "loxpgvhr"
password = "EnFxvtYDVT_nIrSsSqwG8EUpgXtTWWGy"
host = "tuffi.db.elephantsql.com"
database = "loxpgvhr"

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "chavesecreta"

#criando um elemento da classe SQLAlchemy
db = SQLAlchemy(app) 

#Modelar a Classe Filmes - > tabela filmes
#db.Model -> Avisa ao flask que é um modelo de tabelas

#Esta função faz é o mesmo deste comando no SQL - 'SELECT * FROM filmes ORDER BY id ASC'
#query = SELECT

class Filmes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, imagem_url):
        self.nome = nome
        self.imagem_url = imagem_url
    
    @staticmethod
    def read_all():
        # SELECT * FROM filmes ORDER BY id ASC
        return Filmes.query.order_by(Filmes.id.asc()).all()

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/read")
def read():
    # Chamada do método read_all da classe Filmes, que representa a tabela filmes do banco de dados.
    registros = Filmes.read_all()
    return render_template("read_all.html", registros=registros)

@app.route("/read/<id_registro>")
def read_movie(id_registro):
    return "Em construção - Visualizar registro de ID "+id_registro

@app.route("/create")
def read_id():
    return "Em construção: pagina CREATE ainda vai ser construída"

if (__name__ == "__main__"):
   app.run(debug = True)
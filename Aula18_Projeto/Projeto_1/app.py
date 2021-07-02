#importanto o Flask - miniframework que conecta o back e front
#render_template - carrega página para determinada rota incluída no flask
#request - conecta o flask com o banco de dados
#SQLAlchemy - linguagem usada para acessar e manipular BD... equivalente ao SQL

from flask import Flask, render_template, request
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

class Series (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, imagem_url):
        self.nome = nome
        self.imagem_url = imagem_url
    
    @staticmethod
    def read_series():
        return Series.query.order_by(Series.id.asc()).all()
    
    @staticmethod
    def series_single(registro_id):
        return Series.query.get(registro_id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()


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
    
    @staticmethod
    def read_single(registro_id):
        #SELECT * FROM filmes WHERE id = x
        #O get faz o papel do WHERE no SQL
        return Filmes.query.get(registro_id)

    def save(self): #salva as informações no banco de dados
        db.session.add(self) #Equivale ao INSERT VALUE
        db.session.commit()

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/filmes")
def read():
    # Chamada do método read_all da classe Filmes, que representa a tabela filmes do banco de dados.
    registros = Filmes.read_all()
    return render_template("filmes.html", registros=registros)

@app.route("/filmes/<id_registro>")
def read_id(id_registro):
    registro = Filmes.read_single(id_registro)
    return render_template("read_single.html", registro=registro) 

@app.route("/series")
def read_ser():
    # Chamada do método read_all da classe Filmes, que representa a tabela filmes do banco de dados.
    registros = Series.read_series()
    return render_template("series.html", registros=registros)

@app.route("/series/<id_registro>")
def serie_singl(id_registro):
    registro = Series.series_single(id_registro)
    return render_template("read_single.html", registro=registro) 

@app.route("/create" , methods = ('GET', 'POST'))
def create():
    novo_id = None
    serie = " "

    if request.method == 'POST':
        form = request.form
        if form['conteudo'] == 'f':
            registro = Filmes(form['nome'], form['imagem_url'])
            registro.save()
            serie = False
        else:
            registro = Series(form['nome'], form['imagem_url'])
            registro.save()
            serie = True

        novo_id = registro.id
        

    return render_template("create.html", novo_id = novo_id, serie = serie)
if (__name__ == "__main__"):
   app.run(debug = True)
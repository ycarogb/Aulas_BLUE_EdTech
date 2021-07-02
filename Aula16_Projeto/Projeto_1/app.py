from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

registros =[
    {
        "id": 1,
        "nome": "A procura da felicidade",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/pt/thumb/1/1e/The_Pursuit_of_Happyness.jpg/200px-The_Pursuit_of_Happyness.jpg"
    },
     {
        "id": 2,
        "nome": "Laranja Mecânica",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/pt/thumb/1/1e/The_Pursuit_of_Happyness.jpg/200px-The_Pursuit_of_Happyness.jpg"
    }
]

@app.route("/read")
def read_all():
    return render_template("read_all.html", registros = registros)

@app.route("/read/<id_registro>")
def read_id():
    return "Em construção: Visualizar registro de ID2"

if (__name__ == "__main__"):
   app.run(debug = True)
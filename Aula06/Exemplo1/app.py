from flask import Flask, render_template , request

app = Flask (__name__)

@app.route("/" , methods = ('GET' , 'POST'))
def index():
    nome = None
    sobrenome = None
    criatura = None
    imagem = None

    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']    
        criatura = request.form ['criatura']
    
    if criatura == "elfo":
        imagem = "https://i.pinimg.com/originals/80/de/b7/80deb7020d47ef025e88997a815b5558.jpg" #imagem de elfo
    elif criatura == "orc":
        imagem = "https://w7.pngwing.com/pngs/513/1010/png-transparent-azog-orc-goblin-drawing-orc-superhero-fictional-character-religion.png" #imagem orc
    elif criatura == "hobbit":
        imagem = "https://w7.pngwing.com/pngs/558/939/png-transparent-brave-frontier-bilbo-baggins-the-hobbit-fan-art-bilbo-baggins-vertebrate-fictional-character-cartoon.png" #imagem hobbit 


    return render_template ("index.html" , nome=nome , sobrenome=sobrenome , criatura=criatura , imagem=imagem)


if (__name__ == "__main__"):
    app.run(debug = True)



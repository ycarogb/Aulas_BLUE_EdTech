from flask import Blueprint , render_template #A função Blueprint permite que a aplicaçao principal pegue funções definidas para as rotas em um outro arquivo


bp = Blueprint( 'bp' , __name__)

@bp.route("/")
def home():
    return "<h1>Hello, Flask</h1>"

@bp.route("/login/<nome>")
def nome(nome = None):
    return "<h1>Olá " +nome+ "! <br /> Faça seu login!<h1>"

@bp.route("/auladeflexbox/")
def carrega():
    return render_template("Refazendo_Exercicio_com_FlexBox.html")

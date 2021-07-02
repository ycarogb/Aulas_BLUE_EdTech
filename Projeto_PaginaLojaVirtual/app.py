from flask import (
    Blueprint, render_template , request , Flask
)

app = Flask(__name__)

bp = Blueprint('app,', __name__)

@bp.route("/" , methods=('GET' , 'POST'))
def index():
    produtos = [
        {
            'numero': '001',
            'imagem' : 'https://s2.glbimg.com/5NF1Oh81wwlNRLWsqAOq88r8HSE=/0x0:1920x1080/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2019/b/5/Hdek9pQuCJSyJWd99f6g/lenovo.png',
            'nome' : 'Lenovo Ideapad 330',
            'marca' : 'Lenovo',
            'disponivel' : True,
            'processador' : 'Core i5 8250U',
            'hd' : '1TB',
            'ram' : '8GB',
            'preço' : 'R$2450',
        },
        {
            'numero': '002',
            'imagem' : 'https://s2.glbimg.com/GdoN3Z4KhrGB6-zV7bc3C1MMrX4=/0x0:1600x900/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2020/x/a/XHjgdjQ7m116P7YmZtvQ/dell.png',
            'nome' : 'Dell Inspiron 15 3000',
            'marca' : 'Dell',
            'disponivel' : True,
            'processador' : 'Core i5 duall core',
            'hd' : '1TB',
            'ram' : '4GB',
            'preço' : 'R$2300',
        },
        {
            'numero': '003',
            'imagem' : 'https://s2.glbimg.com/puEDK-mjtpuhSuDWaidzlAUf-aI=/0x0:1280x720/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2019/I/E/DhJ1wxShmfP8uI3GGs7Q/x30.png',
            'nome' : 'Samsung Expert X30',
            'marca' : 'Samsung',
            'disponivel' : True,
            'processador' : 'Core i5 8250U',
            'hd' : '1TB',
            'ram' : '8GB',
            'preço' : 'R$2600',
        },
        {
            'numero': '004',
            'imagem' : 'https://s2.glbimg.com/fr9onlccq2aGZo9vfNDJgDzi8Ys=/0x0:1600x900/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2020/r/7/08gAwaQLG0T1ro7qoWgg/aspire3.png',
            'nome' : 'Acer Aspire 3',
            'marca' : 'Acer',
            'disponivel' : True,
            'processador' : 'Core i5 10210U',
            'hd' : '254GB',
            'ram' : '4GB',
            'preço' : 'R$2800',
        },
        {
            'numero': '005',
            'imagem' : 'https://s2.glbimg.com/_gMhQLLedBzSK5dPxO7LNdIqYg0=/0x0:695x390/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2019/e/J/wfQdlMT5e98s1J6tIIsw/notebook-acer-aspire-5-a515-52g-79h1-intel-r-core-tm-i7-8565u-8ageracao-memoria-ram-de-8-gb-ssd-de-128-gb-hd-de-1-tb-nvidia-r-geforce-r-mx130-com-2gb-gddr5-vram-dedicada-tela-de-15-6-hd-windows-10.jpg',
            'nome' : 'Acer Aspire 5',
            'marca' : 'Acer',
            'disponivel' : True,
            'processador' : 'Core i5 8265U',
            'hd' : '1TB',
            'ram' : '4GB',
            'preço' : 'R$2895',
        },
        {
            'numero': '006',
            'imagem' : 'https://s2.glbimg.com/O4zZlFfbbRMHyFz5r-x_1iA-_sE=/0x0:1920x1080/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2020/N/o/bdpsFETd284mCz0q0I6g/ideapad.png',
            'nome' : 'Lenovo Ideapad S145',
            'marca' : 'Lenovo',
            'disponivel' : True,
            'processador' : 'Core i5 8265U',
            'hd' : '1TB',
            'ram' : '4GB',
            'preço' : 'R$2960',
        },

    ]

    caminho_base_imagem = ' C:\Projetos BLUE\M2_Web, Cloud e Database\Projeto_PaginaLojaVirtual\static'

    if request.method == "POST":
        num_produto = request.form['nr_produto']
        selecionado = True
        num_produto_int = int(num_produto)
    else:
        selecionado = False
        num_produto = '000'
        num_produto_int = 0

    
    return render_template(
        'index.html',
        produtos=produtos,
        selecionado=selecionado,
        num_produto=num_produto,
        num_produto_int=num_produto_int
   )
   

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)
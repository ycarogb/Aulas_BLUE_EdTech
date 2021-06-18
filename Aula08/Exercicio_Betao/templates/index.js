//Definir os dados iniciais

const pessoa = {
    nome : "Betão" ,
    sobrenome: "Einstein" ,
    idade: 42 ,

    doido: false ,
    imagem_doido: 'https://www.hypeness.com.br/1/2017/08/EinsteinL3.jpg',
    imagem_serio: 'https://upload.wikimedia.org/wikipedia/commons/5/50/Albert_Einstein_%28Nobel%29.png',

}

const nome = document.getElementById("nome");
const sobrenome = document.getElementById("sobrenome");
const idade = document.getElementById("idade");
const botao = document.getElementById("alterarHumor");

nome.innerText = pessoa.nome;
sobrenome.innerText = pessoa.sobrenome;
idade.innerText = pessoa.idade;

function atualizaHumor() {
    pessoa.doido = !pessoa.doido;
    const imagem = document.getElementById("imagem");
    const humor = document.getElementById("bloco_humor");

    if(pessoa.doido){ 
        imagem.src = pessoa.imagem_doido;
        humor.innetHTML = pessoa.nome + ' tá <b>DOIDO</b>!';
    }
    else {
        imagem.src = pessoa.imagem_serio;
        humor.innerHTML = pessoa.nome + ' tá <b>SERIO</b>!';
    }
}

atualizaHumor();
botao.addEventListener('click' , atualizaHumor);

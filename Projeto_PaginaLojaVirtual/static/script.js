const cardProdutos = document.querySelectorAll('.card_produto');
const input = document.getElementById('nr_produto');

let produtoSelecionado;

for (const cardProduto of cardProdutos) {
    cardProduto.addEventListener('click', function () {
        // Procura por cards que já estão selecionados
        const cardsSelecionados = document.querySelectorAll('.card_produto.selecionado');
		

        // Caso tenha um ou mais cards, remove as classes de selecionado deles.
        if (cardsSelecionados.length > 0) {
            for (const cardSelecionado of cardsSelecionados) {
                cardSelecionado.classList.remove('selecionado');
            }
        }

        if (!this.classList.contains('selecionado')) {
			this.classList.add('selecionado');
			
            // Coloca o card que foi clicado na variável 'produtoSelecionado'
            produtoSelecionado = this;
			const nrProduto = produtoSelecionado.getAttribute('data-numero');
			nr_produto.value = nrProduto;
        } else {
            this.classList.remove('selecionado');
        }
    })
}

const botaoEscolher = document.getElementById('botao_escolher');
const blocoProdutoSelecionado = document.getElementById('selecionado');
botaoEscolher.addEventListener('click', function () {
    if (produtoSelecionado) {
        const nomeProduto = produtoSelecionado.getAttribute('data-nome');
        blocoProdutoSelecionado.innerHTML = `Produto escolhido: <b>${nomeProduto}</b>`;
		
    } else {
        blocoProdutoSelecionado.innerHTML = `Nenhum prduto foi selecionado`;
    }
});

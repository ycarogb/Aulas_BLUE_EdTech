function iniciar(){
	const personagens= document.querySelectorAll(".card_pokemon");
	const texto = document.querySelector("#texto");
    for (const personagem of personagens){
        personagem.addEventListener("click" , marcarElementoSelecionado);
    }
}

function marcarElementoSelecionado(){
    const nomePokemon = this.getAttribute("data-nome")
    
    if(!this.classList.contains("selecionado")){
        this.classList.add("selecionado");
        texto.innerHTML = `Você selecionou <b>${nomePokemon}</b>`;
    }
    else {
        this.classList.remove("selecionado");
        texto.innerHTML = "Selecione um pokemon"
    }

}
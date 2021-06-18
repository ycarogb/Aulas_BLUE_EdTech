const contador = 0;
const nomePokemon = document.getElementsByClassName("nome_pokemon");
const textoPokemon = document.getElementById("pokemon_selecionado")

function selecionaPokemon(){
    contador += 1
    textoPokemon.innerHTML = "<h3>Você selecionou " + contador + " pokemons!!</h3>"
}
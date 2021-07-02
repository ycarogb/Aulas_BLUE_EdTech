CREATE TABLE usuarios (
	idUsuario SERIAL PRIMARY KEY,
	nomeUsuario VARCHAR NOT NULL
);

CREATE TABLE filmes (
	idFilme SERIAL PRIMARY KEY, 
	nomeFilmes VARCHAR NOT NULL,
	imagemUrl VARCHAR,
	ano INT4,
	orcamento DECIMAL(10,2),
	idUsuario INT NOT NULL REFERENCES usuarios (idUsuario)
);

CREATE TABLE personagens (
	idPersonagem SERIAL PRIMARY KEY,
	nomePersonagem VARCHAR NOT NULL,
	imagemUrl VARCHAR
);

CREATE TABLE filmesPersonagens(
	idFilme INT NOT NULL REFERENCES filmes(idFilme),
	idPersonagem INT NOT NULL REFERENCES personagens(idPersonagem),
	PRIMARY KEY (idFilme, idPersonagem)
);

CREATE TABLE filmes (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	imagem_url VARCHAR(255)
);
 
INSERT INTO filmes (nome, imagem_url)
VALUES ('Cidade de Deus', 'https://upload.wikimedia.org/wikipedia/pt/thumb/1/10/CidadedeDeus.jpg/245px-CidadedeDeus.jpg'),
		('Minha mãe é uma peça', 'https://upload.wikimedia.org/wikipedia/pt/d/da/Minha_M%C3%A3e_%C3%A9_uma_Pe%C3%A7a.jpg'),
		('Que horas ela volta?', 'https://br.web.img3.acsta.net/c_310_420/pictures/16/01/21/17/52/543806.jpg');
		
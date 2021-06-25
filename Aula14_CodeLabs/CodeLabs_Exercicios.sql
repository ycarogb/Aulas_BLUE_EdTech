--Listar o nome, sobrenome e email de todos os funcionários
SELECT nome, sobrenome, email FROM funcionarios f 

--Listar o nome, sobrenome e email de todos os funcionários que são representantes de vendas
SELECT nome, sobrenome, email, cargo FROM funcionarios f 
WHERE cargo = 'Sales Rep'

--Listar todos os cargos (sem repetir)
SELECT DISTINCT cargo FROM funcionarios f 

--Listar todas as cidades (sem repetir) em que a empresa possui lojas
SELECT DISTINCT cidade FROM lojas l 

--Listar o nome, sobrenome e email , cidade, país e telefone da loja do presidente da empresa
SELECT f.nome, f.sobrenome, f.email, f.cargo, l.cidade, l.pais, l.telefone
FROM funcionarios f JOIN lojas l 
ON f.codloja = l.codloja 
WHERE cargo LIKE 'President';

--Listar o produto com o maior preço
SELECT nomeproduto, precosugerido FROM produtos p 
ORDER BY precocompra DESC LIMIT 1;

SELECT MAX(precoCompra), a.nomeproduto
FROM produtos a
GROUP BY a.nomeproduto 
ORDER BY a.precocompra;


SELECT MAX(precocompra), nomeproduto FROM produtos p
GROUP BY p.nomeproduto LIMIT 1;

--Listar o produto com o menor preço
SELECT nomeproduto, precosugerido FROM produtos p 
ORDER BY precocompra ASC LIMIT 1; 

SELECT MIN(precosugerido), nomeproduto FROM produtos;

--Listar o produto com menor quantidade em estoque
SELECT nomeproduto, qtdestoque FROM produtos p 
ORDER BY qtdestoque ASC LIMIT 1;


SELECT p.nomeProduto FROM produtos p 
WHERE p.qtdestoque = (SELECT MAX(qtdestoque) FROM produtos);

--Listar o produto com maior quantidade em estoque
SELECT nomeproduto, qtdestoque FROM produtos p 
ORDER BY qtdestoque DESC LIMIT 1;

--Listar produto e quantidade de vendas daquele produto
SELECT * FROM detalhespedidos d2 

SELECT p.nomeproduto, SUM(d.quantidaDEpedida) --a função SUM soma os valores de determinada coluna
FROM produtos p JOIN detalhespedidos d 
ON p.codproduto = d.codproduto 
GROUP BY p.nomeproduto; -- O GROUP BY reúne as outras colunas em que a soma ou outro comando esteja relacionado

---####DESAFIOS###
--Listar os clientes com maior quantidade de vendas. Exibir: Nome, Sobrenome, Cidade e Estado do Cliente e a quantidade de vendas dele
SELECT  c.nomecliente AS "Nome", 
		c.sobrenomecontato AS "Sobrenome", 
		c.cidade AS "Cidade",
		c.estado AS "Estado",
		COUNT(p.numpedido) AS "qtd Vendas"
FROM clientes c JOIN pedidos p 
ON c.numcliente = p.numcliente 
GROUP BY c.nomecliente, c.sobrenomecontato, c.estado, c.cidade 
ORDER BY COUNT(p.numpedido) DESC LIMIT 10;

-- Listar os produtos com maior quantidade de vendas. Exibir: Nome doProduto, Descrição da Linha do Produto, Preço do Produto e Quantidade de Vendas


SELECT  p.nomeproduto AS "Produto" , 
		p.descricaoproduto AS "Descrição", 
		p.precosugerido AS "Preço",
		SUM(d.quantidadepedida) AS "Qtd Vendas" 
FROM produtos p JOIN detalhespedidos d 
ON p.codproduto = d.codproduto
GROUP BY p.nomeproduto , p.descricaoproduto, p.precosugerido
ORDER BY SUM (d.quantidadepedida) DESC LIMIT 10;

-- Listar os funcionários que venderam mais (em quantidade). Exibir: Nome do funcionário, sobrenome, email e o superior dele.
SELECT  f.nome AS "Nome" , 
		f.sobrenome AS "Sobrenome", 
		f.email AS "E-mail",
		f.reportaa AS "Superior",
		COUNT(c.numfuncionarioreprvendas) AS "Qtd Vendas" 
FROM funcionarios f JOIN clientes c 
ON f.numfuncionario = c.numfuncionarioreprvendas 
GROUP BY f.nome, f.sobrenome, f.email, f.reportaa; 

-- Listar os clientes que mais gastaram ($). Exibir: Nome, Sobrenome, Cidade e Estado do Cliente e o limite de créditos deles
SELECT  c.nomecliente AS "Nome",
		c.sobrenomecontato AS "Sobrenome",
		c.cidade AS "Cidade",
		c.estado AS "Estado",
		c.limitecredito AS "Limite de Crédito",
		SUM(p.valor) AS "Valor gasto"
FROM clientes c JOIN pagamentos p
ON c.numcliente = p.numcliente 
GROUP BY c.nomecliente, c.sobrenomecontato, c.cidade, c.estado, c.limitecredito; 


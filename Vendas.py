class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    def total_vendas(self):
        # Calcula o total somando apenas o valor unitário das vendas
        total = 0
        for venda in self.vendas:
            total += venda.valor
        return total

def main():
    # Dados fornecidos para as categorias e vendas
    dados = {
        "Eletrônicos": [
            ("Celular", 5, 1000),
            ("Fone de Ouvido", 10, 500)
        ],
        "Móveis": [
            ("Mesa", 2, 800),
            ("Cadeira", 4, 400)
        ],
        "Alimentos": [
            ("Arroz", 10, 200),
            ("Feijão", 7, 140)
        ],
        "Jardinagem": [
            ("Planta", 2, 60),
            ("Ferramentas", 1, 100)
        ],
        "Livros": [
            ("Aventuras no Tempo", 1, 80),
            ("Mistérios do Oceano", 2, 90)
        ],
        "Esportes": [
            ("Tênis", 7, 210),
            ("Bola", 3, 120)
        ]
    }

    categorias = {}

    # Adicionar vendas às categorias
    for nome_categoria, vendas in dados.items():
        if nome_categoria not in categorias:
            categorias[nome_categoria] = Categoria(nome_categoria)
        
        for produto, quantidade, valor in vendas:
            venda = Venda(produto, quantidade, valor)
            categorias[nome_categoria].adicionar_venda(venda)

    # Exibir os totais de vendas por categoria
    for nome_categoria, categoria in categorias.items():
        total = categoria.total_vendas()
        print(f'Vendas em {nome_categoria}: {total:.1f}')

if __name__ == "__main__":
    main()

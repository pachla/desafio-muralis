# tipos de pagamento
from datetime import datetime

class Pagamento:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        
dinheiro = Pagamento(1, 'dinheiro')
debito = Pagamento(2, 'debito')
credito = Pagamento(3, 'credito')
pix = Pagamento(4, 'pix')
    
    
class Categoria:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

comida = Categoria(1, 'comida', 'refeições em geral')
escritorio = Categoria(2, 'escritorio', 'gastos/custos para o trabalho')
lazer = Categoria(3, 'lazer', 'diversao em geral (jogos, passeios, etc.)')


# despesas (teste)
tipos_de_pagamento = [dinheiro, debito, credito, pix]
categorias = [comida, escritorio, lazer]
despesas = [
    {
        'id': 1,
        'valor': 5,
        'data': datetime.strptime('15/01/23', '%d/%m/%y').date(),
        'descricao': 'arroz',
        'pagamento': tipos_de_pagamento[1].nome,
        'categoria': categorias[0].nome
    },
    {
        'id': 2,
        'valor': 4.5,
        'data': datetime.strptime('15/01/23', '%d/%m/%y').date(),
        'descricao': 'feijao',
        'pagamento': tipos_de_pagamento[1].nome,
        'categoria': categorias[0].nome
    },
    {
        'id': 3,
        'valor': 15,
        'data': datetime.strptime('20/01/23', '%d/%m/%y').date(),
        'descricao': 'mousepad',
        'pagamento': tipos_de_pagamento[1].nome,
        'categoria': categorias[1].nome
    },
    {
        'id': 4,
        'valor': 30,
        'data': datetime.strptime('20/12/22', '%d/%m/%y').date(),
        'descricao': 'cinema',
        'pagamento': tipos_de_pagamento[2].nome,
        'categoria': categorias[2].nome
    }
]

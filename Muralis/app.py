from flask import Flask, jsonify, request, render_template
from datetime import datetime
from db import despesas, tipos_de_pagamento, categorias, Pagamento, Categoria

app = Flask(__name__)

# criar os tipos de pagamento // importada do banco de dados
# criar as categorias // importada do banco de dados

# pagina inicial
@app.route('/', methods=['GET'])
def pagina_inicial():
    return render_template('index.html')

# listar todas as despesas do mes vigente
@app.route('/api/despesas', methods=['GET'])
def get_despesas():
    lista = []
    total = 0
    for despesa in despesas:
        if despesa.get('data').month == datetime.today().month:
            lista.append(despesa)
            total += despesa.get('valor')
    return jsonify({'data': lista, 'total': total, 'success': True})

# listar todas as depesas totais
@app.route('/api/despesasTotais', methods=['GET'])
def get_todas_despesas():
    return jsonify({'data':despesas, 'success': True})

# listas despesas por categoria
@app.route('/api/despesas/<categoria>', methods=['GET'])
def get_por_categoria(categoria):
    lista = []
    for despesa in despesas:
        if despesa.get('categoria') == categoria:
            lista.append(despesa)
    return jsonify({'data': lista, 'success': True})

# adicionar despesa
@app.route('/api/add/despesa', methods=['POST'])
def cadastrar_despesa():
    despesa = request.get_json()
    
    id = despesa['id'] # get id
    valor = despesa['valor'] # get valor
    descricao = despesa['descricao'] # get descricao
    
    for index, pagamento in enumerate(tipos_de_pagamento): # converte o pagamento
        if despesa['pagamento'] == pagamento.nome:
            pagamento = tipos_de_pagamento[index]
    
    for index, categoria in enumerate(categorias): # converte a categoria
        if despesa['categoria'] == categoria.nome:
            categoria = categorias[index]
    
    data = datetime.strptime(despesa['data'], '%d/%m/%y').date() # converte em data
    
    nova_despesa = {
        'id': id,
        'valor': valor,
        'descricao': descricao,
        'pagamento': pagamento.nome,
        'categoria': categoria.nome,
        'data': data
    }
    
    despesas.append(nova_despesa) 
    
    return jsonify({'data': despesas, 'success': True})

# adicionar tipo de pagamento
@app.route('/api/add/pagamento', methods=['POST'])
def cadastrar_pagamento():
    pagamento = request.get_json()
    
    id = pagamento['id']
    nome = pagamento['nome']
    
    novo_pagamento = Pagamento(id, nome)
    
    tipos_de_pagamento.append(novo_pagamento)
    
    return jsonify({'data': f'Pagamento adicionado: {novo_pagamento.id} - {novo_pagamento.nome}',
                    'success': True})
    
    
# adicionar nova categoria de compra
@app.route('/api/add/categoria', methods=['POST'])
def cadastrar_categoria():
    categoria = request.get_json()
    
    id = categoria['id']
    nome = categoria['nome']
    descricao = categoria['descricao']
    
    nova_categoria = Categoria(id, nome, descricao)
    
    categorias.append(nova_categoria)
    
    return jsonify({'data': f'Categoria adicionada: {nova_categoria.id} - {nova_categoria.nome} - {nova_categoria.descricao}',
                   'success': True})

# listar tipos de pagamentos
@app.route('/api/pagamentos', methods=['GET'])
def mostrar_pagamentos():
    lista = []
    for value in tipos_de_pagamento:
        lista.append({'id': value.id,
                      'nome': value.nome})
        
    return jsonify({'data': lista, 'success': True})

# listar categorias e suas descricoes
@app.route('/api/categorias', methods=['GET'])
def mostrar_categorias():
    lista = []
    for value in categorias:
        lista.append({'id': value.id,
                      'nome': value.nome,
                      'descricao': value.descricao})
        
    return jsonify({'data': lista, 'success': True})


app.run(port=5000, host='localhost', debug=True)

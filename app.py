from flask import Flask, jsonify,request
import json

app = Flask(__name__)

clientes =[
    {'id':0,
    'nome':'Carlos',
     'endereco completo':{'rua':'r. goncalves noites', 'numero':'1234', 'cep':'59123-123'},
    'pedido':'cachorro quente',
    'contato':{'telefone':'84987545155', 'email':'carlos@jaironet.com'}
     },

    {'id':1,
    'nome':'Bianco',
     'endereco completo':{'rua':'r. goncalves tardes', 'numero':'1324', 'cep':'58123-123'},
    'pedido':'churrasquinho',
    'contato':{'telefone':'84987545155', 'email':'bianco@jaironet.com'}
     },

    {'id':2,
    'nome':'Jairo',
     'endereco completo':{'rua':'r. goncalves manhas', 'numero':'4321', 'cep':'57123-123'},
    'pedido':'pizza',
     'contato':{'telefone':'84987545155', 'email':'jairo@jaironet.com'}
     },

]
#utilizando ID para buscar, alterar e deletar
@app.route('/clientes/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def cliente(id):
    if request.method == 'GET':
        try:
            response = clientes[id]
        except IndexError:
            mensagem = 'O cliente de ID {} não existe'.format(id)
            response ={'status':'erro', 'mensagem':mensagem}
            print(cliente)
        except Exception:
            mensagem = 'Erro desconhecido. procure o desenvolvedor da API'
            response = {'status': 'erro','mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        clientes[id] = dados
        return jsonify(dados)
    elif request.method =='DELETE':
        clientes.pop(id)
        return jsonify({'status':'Sucesso', 'mensagem':'Registro excluido'})

#permite adicionar e exibir todas os clientes.
@app.route('/clientes/', methods =['POST', 'GET'])
def lista_clientes():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(clientes)
        dados['id'] = posicao
        clientes.append(dados)
        return jsonify(clientes[posicao])
    elif request.method == 'GET':
        return jsonify(clientes)


if __name__ == '__main__':
    app.run()
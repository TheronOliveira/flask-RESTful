from flask import Flask, request
import json
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

bolos =[
    {
        "id":0,
        "coberturas":["Brigadeiro","Leite Ninho","Morango com creme"]
    },
    {
        "id":1,
        "simples":["Laranja","Milho","Coco"]
    }
]
#class para os metodos de busca, atualização e exclusão passando o id como parametro
class Bolos(Resource):
    def get(self,id):
        bolo_selecionado = bolos[id]
        return bolo_selecionado

    def put(self,id):
        dados = json.loads(request.data)
        bolos[id] = dados
        return dados 
    
    def delete(self,id):
        bolos.pop(id)
        return {"status":"sucesso","mensagem":"registro excluído"}

#classe para exibir todos os bolos e cadastrar um novo bolo
class ListaBolos(Resource):
    def get(self):
        return bolos

    def post(self):
        dados = json.loads(request.data)
        posicao = len(bolos)
        dados["id"] = posicao
        bolos.append(dados)
        return {"status":"sucesso","mensagem":"registro inserido com sucesso"}

#metodo add_resources onde é passado dois paranetros:
#o recurso que é a classe e a rota definido após a virgula
api.add_resource(Bolos, "/bolos/<int:id>/")
api.add_resource(ListaBolos, "/bolos/")


if __name__ == "__main__":
    app.run(debug=True)


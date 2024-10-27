#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

#Uma solução simples com estrutura de repetição aninhada, com uma estrutura condicional que verifica o preço

resposta = []
for loja in response:
    for produto in loja["produtos"]:
        if produto["preço"] > 30:
            resposta.append(produto)

print(resposta)

#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

# Estruta de repetição e conficional, que encerra assim que encontra e salva o preço na variável produto_b

produto_b = None

for produto in responsejson["produtos"]:
    if produto["nome"] == "Produto B":
        produto_b = produto["preço"]
        break

print(produto_b)

#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

#Método sort que ordena a lista de maneira mais eficiente, se tratando de memória, 
# que criar uma nova lista com sorted. 

lista.sort()
print(lista)

#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela


lista = ["   joao   ","   maria   ","  joana  "]

#Cria uma nova lista e com uma estrutura de repeticão adiciona o item a essa lista
# com o método strip retiramos os espaços antes e depois de cada item

lista_strip = []
for item in lista:
    lista_strip.append(item.strip())

print(lista_strip)

#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]

#Usei o método pop para remover o segundo item, fácil e eficiente

lista.pop(1)
print(lista)


#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

#Loop com range para iterar pelos indices da lista, baseado no seu tamanho 

for i in range(len(lista)):
    if lista[i] == "joao":
        lista[i] = "maria"

print(lista)

#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

#Utizei o loop while que permite manipular o indice e quantidades de iterações

lista = [1, 2, 3, 4, 5, 6]
i = 0
while i <= 5:
    print(lista[i])
    i += 1

#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra

#Primeiro importamos a biblioteca, criamos uma função que faz a requesição, verifica se ela deu certo (200)
#convertemos para json, conta as task completadas e calcula as pendentes

import requests

def qts_tasks():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    if response.status_code == 200:
        todos = response.json()
        completas = 0
        pendentes = 0

        for todo in todos:
            if todo['completed']:
                completas += 1
            else:
                pendentes += 1
    
        return completas, pendentes

#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra

#Usei o requests.get para obter os dados, transformei a resposta em json, percorri cada usuário 
#e extraí os campos relevantes em um dicionário, adicionando à lista dados_extraidos.
# Essa solução é eficiente para capturar dados específicos de uma estrutura JSON, utilizando somente um loop simples e uma lista.

def extrair_dados():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    
    if response.status_code == 200:
        usuarios = response.json() 
        dados_extraidos = []

        for usuario in usuarios:
            dados = {
                'nome': usuario['name'],
                'username': usuario['username'],
                'email': usuario['email'],
                'rua': usuario['address']['street'],
                'numero': usuario['address']['suite']
            }
            dados_extraidos.append(dados)

        return dados_extraidos


dados = extrair_dados()
print(dados)

#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

#Primeiro importamos o módulo queue nativo do Python, e utilizamos a classe Queue que segue a propriedade FIFO

import queue

fila_FIFO = queue.Queue()
fila_FIFO.put("Primeiro da fila")
fila_FIFO.put("Segundo da fila")
print(fila_FIFO.get())
    

#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO

#Importei a estrutura deque do modo collections, usei uma lista para armazenar os itens, com append adicionamos ao final da lista e com o popleft removemos o primeiro elemento da lista

from collections import deque

lista = deque([1,2,3,4])

def lifo (novo_item,lista):
    if len(lista) >= 4:
        lista.append(novo_item)
        head = lista.popleft()
        print(head)
        return head

resultado = lifo(5,lista)
print(resultado)

#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

#Criei a classe ContaBancaria e uma variavel contadora garantindo que cada conta tenha um ID, depois o contrutor para inicializar ID, nome, CPF e saldo e os métodos depósito e saldo 
#Por ultimo criei os exemplos 

class ContaBancaria:
    count = 1

    def __init__(self, nome, cpf):
        self.id = ContaBancaria.count
        ContaBancaria.count += 1
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return f'Depósito: {valor}. Saldo: {self.saldo}'
        return 'Depósito inválido.'

    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f'Saque: {valor}. Saldo: {self.saldo}'
        return 'Saque inválido ou saldo insuficiente.'


conta = ContaBancaria('João Silva', '123.456.789-00')
print(conta.deposito(500)) 
print(conta.saque(200))    
print(conta.saldo)        








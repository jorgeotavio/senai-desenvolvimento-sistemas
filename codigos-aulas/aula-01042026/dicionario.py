def gritar():
    print('AHHHHHHHHHHHHH')

# pessoa = {
#     'nome': 'Geovania',
#     'idade': 19,
#     'email': 'geovania.19@gmail.com',
#     'gritar': gritar
# }

pessoa = {}

pessoa['nome'] = input("Digite seu nome: ")
pessoa['idade'] = int(input("Digite sua idade: "))
pessoa['email'] = input("Digite seu email: ")

print(pessoa)

dbConnection = {} # só pra exemplificar, isso nao funciona mas existe algo parecido

def cadastra_pessoa(nome, idade, email):
    dbConnection.execute(f"INSERT INTO usuarios (nome, idade, email) VALUES ({nome}, {idade}, {email})")
    return "usuario cadastrado"

mensagem = cadastra_pessoa(pessoa['nome'], pessoa['idade'], pessoa['email'])

pessoa_do_banco = dbConnection.execute(f"SELECT (nome, idade, email) FROM usuarios where id = 0")


import csv
from cadastro import Usuario

def mostrar_usuario(usuario):
    print(f"Nome: {usuario.nome}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Email: {usuario.email}")
    print(f"CPF: {usuario.cpf}")
    print(f"Data de Nascimento: {usuario.data_nascimento}")

def buscar_usuario(nome_consulta):
    with open('usuarios.csv', mode='r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            if len(linha) == 5:
                nome, telefone, email, cpf, data_nascimento = linha
                usuario = Usuario(nome, telefone, email, cpf, data_nascimento)
                if usuario.nome == nome_consulta:
                    mostrar_usuario(usuario)
                    break
        else:
            print("Usuário não encontrado.")
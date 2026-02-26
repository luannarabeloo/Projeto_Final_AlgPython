import csv
from cadastro import Usuario

def salvar_usuario(usuario):
    with open('usuarios.csv', mode='a', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow([usuario.nome, usuario.telefone, usuario.email, usuario.cpf, usuario.data_nascimento])

def carregar_usuarios():
    usuarios = []
    try:
        with open('usuarios.csv', mode='r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                if len(linha) == 5:  # Verifica se a linha tem os campos esperados
                    nome, telefone, email, cpf, data_nascimento = linha
                    usuario = Usuario(nome, telefone, email, cpf, data_nascimento)
                    usuarios.append(usuario)
    except FileNotFoundError:
        pass  # Se o arquivo não existir, retorna uma lista vazia
    return usuarios

def editar_usuario(usuario_editado):
    usuarios = carregar_usuarios()
    usuario_encontrado = False

    for i, u in enumerate(usuarios):
        if u.cpf == usuario_editado.cpf:
            usuarios[i] = usuario_editado
            usuario_encontrado = True
            break

    if usuario_encontrado:
        with open('usuarios.csv', mode='w', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
            for u in usuarios:
                escritor_csv.writerow([u.nome, u.telefone, u.email, u.cpf, u.data_nascimento])
    return usuario_encontrado


def excluir_usuario(nome_excluir):
    usuarios_restantes = []
    usuario_encontrado = False

    with open('usuarios.csv', mode='r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            if len(linha)==5:
                nome, telefone, email, cpf, data_nascimento = linha
                if nome != nome_excluir:
                    usuarios_restantes.append([nome, telefone, email, cpf, data_nascimento])
                else:
                    usuario_encontrado = True

    with open('usuarios.csv', mode='w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerows(usuarios_restantes)

    return usuario_encontrado
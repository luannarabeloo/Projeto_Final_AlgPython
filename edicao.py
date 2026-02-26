import re
from cadastro import Usuario

class Edicao:
    def __init__(self, nome, telefone, email, cpf, data_nascimento):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.data_nascimento = data_nascimento


    def editar_nome(self, novo_nome):
        nome = novo_nome
        validar_nome(novo_nome)
        editar_usuario(self, "nome", novo_nome)
    
    def editar_telefone(self, novo_telefone):
        telefone = novo_telefone
        validar_telefone(novo_telefone)
        editar_usuario(self, "telefone", novo_telefone)
    
    def editar_email(self, novo_email):
        email = novo_email
        validar_email(novo_email)
        editar_usuario(self, "email", novo_email)
    
    def editar_cpf(self, novo_cpf):
        cpf = novo_cpf
        validar_cpf(novo_cpf)
        editar_usuario(self, "cpf", novo_cpf)
    
    def editar_data_nascimento(self, nova_data_nascimento):
        data_nascimento = nova_data_nascimento
        validar_data_nascimento(nova_data_nascimento)
        editar_usuario(self, "data_nascimento", nova_data_nascimento)
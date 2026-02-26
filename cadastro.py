import re

class Usuario:
    def __init__(self, nome, telefone, email, cpf, data_nascimento):
        if not self.validar_nome(nome):
            raise ValueError("Nome inválido.")

        if not self.validar_telefone(telefone):
            raise ValueError("Telefone inválido.")

        if not self.validar_email(email):
            raise ValueError("Email inválido.")

        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido.")
        
        if not self.validar_data_nascimento(data_nascimento):
            raise ValueError("Data de nascimento inválida.")

        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def validar_nome(self, nome):
        if nome.replace(" ", "").isalpha() and len(nome) <= 30:
            return True
        else:
            return False
    
    def validar_telefone(self, telefone):
        if telefone.isdigit() and len(telefone) == 11:
            return True
        else:
            return False

    def validar_email(self, email):
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(padrao, email) is not None and len(email) <= 30

    def validar_cpf(self, cpf):
        cpf = cpf.replace(".", "").replace("-", "")

        if not cpf.isdigit() or len(cpf) != 11:
            return False

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)

        resto = soma % 11
        if resto < 2:
            digito1 = 0
        else: 
            digito1 = 11 - resto

        #digito 2
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)

        resto = soma % 11
        if resto < 2:
            digito2 = 0
        else:
            digito2 = 11 - resto

        if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
            return True
        else:
            return False

    def validar_data_nascimento(self, data_nascimento):
        padrao = r'^\d{2}/\d{2}/\d{4}$'
        return re.match(padrao, data_nascimento) is not None and len(data_nascimento) <= 10
from cadastro import Usuario
import tkinter as tk
from tkinter import messagebox

opcao = 0
usuarios = []  # Lista para armazenar os usuários cadastrados

while opcao != 5:
    print("MENU INICIAL")
    print("1 - Cadastro")
    print("2 - Editar")
    print("3 - Excluir")
    print("4 - Listar")
    print("5 - Sair")

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida. Por favor, digite um número entre 1 e 5.")
        continue

    match opcao:
        case 1:
            def cadastrar():
                nome = entry_nome.get()
                telefone = entry_telefone.get()
                email = entry_email.get()
                cpf = entry_cpf.get()
                data_nascimento = entry_data_nascimento.get()

                try:
                    usuario = Usuario(nome, telefone, email, cpf, data_nascimento)
                    usuarios.append(usuario)
                    messagebox.showinfo("Sucesso", "Usuario cadastrado!")

                    limpar_campos()

                except ValueError as e:
                    messagebox.showerror("Erro", str(e))

            def limpar_campos():
                entry_nome.delete(0, tk.END)
                entry_telefone.delete(0, tk.END)
                entry_email.delete(0, tk.END)
                entry_cpf.delete(0, tk.END)
                entry_data_nascimento.delete(0, tk.END)


            janela = tk.Tk()
            janela.title("Cadastro de Usuário")
            janela.geometry("400x400")

            tk.Label(janela, text="Nome:").pack()
            entry_nome = tk.Entry(janela)
            entry_nome.pack()

            tk.Label(janela, text="Telefone:").pack()
            entry_telefone = tk.Entry(janela)
            entry_telefone.pack()

            tk.Label(janela, text="Email:").pack()
            entry_email = tk.Entry(janela)
            entry_email.pack()

            tk.Label(janela, text="CPF:").pack()
            entry_cpf = tk.Entry(janela)
            entry_cpf.pack()

            tk.Label(janela, text="Data de Nascimento (dd/mm/aaaa):").pack()
            entry_data_nascimento = tk.Entry(janela)
            entry_data_nascimento.pack()

            tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=10)

            janela.mainloop()

        case 2:
            print("MENU DE EDIÇÃO")
        case 3:
            print("MENU DE EXCLUSÃO")
        case 4:
            print("MENU DE LISTAGEM")
            if not usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for u in usuarios:
                    print(f"Nome: {u.nome}, Telefone: {u.telefone}, Email: {u.email}, CPF: {u.cpf}, Data de Nascimento: {u.data_nascimento}")
            print("Saindo do programa...")
            break

print("Programa encerrado.")
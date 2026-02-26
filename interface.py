import tkinter as tk
from tkinter import messagebox
from cadastro import Usuario  # importa sua classe
from arquivo import salvar_usuario  # importa a função de salvar
from arquivo import editar_usuario  # importa a função de edição
from arquivo import carregar_usuarios  # importa a função de carregar usuários # importa a função de mostrar usuário
from arquivo import excluir_usuario  # importa a função de exclusão

usuarios = []

# ---------- TELA DE CADASTRO ----------
def abrir_cadastro():
    janela_menu.withdraw()  # Esconde o menu

    cadastro = tk.Toplevel()
    cadastro.title("Cadastro")
    cadastro.geometry("400x400")

    def voltar():
        cadastro.destroy()
        janela_menu.deiconify()

    # -------- FUNÇÕES --------
    def cadastrar():
        nome = entry_nome.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        cpf = entry_cpf.get()
        data_nascimento = entry_data_nascimento.get()

        try:
            usuario = Usuario(nome, telefone, email, cpf, data_nascimento)
            usuarios.append(usuario)
            salvar_usuario(usuario)  # Salva o usuário no arquivo
            messagebox.showinfo("Sucesso", "Usuário cadastrado!")
            limpar_campos()

        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_data_nascimento.delete(0, tk.END)

    # -------- CAMPOS --------
    tk.Label(cadastro, text="Nome:").pack()
    entry_nome = tk.Entry(cadastro)
    entry_nome.pack()

    tk.Label(cadastro, text="Telefone:").pack()
    entry_telefone = tk.Entry(cadastro)
    entry_telefone.pack()

    tk.Label(cadastro, text="Email:").pack()
    entry_email = tk.Entry(cadastro)
    entry_email.pack()

    tk.Label(cadastro, text="CPF:").pack()
    entry_cpf = tk.Entry(cadastro)
    entry_cpf.pack()

    tk.Label(cadastro, text="Data de Nascimento (dd/mm/aaaa):").pack()
    entry_data_nascimento = tk.Entry(cadastro)
    entry_data_nascimento.pack()

    tk.Button(cadastro, text="Cadastrar", command=cadastrar).pack(pady=10)
    tk.Button(cadastro, text="Voltar", command=voltar).pack(pady=5)

def abrir_edicao():
    janela_menu.withdraw()

    edicao = tk.Toplevel()
    edicao.title("Edição")
    edicao.geometry("400x400")

    def voltar():
        edicao.destroy()
        janela_menu.deiconify()

    def editar():
        nome = entry_novo_nome.get()
        telefone = entry_novo_telefone.get()
        email = entry_novo_email.get()
        cpf = entry_novo_cpf.get()
        data_nascimento = entry_novo_data_nascimento.get()

        try:
            usuario_editado = Usuario(nome, telefone, email, cpf, data_nascimento)

            if editar_usuario(usuario_editado):
                carregar_usuarios()  
                messagebox.showinfo("Sucesso", "Usuário editado!")
            else:
                messagebox.showerror("Erro", "Usuário não encontrado.")
            limpar_campos()  
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def limpar_campos():
        entry_novo_nome.delete(0, tk.END)
        entry_novo_telefone.delete(0, tk.END)
        entry_novo_email.delete(0, tk.END)
        entry_novo_cpf.delete(0, tk.END)
        entry_novo_data_nascimento.delete(0, tk.END)

# -------- CAMPOS --------
    tk.Label(edicao, text="Nome:").pack()
    entry_novo_nome = tk.Entry(edicao)
    entry_novo_nome.pack()

    tk.Label(edicao, text="Telefone:").pack()
    entry_novo_telefone = tk.Entry(edicao)
    entry_novo_telefone.pack()

    tk.Label(edicao, text="Email:").pack()
    entry_novo_email = tk.Entry(edicao)
    entry_novo_email.pack()

    tk.Label(edicao, text="CPF:").pack()
    entry_novo_cpf = tk.Entry(edicao)
    entry_novo_cpf.pack()   

    tk.Label(edicao, text="Data de Nascimento (dd/mm/aaaa):").pack()
    entry_novo_data_nascimento = tk.Entry(edicao)
    entry_novo_data_nascimento.pack()

    tk.Button(edicao, text="Editar", command=editar).pack(pady=10)
    tk.Button(edicao, text="Voltar", command=voltar).pack(pady=5)

def abrir_consulta():
    janela_menu.withdraw()

    consulta = tk.Toplevel()
    consulta.title("Consulta de Usuários")
    consulta.geometry("400x400")


    def voltar():
        consulta.destroy()
        janela_menu.deiconify()

 # ------- CAMPOS --------
    tk.Label(consulta, text="Consultar usuario: ", font=("Arial", 10)).pack(pady=10)
    tk.Label(consulta, text="NOME:").pack()

    tk.Label(consulta, text="Digite o nome do usuário para consulta:").pack()
    entry_nome_consulta = tk.Entry(consulta)
    entry_nome_consulta.pack()

    resultado_label = tk.Label(consulta, text="", justify="left")
    resultado_label.pack()

    def consultar_usuarios():
        nome_consulta = entry_nome_consulta.get()
        usuarios = carregar_usuarios()

        texto = ""
        encontrado = False

        for u in usuarios:
            if u.nome.lower() == nome_consulta.lower():
                texto += f"Nome: {u.nome}\nCPF: {u.cpf}\nTelefone: {u.telefone}\nEmail: {u.email}\nData de Nascimento: {u.data_nascimento}\n\n"
                encontrado = True

        if encontrado:
            resultado_label.config(text=texto)
        else:
            resultado_label.config(text="Nenhum usuário encontrado.")

    tk.Button(consulta, text="Consultar", command=consultar_usuarios).pack(pady=10)
    tk.Button(consulta, text="Voltar", command=voltar).pack(pady=5)


def abrir_exclusao():
    janela_menu.withdraw()

    exclusao = tk.Toplevel()
    exclusao.title("Exclusão de Usuários")
    exclusao.geometry("400x400")

    def voltar():
        exclusao.destroy()
        janela_menu.deiconify()

    tk.Label(exclusao, text="Digite o nome do usuário para exclusão:").pack(pady=10)

# ------- CAMPOS --------
    entry_nome_exclusao = tk.Entry(exclusao)
    entry_nome_exclusao.pack()

    resultado_label_exclusao = tk.Label(exclusao, text="")
    resultado_label_exclusao.pack()

    def excluir():
        nome = entry_nome_exclusao.get()
        sucesso = excluir_usuario(nome)

        if sucesso:
            resultado_label_exclusao.config(text="Usuário excluído com sucesso.")
        else:
            resultado_label_exclusao.config(text="Usuário não encontrado.")

    tk.Button(exclusao, text="Excluir", command=excluir).pack(pady=10)
    tk.Button(exclusao, text="Voltar", command=voltar).pack(pady=5)

# ---------- TELA MENU ----------
janela_menu = tk.Tk()
janela_menu.title("Menu Principal")
janela_menu.geometry("300x300")

tk.Label(janela_menu, text="MENU PRINCIPAL", font=("Arial", 14)).pack(pady=10)

tk.Button(janela_menu, text="1 - Cadastro", command=abrir_cadastro).pack(pady=5)
tk.Button(janela_menu, text="2 - Edição", command=abrir_edicao).pack(pady=5)
tk.Button(janela_menu, text="3 - Consulta", command=abrir_consulta).pack(pady=5)
tk.Button(janela_menu, text="4 - Exclusão", command=abrir_exclusao).pack(pady=5)
tk.Button(janela_menu, text="5 - Sair", command=janela_menu.quit).pack(pady=5)

janela_menu.mainloop()
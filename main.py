# Ponto de entrada: ecrã para iniciar sessão ou criar conta.

import tkinter as tk
from layout_cliente import *
from layout_admin import *

def f_tela_iniciar_seccao():
    root = tk.Tk()
    root.title("Iniciar/Criar Conta")
    root.geometry("683x393")
    root.resizable(True,True)
    root.configure(background="#e6ffe6")
    frame = Frame(root, relief="solid", background="#ccffcc", borderwidth=1, pady=20, padx=20)
    ooo = 0
    f_mudar_criar_sessao(root, frame, ooo)
    root.mainloop()

def validar_num_telefone(valor):
    return valor.isdigit() or valor == ""

def validar_num_nif(valor):
    return (valor.isdigit() or valor == "") and len(valor) <= 9

def f_mudar_criar_sessao(root, frame_criar_conta ,*args):
    so_digitos_telefone = root.register(validar_num_telefone)
    so_digitos_nif = root.register(validar_num_nif)
    if args[0] == 0:
        pass
    else:
        args[0].configure(state="active")
        args[1].configure(state="disabled")
        args[2].pack_forget()
        for arg in args:
            arg.grid_forget()

    label_criar_conta = Label(
        frame_criar_conta,
        text="Criar Conta",
        font="Arial, 19",
        background="#ccffcc",
        anchor="center"
    )
    #   Label para criar o nome
    label_criar_conta_nome = Label(
        frame_criar_conta,
        text="Nome ",
        font="Arial, 17",
        background="#ccffcc",
        padx=10
    )
    #   Entry para criar o nome
    texto_criar_conta_nome = Entry(
        frame_criar_conta,
        font="Arial, 15",
        background="white",
        borderwidth=1,
        relief="solid"
    )
    #   Label para criar o nif
    label_criar_conta_nif = Label(
        frame_criar_conta,
        text="Nif ",
        font="Arial, 17",
        background="#ccffcc",
        padx=10
    )
    #   Entry para criar o nif
    texto_criar_conta_nif = Entry(
        frame_criar_conta,
        font="Arial, 15",
        background="white",
        borderwidth=1,
        relief="solid",
        validate="key",
        validatecommand=(so_digitos_nif, "%P")
    )
    #   Label para criar o email
    label_criar_conta_email = Label(
        frame_criar_conta,
        text="Email ",
        font="Arial, 17",
        background="#ccffcc",
        padx=10
    )
    #   Entry para criar o email
    texto_criar_conta_email = Entry(
        frame_criar_conta,
        font="Arial, 15",
        background="white",
        borderwidth=1,
        relief="solid"
    )
    #   Label para criar o telefone
    label_criar_conta_telefone = Label(
        frame_criar_conta,
        text="Telefone ",
        font="Arial, 17",
        background="#ccffcc",
        padx=10
    )
    #   Entry para criar o telefone
    texto_criar_conta_telefone = Entry(
        frame_criar_conta,
        font="Arial, 15",
        background="white",
        borderwidth=1,
        relief="solid",
        validate="key",
        validatecommand=(so_digitos_telefone, "%P")
    )
    #   Label para criar a password
    label_criar_conta_password = Label(
        frame_criar_conta,
        text="Password ",
        font="Arial, 17",
        background="#ccffcc",
        padx=10
    )
    #   Entry para criar a password
    texto_criar_conta_password = Entry(
        frame_criar_conta,
        font="Arial, 15",
        background="white",
        borderwidth=1,
        relief="solid"
    )
    butao_iniciar_sessao = Button(
        frame_criar_conta,
        text="Iniciar Sessão",
        font="Arial, 15",
        relief="solid",
        borderwidth=1,
        cursor="hand2",
        command=lambda:f_mudar_iniciar_sessao(root,
                                              frame_criar_conta,
                                              butao_criar_sessao,
                                              butao_iniciar_sessao,
                                              butao_continuar,
                                              label_criar_conta,
                                              label_criar_conta_nome,
                                              texto_criar_conta_nome,
                                              label_criar_conta_nif,
                                              texto_criar_conta_nif,
                                              label_criar_conta_email,
                                              texto_criar_conta_email,
                                              label_criar_conta_telefone,
                                              texto_criar_conta_telefone,
                                              label_criar_conta_password,
                                              texto_criar_conta_password)
    )
    butao_criar_sessao = Button(
        frame_criar_conta,
        text="Criar Sessão",
        font="Arial, 15",
        relief="solid",
        borderwidth=1,
        cursor="hand2",
        state="disabled",
        disabledforeground="grey",
        command=lambda:f_mudar_criar_sessao(root, frame_criar_conta, butao_criar_sessao, butao_iniciar_sessao)
    )

    butao_continuar = Button(
        root,
        text="Continuar",
        font="Arial, 15",
        relief="solid",
        borderwidth=1,
        cursor="hand2",
        command=lambda:f_continuar("criar", root, texto_criar_conta_email, texto_criar_conta_password, 1, texto_criar_conta_nome, texto_criar_conta_telefone, texto_criar_conta_nif)
    )


    label_criar_conta.grid(column=0, row=0, columnspan=2, sticky="nsew", pady=10)

    label_criar_conta_nome.grid(    column=0, row=1, sticky="e", pady=10, padx=20)
    texto_criar_conta_nome.grid(    column=1, row=1, sticky="w", pady=10, padx=10)

    label_criar_conta_nif.grid(     column=0, row=2, sticky="e", pady=10, padx=20)
    texto_criar_conta_nif.grid(     column=1, row=2, sticky="w", pady=10, padx=10)

    label_criar_conta_email.grid(   column=0, row=3, sticky="e", pady=10, padx=20)
    texto_criar_conta_email.grid(   column=1, row=3, sticky="w", pady=10, padx=10)

    label_criar_conta_telefone.grid(column=0, row=4, sticky="e", pady=10, padx=20)
    texto_criar_conta_telefone.grid(column=1, row=4, sticky="w", pady=10, padx=10)

    label_criar_conta_password.grid(column=0, row=5, sticky="e", pady=10, padx=20)
    texto_criar_conta_password.grid(column=1, row=5, sticky="w", pady=10, padx=10)

    butao_iniciar_sessao.grid(column=0, row=6, sticky="w", pady=20, padx=(10, 0))
    butao_criar_sessao.grid(column=1,row=6, sticky="e", pady=20, padx=(0, 10))

    frame_criar_conta.pack(expand=True)

    butao_continuar.pack(expand=True, side="top", anchor="n")

def f_mudar_iniciar_sessao(root, frame_iniciar_conta, *args):
    args[0].configure(state="active")
    args[1].configure(state="disabled")
    args[2].pack_forget()
    for arg in args:
        arg.grid_forget()

    label_iniciar_conta = Label(
        frame_iniciar_conta,
        text="Iniciar Conta",
        font="Arial, 19",
        background="#ccffcc",
        anchor="center"
    )

    #   Label para iniciar com o email
    label_iniciar_conta_email = Label(
        frame_iniciar_conta,
        text="Email ",
        font="Arial, 17",
        background="#ccffcc",
        padx=10
    )
    #   Entry para iniciar com o email
    texto_iniciar_conta_email = Entry(
        frame_iniciar_conta,
        font="Arial, 15",
        background="white",
        borderwidth=1,
        relief="solid"
    )
    #   Label para iniciar com a password
    label_iniciar_conta_password = Label(
        frame_iniciar_conta,
        text="Password ",
        font="Arial, 17",
        background="#ccffcc",
        padx=10
    )
    #   Entry para iniciar com a password
    texto_iniciar_conta_password = Entry(
        frame_iniciar_conta,
        font="Arial, 15",
        background="white",
        borderwidth=1,
        relief="solid"
    )

    butao_iniciar_sessao = Button(
        frame_iniciar_conta,
        text="Iniciar Sessão",
        font="Arial, 15",
        relief="solid",
        borderwidth=1,
        state="disabled",
        cursor="hand2",
        command=lambda:f_mudar_iniciar_sessao(root,
                                              frame_iniciar_conta,
                                              butao_criar_sessao,
                                              butao_iniciar_sessao,
                                              butao_continuar)
    )
    butao_criar_sessao = Button(
        frame_iniciar_conta,
        text="Criar Sessão",
        font="Arial, 15",
        relief="solid",
        borderwidth=1,
        cursor="hand2",
        disabledforeground="grey",
        command=lambda:f_mudar_criar_sessao(root,
                                            frame_iniciar_conta,
                                            butao_criar_sessao,
                                            butao_iniciar_sessao,
                                            butao_continuar,
                                            )
    )

    butao_continuar = Button(
        root,
        text="Continuar",
        font="Arial, 15",
        relief="solid",
        borderwidth=1,
        cursor="hand2",
        command=lambda:f_continuar("iniciar", root, texto_iniciar_conta_email, texto_iniciar_conta_password, 0)
    )

    label_iniciar_conta.grid(column=0, row=0, columnspan=2, sticky="nsew", pady=10)
    label_iniciar_conta_email.grid(column=0, row=1, sticky="e", pady=10, padx=20)
    texto_iniciar_conta_email.grid(column=1, row=1, sticky="w", pady=10, padx=10)
    label_iniciar_conta_password.grid(column=0, row=2, sticky="e", pady=10, padx=20)
    texto_iniciar_conta_password.grid(column=1, row=2, sticky="w", pady=10, padx=10)
    butao_iniciar_sessao.grid(column=0, row=6, sticky="w", pady=20, padx=(10, 0))
    butao_criar_sessao.grid(column=1,row=6, sticky="e", pady=20, padx=(0, 10))

    butao_continuar.pack(expand=True, side="top", anchor="n")

def f_continuar(fazer, root, *args):
    if args[2] == 0:
        email = args[0].get()
        password = args[1].get()
    else:
        email = args[0].get()
        password = args[1].get()
        nome = args[3].get()
        telefone = args[4].get()
        nif = args[5].get()
    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        if fazer == "iniciar":
            try:
                f_iniciar_cliente(email, password)
                messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
                root.destroy()
                if f_ver_cliente_admin(email):
                    JanelaPrincipalCliente(f_procurar_cliente_id(email))
                else:
                    SistemaHotel()
                # Aqui podes abrir o menu principal
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        if fazer == "criar":
            try:
                f_adicionar_cliente(nome, nif, email, telefone, password)
                messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
                root.destroy()
                if f_ver_cliente_admin(email):
                    JanelaPrincipalCliente(f_procurar_cliente_id(email))
                else:
                    SistemaHotel()
            except Exception as e:
                messagebox.showerror("Erro", str(e))
    else:
        messagebox.showerror("Erro", "Email Inválido")

f_tela_iniciar_seccao()

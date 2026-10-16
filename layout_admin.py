# Painel de administração: clientes, quartos, reservas, pagamentos, funcionários e manutenção.

from tkinter import *
from tkinter import ttk, messagebox
from funcoes import *


# ----------------- FUNÇÃO DE ERRO -----------------
def mostrar_erro(msg):
    messagebox.showerror("Erro", msg)


# ----------------- JANELA PRINCIPAL -----------------
# Função principal que constrói e gere a interface do sistema
def SistemaHotel():
    # Criação da janela principal (root)
    root = Tk()
    root.title("Administração do Hotel")
    root.geometry("1100x650")
    root.resizable(False, False) # Impede redimensionamento para manter layout fixo

    # ESTILOS
    style = ttk.Style()
    style.configure("Title.TLabel", font=("Arial", 16, "bold"))
    style.configure("Menu.TButton", font=("Arial", 11), width=20)

    menu = Frame(root, bg="#2c3e50", width=220)
    menu.pack(side=LEFT, fill=Y)

    conteudo = Frame(root, bg="#ecf0f1")
    conteudo.pack(side=RIGHT, fill=BOTH, expand=True)

    # Função para limpar a área de conteúdo (painel direito) antes de carregar um novo menu
    def limpar():
        for widget in conteudo.winfo_children():
            widget.destroy()

    # Atalho para criar botões estilizados para o menu lateral
    def botao(texto, comando):
        return ttk.Button(menu, text=texto, command=comando, style="Menu.TButton")

    # --- SEÇÃO DE CLIENTES ---
    def menu_clientes():
        limpar() # Limpa a tela antes de mostrar o menu de clientes
        ttk.Label(conteudo, text="Clientes", style="Title.TLabel").pack(pady=10)

        # Definição das entradas de texto (Entry) para o formulário
        nif = ttk.Entry(conteudo, width=40)
        email = ttk.Entry(conteudo, width=40)
        telefone = ttk.Entry(conteudo, width=40)
        senha = ttk.Entry(conteudo, width=40)
        cid = ttk.Entry(conteudo, width=40)

        campos = [
            ("Nome", nome), ("NIF", nif), ("Email", email),
            ("Telefone", telefone), ("Senha", senha), ("Cliente ID", cid)
        ]

        for l, e in campos:
            ttk.Label(conteudo, text=l).pack()
            e.pack(pady=3)

        is_admin = IntVar()
        ttk.Checkbutton(conteudo, text="Admin?", variable=is_admin).pack(pady=5)

        def adicionar():
            try:
                f_adicionar_cliente(nome.get(), nif.get(), email.get(), telefone.get(), senha.get())
                messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso.")
            except Exception as e:
                mostrar_erro(str(e))

        def listar_clientes():
            try:
                headers = ("ID", "Nome", "NIF", "Email", "Telefone", "Senha", "Cadastro", "Admin")
                listar(headers, f_listar_clientes())
            except Exception as e:
                mostrar_erro(str(e))

        def remover():
            try:
                f_remover_cliente(cid.get())
                messagebox.showinfo("Sucesso", "Cliente removido.")
            except Exception as e:
                mostrar_erro(str(e))

        def atualizar_admin():
            try:
                if not cid.get():
                    raise ValueError("ID do Cliente é necessário.")
                f_admin(cid.get(), is_admin.get())
                messagebox.showinfo("Sucesso", "Status de admin atualizado.")
            except Exception as e:
                mostrar_erro(str(e))

        ttk.Button(conteudo, text="Adicionar", command=adicionar).pack(pady=3)
        ttk.Button(conteudo, text="Listar", command=listar_clientes).pack(pady=3)
        ttk.Button(conteudo, text="Remover", command=remover).pack(pady=3)
        ttk.Button(conteudo, text="Atualizar Admin", command=atualizar_admin).pack(pady=3)

    #QUARTOS
    def menu_quartos():
        limpar()
        ttk.Label(conteudo, text="Quartos", style="Title.TLabel").pack(pady=10)

        end = ttk.Entry(conteudo, width=40)
        tipo = ttk.Entry(conteudo, width=40)
        cap = ttk.Entry(conteudo, width=40)
        vn = ttk.Entry(conteudo, width=40)
        vp = ttk.Entry(conteudo, width=40)
        qid = ttk.Entry(conteudo, width=40)

        campos = [
            ("Endereço", end), ("Tipo", tipo), ("Capacidade", cap),
            ("Valor Noite", vn), ("Valor Pessoa", vp), ("Quarto ID", qid)
        ]

        for l, e in campos:
            ttk.Label(conteudo, text=l).pack()
            e.pack(pady=3)

        def adicionar():
            try:
                f_adicionar_quarto(end.get(), tipo.get(), cap.get(), vn.get(), vp.get())
                messagebox.showinfo("Sucesso", "Quarto adicionado.")
            except Exception as e:
                mostrar_erro(str(e))

        def listar_quartos():
            try:
                headers = ("ID", "Endereço", "Tipo", "Capacidade", "Valor Noite", "Valor Pessoa", "Status")
                listar(headers, f_listar_quartos())
            except Exception as e:
                mostrar_erro(str(e))

        def remover():
            try:
                f_remover_quarto(qid.get())
                messagebox.showinfo("Sucesso", "Quarto removido.")
            except Exception as e:
                mostrar_erro(str(e))

        ttk.Button(conteudo, text="Adicionar", command=adicionar).pack(pady=3)
        ttk.Button(conteudo, text="Listar", command=listar_quartos).pack(pady=3)
        ttk.Button(conteudo, text="Remover", command=remover).pack(pady=3)

    #RESERVAS
    def menu_reservas():
        limpar()
        ttk.Label(conteudo, text="Reservas", style="Title.TLabel").pack(pady=10)

        cid = ttk.Entry(conteudo, width=40)
        qid = ttk.Entry(conteudo, width=40)
        ci = ttk.Entry(conteudo, width=40)
        co = ttk.Entry(conteudo, width=40)
        vt = ttk.Entry(conteudo, width=40)
        rid = ttk.Entry(conteudo, width=40)

        campos = [
            ("Cliente ID", cid), ("Quarto ID", qid),
            ("Check-in", ci), ("Check-out", co),
            ("Valor Total", vt), ("Reserva ID", rid)
        ]

        for l, e in campos:
            ttk.Label(conteudo, text=l).pack()
            e.pack(pady=3)

        def adicionar():
            try:
                f_adicionar_reserva(cid.get(), qid.get(), ci.get(), co.get(), vt.get())
                messagebox.showinfo("Sucesso", "Reserva adicionada.")
            except Exception as e:
                mostrar_erro(str(e))

        def listar_reservas():
            try:
                headers = ("ID", "Cliente", "Quarto", "Check-in", "Check-out", "Total", "Status")
                listar(headers, f_listar_reservas())
            except Exception as e:
                mostrar_erro(str(e))

        def remover():
            try:
                f_remover_reserva(rid.get())
                messagebox.showinfo("Sucesso", "Reserva removida.")
            except Exception as e:
                mostrar_erro(str(e))

        ttk.Button(conteudo, text="Adicionar", command=adicionar).pack(pady=3)
        ttk.Button(conteudo, text="Listar", command=listar_reservas).pack(pady=3)
        ttk.Button(conteudo, text="Remover", command=remover).pack(pady=3)

    #PAGAMENTOS
    def menu_pagamentos():
        limpar()
        ttk.Label(conteudo, text="Pagamentos", style="Title.TLabel").pack(pady=10)

        rid = ttk.Entry(conteudo, width=40)
        data = ttk.Entry(conteudo, width=40)
        metodo = ttk.Entry(conteudo, width=40)
        valor = ttk.Entry(conteudo, width=40)
        pid = ttk.Entry(conteudo, width=40)

        campos = [
            ("Reserva ID", rid), ("Data", data),
            ("Método", metodo), ("Valor", valor),
            ("Pagamento ID", pid)
        ]

        for l, e in campos:
            ttk.Label(conteudo, text=l).pack()
            e.pack(pady=3)

        def adicionar():
            try:
                f_adicionar_pagamento(rid.get(), data.get(), metodo.get(), valor.get())
                messagebox.showinfo("Sucesso", "Pagamento registado.")
            except Exception as e:
                mostrar_erro(str(e))

        def listar_pagamentos():
            try:
                headers = ("ID", "Reserva ID", "Data", "Método", "Valor", "Status")
                listar(headers, f_listar_pagamentos())
            except Exception as e:
                mostrar_erro(str(e))

        def remover():
            try:
                f_remover_pagamento(pid.get())
                messagebox.showinfo("Sucesso", "Pagamento removido.")
            except Exception as e:
                mostrar_erro(str(e))

        ttk.Button(conteudo, text="Adicionar", command=adicionar).pack(pady=3)
        ttk.Button(conteudo, text="Listar", command=listar_pagamentos).pack(pady=3)
        ttk.Button(conteudo, text="Remover", command=remover).pack(pady=3)

    #FUNCIONÁRIOS
    def menu_funcionarios():
        limpar()
        ttk.Label(conteudo, text="Funcionários", style="Title.TLabel").pack(pady=10)

        nome = ttk.Entry(conteudo, width=40)
        cargo = ttk.Entry(conteudo, width=40)
        email = ttk.Entry(conteudo, width=40)
        tel = ttk.Entry(conteudo, width=40)
        data = ttk.Entry(conteudo, width=40)
        ordn = ttk.Entry(conteudo, width=40)
        fid = ttk.Entry(conteudo, width=40)

        campos = [
            ("Nome", nome), ("Cargo", cargo), ("Email", email),
            ("Telefone", tel), ("Data", data),
            ("Ordenado", ordn), ("Funcionário ID", fid)
        ]

        for l, e in campos:
            ttk.Label(conteudo, text=l).pack()
            e.pack(pady=3)

        def adicionar():
            try:
                f_adicionar_funcionario(nome.get(), cargo.get(), email.get(), tel.get(), data.get(), ordn.get())
                messagebox.showinfo("Sucesso", "Funcionário adicionado.")
            except Exception as e:
                mostrar_erro(str(e))

        def listar_funcionarios():
            try:
                headers = ("ID", "Nome", "Cargo", "Email", "Telefone", "Contratação", "Ordenado")
                listar(headers, f_listar_funcionarios())
            except Exception as e:
                mostrar_erro(str(e))

        def remover():
            try:
                f_remover_funcionario(fid.get())
                messagebox.showinfo("Sucesso", "Funcionário removido.")
            except Exception as e:
                mostrar_erro(str(e))

        ttk.Button(conteudo, text="Adicionar", command=adicionar).pack(pady=3)
        ttk.Button(conteudo, text="Listar", command=listar_funcionarios).pack(pady=3)
        ttk.Button(conteudo, text="Remover", command=remover).pack(pady=3)

    #MANUTENÇÃO
    def menu_manutencao():
        limpar()
        ttk.Label(conteudo, text="Manutenção", style="Title.TLabel").pack(pady=10)

        qid = ttk.Entry(conteudo, width=40)
        fid = ttk.Entry(conteudo, width=40)
        desc = ttk.Entry(conteudo, width=40)
        ini = ttk.Entry(conteudo, width=40)
        fim = ttk.Entry(conteudo, width=40)
        resp = ttk.Entry(conteudo, width=40)
        mid = ttk.Entry(conteudo, width=40)

        campos = [
            ("Quarto ID", qid), ("Funcionário ID", fid),
            ("Descrição", desc), ("Início", ini),
            ("Fim", fim), ("Responsável", resp),
            ("Manutenção ID", mid)
        ]

        for l, e in campos:
            ttk.Label(conteudo, text=l).pack()
            e.pack(pady=3)

        def adicionar():
            try:
                f_adicionar_manutencao(qid.get(), fid.get(), desc.get(), ini.get(), fim.get(), resp.get())
                messagebox.showinfo("Sucesso", "Manutenção registada.")
            except Exception as e:
                mostrar_erro(str(e))

        def listar_manutencoes():
            try:
                headers = ("ID", "Quarto", "Funcionário", "Descrição", "Início", "Fim", "Responsável")
                listar(headers, f_listar_manutencoes())
            except Exception as e:
                mostrar_erro(str(e))

        def remover():
            try:
                f_remover_manutencao(mid.get())
                messagebox.showinfo("Sucesso", "Manutenção removida.")
            except Exception as e:
                mostrar_erro(str(e))

        ttk.Button(conteudo, text="Adicionar", command=adicionar).pack(pady=3)
        ttk.Button(conteudo, text="Listar", command=listar_manutencoes).pack(pady=3)
        ttk.Button(conteudo, text="Remover", command=remover).pack(pady=3)

    # --- FUNÇÃO DE LISTAGEM GENÉRICA (TABELAS) ---
    # Esta função cria uma visualização em tabela (Treeview) para qualquer conjunto de dados
    def listar(cabecalhos, dados):
        limpar() # Limpa o conteúdo atual

        # Frame container para a tabela e scrollbar
        frame_tabela = Frame(conteudo)
        frame_tabela.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Adiciona barra de rolagem vertical
        scrollbar = ttk.Scrollbar(frame_tabela)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configura o Treeview (tabela)
        # columns: define os nomes internos das colunas
        # show="headings": esconde a primeira coluna vazia padrão do Treeview
        tree = ttk.Treeview(frame_tabela, columns=cabecalhos, show="headings",
                            yscrollcommand=scrollbar.set)

        # Configura os cabeçalhos das colunas
        for col in cabecalhos:
            tree.heading(col, text=col) # Define o texto visível do cabeçalho
            tree.column(col, width=100, anchor=CENTER) # Centraliza o texto e define largura fixa

        # Insere os dados vindos do banco de dados na tabela
        for d in dados:
            tree.insert("", END, values=d)

        # Exibe a tabela e vincula a barra de rolagem
        tree.pack(fill=BOTH, expand=True)
        scrollbar.config(command=tree.yview)

    #MENU
    ttk.Label(menu, text="MENU", foreground="white",
              background="#2c3e50", font=("Arial", 16, "bold")).pack(pady=20)

    botao("Clientes", menu_clientes).pack(pady=5,padx=20)
    botao("Quartos", menu_quartos).pack(pady=5,padx=20)
    botao("Reservas", menu_reservas).pack(pady=5,padx=20)
    botao("Pagamentos", menu_pagamentos).pack(pady=5,padx=20)
    botao("Funcionários", menu_funcionarios).pack(pady=5,padx=20)
    botao("Manutenção", menu_manutencao).pack(pady=5,padx=20)

    # Botão Sair destacado em vermelho e posicionado no fundo do menu
    Button(menu, text="Sair", command=root.destroy, bg="red", fg="white",
           font=("Arial", 11), width=18).pack(side=BOTTOM, pady=20,padx=20)

    root.mainloop()

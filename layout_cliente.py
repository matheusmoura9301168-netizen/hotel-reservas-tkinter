# Área do cliente: consultar quartos e fazer reservas.

from tkinter import *
from tkinter import ttk, messagebox
from funcoes import *
from datetime import datetime


# ----------------- FUNÇÕES DE APOIO -----------------
def limpar_ecra(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# ----------------- INTERFACE DO CLIENTE -----------------
def JanelaPrincipalCliente(id_cliente_logado):
    root = Tk()
    root.title("Hotel - Portal do Cliente")
    root.geometry("1100x650")
    root.resizable(True, True)

    # Definições de Cores (Estilo semelhante ao Admin)
    cor_menu = "#2c3e50"
    cor_fundo = "#ecf0f1"
    cor_detalhe = "#3498db"

    # --- Estrutura Principal ---
    menu_lateral = Frame(root, bg=cor_menu, width=220)
    menu_lateral.pack(side="left", fill="y")

    conteudo = Frame(root, bg=cor_fundo)
    conteudo.pack(side="right", fill="both", expand=True)

    # ----------------- LOGICA: PERFIL -----------------
    def aba_perfil():
        limpar_ecra(conteudo)
        Label(conteudo, text="A Minha Conta", font=("Arial", 18, "bold"), bg=cor_fundo).pack(pady=20)

        # Procurar dados na BD
        conn = f_get_conn()
        c = conn.cursor()
        c.execute("SELECT C_Nome, C_Email, C_Telefone, C_NIF FROM Cliente WHERE C_ID_Cliente=?", (id_cliente_logado,))
        user = c.fetchone()
        conn.close()

        form = Frame(conteudo, bg=cor_fundo)
        form.pack(pady=10)

        Label(form, text="Nome:", bg=cor_fundo).grid(row=0, column=0, sticky=W, pady=5)
        e_nome = Entry(form, width=35, font=("Arial", 10))
        e_nome.insert(0, user[0]);
        e_nome.grid(row=0, column=1, pady=5)

        Label(form, text="Email:", bg=cor_fundo).grid(row=1, column=0, sticky=W, pady=5)
        e_email = Entry(form, width=35, font=("Arial", 10))
        e_email.insert(0, user[1]);
        e_email.grid(row=1, column=1, pady=5)

        Label(form, text="Telefone:", bg=cor_fundo).grid(row=2, column=0, sticky=W, pady=5)
        e_tel = Entry(form, width=35, font=("Arial", 10))
        e_tel.insert(0, user[2]);
        e_tel.grid(row=2, column=1, pady=5)

        Label(form, text="NIF:", bg=cor_fundo).grid(row=3, column=0, sticky=W, pady=5)
        e_nif = Entry(form, width=35, font=("Arial", 10), state='readonly')
        e_nif.insert(0, user[3]);
        e_nif.grid(row=3, column=1, pady=5)

        def salvar():
            try:
                f_atualizar_cliente(id_cliente_logado, e_nome.get(), e_email.get(), e_tel.get())
                messagebox.showinfo("Sucesso", "Dados atualizados!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        Button(conteudo, text="Guardar Alterações", bg="#27ae60", fg="white",
               command=salvar, width=20, height=2).pack(pady=20)

    # ----------------- LOGICA: RESERVAS -----------------
    def aba_reservar():
        limpar_ecra(conteudo)
        Label(conteudo, text="Reservar Quarto", font=("Arial", 18, "bold"), bg=cor_fundo).pack(pady=10)

        # Filtros
        f_filtros = Frame(conteudo, bg="#d1d8e0", pady=10, padx=10)
        f_filtros.pack(fill="x", padx=20)

        Label(f_filtros, text="Pessoas:", bg="#d1d8e0").grid(row=0, column=0)
        spn_pess = Spinbox(f_filtros, from_=1, to=10, width=5);
        spn_pess.grid(row=0, column=1, padx=5)

        Label(f_filtros, text="Noites:", bg="#d1d8e0").grid(row=0, column=2)
        spn_noit = Spinbox(f_filtros, from_=1, to=30, width=5);
        spn_noit.grid(row=0, column=3, padx=5)

        Label(f_filtros, text="Data Check-in:", bg="#d1d8e0").grid(row=0, column=4)
        ent_data = Entry(f_filtros, width=12)
        ent_data.insert(0, datetime.now().strftime("%d/%m/%Y"))
        ent_data.grid(row=0, column=5, padx=5)

        # Tabela
        cols = ("id", "tipo", "cap", "p_noite", "p_pess", "total")
        tree = ttk.Treeview(conteudo, columns=cols, show="headings", height=10)
        tree.heading("id", text="ID");
        tree.column("id", width=40)
        tree.heading("tipo", text="Tipo")
        tree.heading("cap", text="Capacidade")
        tree.heading("p_noite", text="€/Noite")
        tree.heading("p_pess", text="€/Pessoa")
        tree.heading("total", text="VALOR TOTAL")
        tree.pack(pady=15, padx=20, fill="both")

        def carregar_disponiveis():
            for i in tree.get_children(): tree.delete(i)
            pess = int(spn_pess.get())
            noit = int(spn_noit.get())

            for q in f_listar_quartos():
                if q[3] >= pess and q[6] == 0:  # Capacidade OK e Disponível (0)
                    calc = (q[4] * noit) + (q[5] * pess)
                    tree.insert("", "end", values=(q[0], q[2], q[3], q[4], q[5], f"{calc}€"))

        Button(f_filtros, text="Pesquisar", command=carregar_disponiveis, bg=cor_detalhe, fg="white").grid(row=0,
                                                                                                           column=6,
                                                                                                           padx=10)

        def pagar():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("Aviso", "Selecione um quarto!")
                return

            dados_q = tree.item(sel)['values']
            janela_pagamento(dados_q[0], ent_data.get(), spn_noit.get(), dados_q[5])

        Button(conteudo, text="Prosseguir para Pagamento", bg="#27ae60", fg="white",
               font=("Arial", 11, "bold"), command=pagar, height=2).pack(pady=10)

    def janela_pagamento(q_id, data_in, noites, valor_str):
        pop = Toplevel(root)
        pop.title("Finalizar Reserva")
        pop.geometry("350x300")

        valor = float(str(valor_str).replace('€', ''))

        Label(pop, text="DADOS DO PAGAMENTO", font=("Arial", 10, "bold")).pack(pady=10)
        Label(pop, text=f"Total a pagar: {valor}€", fg="blue").pack()

        Label(pop, text="Nome do Titular:").pack(pady=(10, 0))
        e_titular = Entry(pop, width=30);
        e_titular.pack()

        Label(pop, text="Método:").pack(pady=(10, 0))
        cb_metodo = ttk.Combobox(pop, values=["Cartão", "MB Way", "Numerário"], state="readonly")
        cb_metodo.pack()

        def confirmar():
            if not e_titular.get() or not cb_metodo.get():
                messagebox.showerror("Erro", "Campos obrigatórios!")
                return

            try:
                # 1. Reserva
                f_adicionar_reserva(id_cliente_logado, q_id, data_in, f"{noites} noites", valor)

                # 2. Pagamento (Obter ID da reserva acabada de criar)
                conn = f_get_conn()
                res_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
                conn.close()
                f_adicionar_pagamento(res_id, datetime.now().strftime("%d/%m/%Y"), cb_metodo.get(), valor)

                messagebox.showinfo("Sucesso", "Reserva confirmada!")
                pop.destroy()
                aba_reservar()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        Button(pop, text="PAGAR AGORA", bg="#27ae60", fg="white", command=confirmar).pack(pady=20)

    # --- Menu Lateral ---
    Label(menu_lateral, text="PAINEL CLIENTE", fg="white", bg=cor_menu, font=("Arial", 14, "bold")).pack(pady=30)

    Button(menu_lateral, text="A Minha Conta", command=aba_perfil, bg="#34495e", fg="white", relief=FLAT,
           height=2).pack(fill=X, padx=10, pady=5)
    Button(menu_lateral, text="Reservar Quarto", command=aba_reservar, bg="#34495e", fg="white", relief=FLAT,
           height=2).pack(fill=X, padx=10, pady=5)

    Button(menu_lateral, text="Sair", command=root.destroy, bg="#e74c3c", fg="white", relief=FLAT).pack(side=BOTTOM,
                                                                                                        fill=X, padx=10,
                                                                                                        pady=20)

    aba_perfil()  # Inicia na conta
    root.mainloop()

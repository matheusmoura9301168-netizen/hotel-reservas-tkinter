# Funções de acesso à base de dados Hotel.db e validações.

import sqlite3
import re
DB = "Hotel.db"

def f_get_conn():
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def f_iniciar_cliente(email, senha):
    # Verificar campos vazios
    if not email or not senha:
        raise ValueError("Email e senha são obrigatórios.")

    conn = sqlite3.connect("Hotel.db")
    cursor = conn.cursor()

    # Verificar se o email existe
    cursor.execute("SELECT C_Senha FROM Cliente WHERE C_Email = ?", (email,))
    resultado = cursor.fetchone()

    if resultado is None:
        conn.close()
        raise ValueError("Email não encontrado.")

    senha_correta = resultado[0]

    # Verificar senha
    if senha != senha_correta:
        conn.close()
        raise ValueError("Senha incorreta.")

    conn.close()
    return True

def f_validar_nif(nif):
    return re.fullmatch(r"\d{9}", nif) is not None

def f_validar_nome(nome):
    return re.fullmatch(r"[A-Za-zÀ-ÿ\s]{3,50}", nome) is not None

def f_validar_preco(preco):
    return re.fullmatch(r"\d+(\.\d{1,2})?", preco) is not None

def f_validar_id(id_):
    return re.fullmatch(r"\d+", id_) is not None


def f_validate_nonempty(label, value):
    if value is None or str(value).strip() == "":
        raise ValueError(f"{label} é obrigatório.")

def f_validate_float(label, value):
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{label} deve ser numérico.")


def f_validate_int(label, value):
    try:
        return int(value)
    except (TypeError, ValueError):
        raise ValueError(f"{label} deve ser inteiro.")

def f_procurar_cliente(nome):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Cliente WHERE C_Nome LIKE ?", (f"%{nome}%",))
    data = c.fetchall()
    conn.close()
    return data

def f_adicionar_cliente(nome, nif, email, telefone, senha):
    f_validate_nonempty("Nome", nome)
    f_validate_nonempty("nif", nif)
    f_validate_nonempty("telefone", telefone)
    f_validate_nonempty("Senha", senha)
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT INTO Cliente (C_Nome, C_NIF, C_Email, C_Telefone, C_Senha)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, nif, email, telefone, senha))
    conn.commit()
    conn.close()

def f_ver_cliente_admin(email):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("SELECT C_Admin FROM Cliente WHERE C_Email LIKE ?", (f"%{email}%",))
    data = c.fetchone()
    conn.close()
    if data == 0:
        return 0
    else:
        return 1

def f_listar_clientes():
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Cliente")
    data = c.fetchall()
    conn.close()
    return data


def f_procurar_cliente_id(email):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("SELECT C_ID_Cliente FROM Cliente WHERE C_Email LIKE ?", (f"%{email}%",))
    data = c.fetchone()
    conn.close()
    return data


def f_atualizar_cliente(cid, nome, email, telefone):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        UPDATE Cliente
        SET C_Nome = ?, C_Email = ?, C_Telefone = ?
        WHERE C_ID_Cliente = ?
    """, (nome, email, telefone, cid))
    conn.commit()
    conn.close()


def f_remover_cliente(cid):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM Cliente WHERE C_ID_Cliente = ?", (cid,))
    conn.commit()
    conn.close()



def f_adicionar_quarto(endereco, tipo, capacidade, valor_noite, valor_pessoa):
    f_validate_nonempty("Endereço", endereco)

    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT INTO Quarto (Q_Endereco, Q_Tipo, Q_Capacidade, Q_Valor_Por_Noite, Q_Valor_Por_Pessoa)
        VALUES (?, ?, ?, ?, ?)
    """, (endereco, tipo, capacidade, valor_noite, valor_pessoa))
    conn.commit()
    conn.close()


def f_listar_quartos():
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Quarto")
    data = c.fetchall()
    conn.close()
    return data


def f_atualizar_quarto(qid, tipo, capacidade, valor_noite, valor_pessoa, status):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        UPDATE Quarto
        SET Q_Tipo = ?, Q_Capacidade = ?, Q_Valor_Por_Noite = ?,
            Q_Valor_Por_Pessoa = ?, Q_Status = ?
        WHERE Q_ID_Quarto = ?
    """, (tipo, capacidade, valor_noite, valor_pessoa, status, qid))
    conn.commit()
    conn.close()


def f_remover_quarto(qid):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM Quarto WHERE Q_ID_Quarto = ?", (qid,))
    conn.commit()
    conn.close()



def f_adicionar_reserva(cliente_id, quarto_id, checkin, checkout, valor_total):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT INTO Reserva (R_ID_Cliente, R_ID_Quarto, R_Data_Checkin, R_Data_Checkout, R_Valor_Total)
        VALUES (?, ?, ?, ?, ?)
    """, (cliente_id, quarto_id, checkin, checkout, valor_total))
    conn.commit()
    conn.close()


def f_listar_reservas():
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        SELECT r.R_ID_Reserva, c.C_Nome, q.Q_Endereco, r.R_Data_Checkin,
               r.R_Data_Checkout, r.R_Valor_Total, r.R_Status
        FROM Reserva r
        JOIN Cliente c ON c.C_ID_Cliente = r.R_ID_Cliente
        JOIN Quarto q ON q.Q_ID_Quarto = r.R_ID_Quarto
    """)
    data = c.fetchall()
    conn.close()
    return data


def f_atualizar_reserva(rid, checkin, checkout, valor_total, status):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        UPDATE Reserva
        SET R_Data_Checkin = ?, R_Data_Checkout = ?, R_Valor_Total = ?, R_Status = ?
        WHERE R_ID_Reserva = ?
    """, (checkin, checkout, valor_total, status, rid))
    conn.commit()
    conn.close()


def f_remover_reserva(rid):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM Reserva WHERE R_ID_Reserva = ?", (rid,))
    conn.commit()
    conn.close()



def f_adicionar_pagamento(reserva_id, data, metodo, valor):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT INTO Pagamento (P_ID_Reserva, P_Data_Pagamento, P_Metodo, P_Valor_Pago)
        VALUES (?, ?, ?, ?)
    """, (reserva_id, data, metodo, valor))
    conn.commit()
    conn.close()


def f_listar_pagamentos():
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        SELECT p.P_ID_Pagamento, r.R_ID_Reserva, p.P_Data_Pagamento,
               p.P_Metodo, p.P_Valor_Pago, p.P_Status
        FROM Pagamento p
        JOIN Reserva r ON r.R_ID_Reserva = p.P_ID_Reserva
    """)
    data = c.fetchall()
    conn.close()
    return data


def f_atualizar_pagamento(pid, metodo, valor, status):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        UPDATE Pagamento
        SET P_Metodo = ?, P_Valor_Pago = ?, P_Status = ?
        WHERE P_ID_Pagamento = ?
    """, (metodo, valor, status, pid))
    conn.commit()
    conn.close()


def f_remover_pagamento(pid):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM Pagamento WHERE P_ID_Pagamento = ?", (pid,))
    conn.commit()
    conn.close()



def f_adicionar_funcionario(nome, cargo, email, telefone, data_contratacao, ordenado):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT INTO Funcionario (F_Nome, F_Cargo, F_Email, F_Telefone, F_Data_Contratacao, F_Ordenado)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, cargo, email, telefone, data_contratacao, ordenado))
    conn.commit()
    conn.close()


def f_listar_funcionarios():
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Funcionario")
    data = c.fetchall()
    conn.close()
    return data


def f_atualizar_funcionario(fid, cargo, telefone, ordenado):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        UPDATE Funcionario
        SET F_Cargo = ?, F_Telefone = ?, F_Ordenado = ?
        WHERE F_ID_Funcionario = ?
    """, (cargo, telefone, ordenado, fid))
    conn.commit()
    conn.close()


def f_remover_funcionario(fid):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM Funcionario WHERE F_ID_Funcionario = ?", (fid,))
    conn.commit()
    conn.close()


def f_adicionar_manutencao(quarto_id, funcionario_id, descricao, inicio, fim, responsavel):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT INTO Manutencao (M_ID_Quarto, M_ID_Funcionario, M_Descricao, M_Data_Inicio, M_Data_Fim, M_Responsavel)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (quarto_id, funcionario_id, descricao, inicio, fim, responsavel))
    conn.commit()
    conn.close()


def f_listar_manutencoes():
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
        SELECT m.M_ID_Manutencao, q.Q_Endereco, f.F_Nome, m.M_Descricao,
               m.M_Data_Inicio, m.M_Data_Fim, m.M_Responsavel
        FROM Manutencao m
        JOIN Quarto q ON q.Q_ID_Quarto = m.M_ID_Quarto
        JOIN Funcionario f ON f.F_ID_Funcionario = m.M_ID_Funcionario
    """)
    data = c.fetchall()
    conn.close()
    return data


def f_remover_manutencao(mid):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM Manutencao WHERE M_ID_Manutencao = ?", (mid,))
    conn.commit()
    conn.close()

def f_admin(cid, adm):
    conn = f_get_conn()
    c = conn.cursor()
    c.execute("""
         UPDATE Cliente
         SET C_Admin = ?
         WHERE C_ID_Cliente = ?
     """, (adm, cid))
    conn.commit()
    conn.close()

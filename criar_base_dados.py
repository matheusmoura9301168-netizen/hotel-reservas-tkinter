# Cria a base de dados Hotel.db com todas as tabelas.

import sqlite3

conn = sqlite3.connect("Hotel.db")
cursor = conn.cursor()

# Cliente
cursor.execute("""
CREATE TABLE IF NOT EXISTS Cliente (
    C_ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    C_Nome TEXT NOT NULL,
    C_NIF TEXT UNIQUE,
    C_Email TEXT UNIQUE,
    C_Telefone TEXT,
    C_Senha TEXT,
    C_Data_Cadastro TEXT DEFAULT (datetime('now')),
    C_Admin BOOLEAN DEFAULT 0
)
""")

# Quarto
cursor.execute("""
CREATE TABLE IF NOT EXISTS Quarto (
    Q_ID_Quarto INTEGER PRIMARY KEY AUTOINCREMENT,
    Q_Endereco TEXT UNIQUE,
    Q_Tipo TEXT,
    Q_Capacidade INTEGER,
    Q_Valor_Por_Noite REAL,
    Q_Valor_Por_Pessoa REAL,
    Q_Status BOOLEAN DEFAULT 0
)
""")

# Reserva
cursor.execute("""
CREATE TABLE IF NOT EXISTS Reserva (
    R_ID_Reserva INTEGER PRIMARY KEY AUTOINCREMENT,
    R_ID_Cliente INTEGER,
    R_ID_Quarto INTEGER,
    R_Data_Checkin TEXT,
    R_Data_Checkout TEXT,
    R_Valor_Total REAL,
    R_Status TEXT DEFAULT 'ativa',
    FOREIGN KEY(R_ID_Cliente) REFERENCES Cliente(C_ID_Cliente),
    FOREIGN KEY(R_ID_Quarto) REFERENCES Quarto(Q_ID_Quarto)
)
""")

# Pagamento
cursor.execute("""
CREATE TABLE IF NOT EXISTS Pagamento (
    P_ID_Pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
    P_ID_Reserva INTEGER,
    P_Data_Pagamento TEXT,
    P_Metodo TEXT,
    P_Valor_Pago REAL,
    P_Status TEXT DEFAULT 'pendente',
    FOREIGN KEY(P_ID_Reserva) REFERENCES Reserva(R_ID_Reserva)
)
""")

# Funcionario
cursor.execute("""
CREATE TABLE IF NOT EXISTS Funcionario (
    F_ID_Funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
    F_Nome TEXT,
    F_Cargo TEXT,
    F_Email TEXT UNIQUE,
    F_Telefone TEXT,
    F_Data_Contratacao TEXT,
    F_Ordenado REAL
)
""")

# Manutencao
cursor.execute("""
CREATE TABLE IF NOT EXISTS Manutencao (
    M_ID_Manutencao INTEGER PRIMARY KEY AUTOINCREMENT,
    M_ID_Quarto INTEGER,
    M_ID_Funcionario INTEGER,
    M_Descricao TEXT,
    M_Data_Inicio TEXT,
    M_Data_Fim TEXT,
    M_Responsavel TEXT,
    FOREIGN KEY(M_ID_Quarto) REFERENCES Quarto(Q_ID_Quarto),
    FOREIGN KEY(M_ID_Funcionario) REFERENCES Funcionario(F_ID_Funcionario)
)
""")

conn.commit()
conn.close()

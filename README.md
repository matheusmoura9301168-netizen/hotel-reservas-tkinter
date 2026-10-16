# Sistema de Reservas de Hotel

Aplicação em Python (Tkinter + SQLite) para gerir um hotel, com uma área para clientes e outra para administração.

## Funcionalidades

**Clientes**
- Criar conta e iniciar sessão (com validação de NIF e telefone)
- Consultar quartos e fazer reservas

**Administração**
- Gestão de clientes, quartos e reservas
- Pagamentos
- Funcionários e manutenção dos quartos
- Atribuir permissões de administrador

## Como executar

```bash
python criar_base_dados.py   # cria o ficheiro Hotel.db
python main.py
```

## Ficheiros

| Ficheiro | O que faz |
|---|---|
| `main.py` | Ecrã inicial para iniciar sessão ou criar conta |
| `layout_cliente.py` | Interface da área do cliente |
| `layout_admin.py` | Painel de administração |
| `funcoes.py` | Funções de acesso à base de dados e validações |
| `criar_base_dados.py` | Cria as tabelas (Cliente, Quarto, Reserva, Pagamento, Funcionário, Manutenção) |

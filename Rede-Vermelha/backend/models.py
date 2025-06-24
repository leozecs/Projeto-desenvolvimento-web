import sqlite3
import os

DB_PATH = 'database.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Cria a tabela com UNIQUE(nome, email) para evitar duplicatas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            genero TEXT NOT NULL,
            cpf_rg TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            estado TEXT NOT NULL,
            cidade TEXT NOT NULL,
            cep TEXT NOT NULL,
            tipo_sanguineo TEXT NOT NULL,
            doacoes_anteriores TEXT NOT NULL,
            medicacao TEXT,
            detalhe_medicacao TEXT,
            doenca TEXT NOT NULL,
            qual_doenca TEXT,
            aceitou_termos INTEGER NOT NULL,
            data_envio TEXT NOT NULL,
            UNIQUE(nome, email)
        )
    ''')

    conn.commit()
    conn.close()
    print(f"[DB] Banco de dados '{DB_PATH}' verificado e pronto.")

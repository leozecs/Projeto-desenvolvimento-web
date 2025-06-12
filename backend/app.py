from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
from datetime import datetime
from models import init_db
import traceback
import os

# ==========================================
# Inicialização do app Flask
# ==========================================
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)
init_db()

# ==========================================
# Conexão com banco de dados SQLite
# ==========================================
def conectar():
    return sqlite3.connect('database.db')

# ==========================================
# Validação de campos obrigatórios
# ==========================================
def validar_doador(data):
    obrigatorios = [
        'nome', 'data_nascimento', 'genero', 'cpf_rg', 'email', 'telefone',
        'estado', 'cidade', 'cep', 'tipo_sanguineo', 'doacao_anteriores',
        'medicacao', 'doenca', 'termos'
    ]

    erros = []
    for campo in obrigatorios:
        if campo not in data or str(data[campo]).strip() == '':
            erros.append(f"Campo obrigatório ausente ou vazio: {campo}")

    if 'email' in data and '@' not in data['email']:
        erros.append("E-mail inválido")
    if 'cpf_rg' in data and len(data['cpf_rg']) < 5:
        erros.append("CPF/RG inválido")

    return erros

# ==========================================
# Rota: Servir o frontend (index.html)
# ==========================================
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# ==========================================
# Rota: Servir arquivos estáticos
# ==========================================
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

# ==========================================
# Rota: Status da API
# ==========================================
@app.route('/api')
def api_info():
    return jsonify({
        'mensagem': 'API Rede Vermelha Online',
        'endpoints': {
            'listar': '/api/doadores',
            'cadastrar': '/api/doadores (POST)',
            'buscar_por_id': '/api/doadores/<id>',
            'deletar': '/api/doadores/<id> (DELETE)'
        }
    })

# ==========================================
# Rota: Cadastrar novo doador
# ==========================================
@app.route('/api/doadores', methods=['POST'])
def cadastrar():
    data = request.json
    erros = validar_doador(data)

    if erros:
        return jsonify({'erros': erros}), 400

    try:
        conn = conectar()
        cursor = conn.cursor()

        # 🔎 Verificação de duplicata por nome e email
        cursor.execute('SELECT * FROM doadores WHERE LOWER(nome) = LOWER(?) AND LOWER(email) = LOWER(?)',
                       (data['nome'].strip(), data['email'].strip()))
        existente = cursor.fetchone()

        if existente:
            return jsonify({
                'erro': f"Olá {data['nome'].strip()}, você já realizou o cadastro para doação."
            }), 409  # 409 Conflict

        # 📝 Inserção no banco
        cursor.execute('''
            INSERT INTO doadores (
                nome, data_nascimento, genero, cpf_rg, email, telefone,
                estado, cidade, cep, tipo_sanguineo, doacoes_anteriores,
                medicacao, detalhe_medicacao, doenca, qual_doenca,
                aceitou_termos, data_envio
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['nome'].strip(),
            data['data_nascimento'].strip(),
            data['genero'].strip(),
            data['cpf_rg'].strip(),
            data['email'].strip(),
            data['telefone'].strip(),
            data['estado'].strip(),
            data['cidade'].strip(),
            data['cep'].strip(),
            data['tipo_sanguineo'].strip(),
            data['doacao_anteriores'].strip(),
            data['medicacao'].strip(),
            data.get('detalhe_medicacao', '').strip(),
            data['doenca'].strip(),
            data.get('qual_doenca', '').strip(),
            int(data['termos']),
            datetime.now().isoformat()
        ))

        conn.commit()
        conn.close()

        print(f"[API] Novo doador cadastrado: {data['nome']}")
        return jsonify({'mensagem': 'Cadastro realizado com sucesso!'}), 201

    except Exception as e:
        traceback.print_exc()
        return jsonify({'erro': 'Erro interno ao salvar doador.'}), 500

# ==========================================
# Rota: Listar todos os doadores
# ==========================================
@app.route('/api/doadores', methods=['GET'])
def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM doadores')
    colunas = [desc[0] for desc in cursor.description]
    resultados = cursor.fetchall()
    doadores = [dict(zip(colunas, linha)) for linha in resultados]
    conn.close()

    print(f"[API] {len(doadores)} doadores retornados")
    return jsonify(doadores)

# ==========================================
# Rota: Buscar doador por ID
# ==========================================
@app.route('/api/doadores/<int:id>', methods=['GET'])
def buscar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM doadores WHERE id = ?', (id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        colunas = [desc[0] for desc in cursor.description]
        return jsonify(dict(zip(colunas, row)))

    return jsonify({'erro': 'Doador não encontrado'}), 404

# ==========================================
# Rota: Deletar doador por ID
# ==========================================
@app.route('/api/doadores/<int:id>', methods=['DELETE'])
def deletar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM doadores WHERE id = ?', (id,))
    conn.commit()
    afetadas = cursor.rowcount
    conn.close()

    if afetadas == 0:
        return jsonify({'erro': 'Doador não encontrado'}), 404

    print(f"[API] Doador ID {id} removido com sucesso")
    return jsonify({'mensagem': f'Doador ID {id} removido com sucesso.'}), 200

# ==========================================
# Inicialização do servidor
# ==========================================
if __name__ == '__main__':
    app.run(debug=True)

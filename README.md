# 🩸 Rede Vermelha – Backend

Este repositório contém o servidor **backend em Flask** do projeto **Rede Vermelha**, desenvolvido para a disciplina **ARA0062 - Desenvolvimento Web**.

O sistema gerencia o **cadastro de doadores de sangue**, com persistência em banco de dados SQLite e comunicação assíncrona com o frontend via API REST.

---

## 👥 Participantes

- **Leonardo Rodrigues Tavares** – 202302535976  
- **Maria Eduarda dos Santos Jorge** – 202402395271

---

## 🧱 Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask-CORS (integração com frontend)
- SQLite (banco de dados local)
- JavaScript (fetch API no frontend)

---

## 📁 Estrutura do Projeto

```
backend/
├── app.py            # Servidor Flask e rotas da API
├── models.py         # Criação da tabela 'doadores' no SQLite
├── database.db       # Banco de dados gerado automaticamente
├── requirements.txt  # Lista de dependências do projeto
└── README.md         # Documentação (este arquivo)
```

---

## 🚀 Como executar o backend localmente

```bash
# 1. Clone o projeto
git clone https://github.com/1606200617/Projeto-desenvolvimento-web.git
cd backend

# 2. Crie e ative o ambiente virtual
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie o servidor
python app.py
```

O backend estará disponível em: **http://localhost:5000**

---

## 📦 Banco de Dados

O arquivo `database.db` será criado automaticamente ao iniciar o app, contendo a tabela `doadores` com todos os campos definidos no `models.py`.

> ✅ Agora inclui uma **constraint `UNIQUE(nome, email)`** para evitar cadastros duplicados.

---

## 🌐 Integração com o Frontend

Este backend é consumido pelo frontend SPA hospedado via GitHub Pages:  
🔗 [Frontend - Rede Vermelha](https://github.com/1606200617/Projeto-desenvolvimento-web/tree/main/frontend)

---

## 📎 Links úteis

- 🎨 [Design Figma](#)(https://www.figma.com/design/s2taholiw9xc05JfWIFhXR/Untitled?node-id=0-1&p=f&t=bpma0OlpjltWADNR-0)
- 📚 [Documentação Flask](https://flask.palletsprojects.com/)
- 📘 [W3C HTML Validator](https://validator.w3.org/)

---

## 📄 Licença

Projeto acadêmico desenvolvido para a disciplina Desenv. Web em HTML5, Css, Javascript e Php.  
Distribuição e uso livre com os devidos créditos aos autores.

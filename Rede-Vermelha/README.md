# 🩸 Rede Vermelha – Backend

Este repositório contém o **servidor backend em Flask** do projeto **Rede Vermelha**, desenvolvido para a disciplina **ARA0062 - Desenvolvimento Web**. O sistema gerencia o cadastro de doadores de sangue, com persistência em banco de dados SQLite e comunicação assíncrona com o frontend.

---

## 👥 Participantes

- Leonardo Rodrigues Tavares – 202302535976  
- Maria Eduarda dos Santos Jorge – 202402395271

---

## 💡 Objetivo

Oferecer uma **API RESTful** que permita:

- Cadastrar doadores via formulário (POST)
- Listar todos os doadores (GET)
- Consultar um doador específico (GET com ID)
- Remover doadores (DELETE)

---

## 🧱 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) – integração com frontend
- [JavaScript (fetch)](https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API) – no frontend

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

### 1. Clone o projeto
```bash
git clone https://github.com/1606200617/Projeto-desenvolvimento-web.git
cd backend
```

### 2. Crie e ative o ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\\Scripts\\activate    # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o servidor Flask
```bash
python app.py
```

O backend estará disponível em: `http://localhost:5000`

---

## 📡 Endpoints da API

| Método | Endpoint              | Descrição                    |
|--------|-----------------------|------------------------------|
| POST   | `/api/doadores`       | Cadastrar novo doador        |
| GET    | `/api/doadores`       | Listar todos os doadores     |
| GET    | `/api/doadores/<id>`  | Obter um doador por ID       |
| DELETE | `/api/doadores/<id>`  | Remover um doador por ID     |

---

## ✅ Campos esperados na requisição (POST)

- `nome`: string (obrigatório)
- `data_nascimento`: string (obrigatório)
- `genero`: string (obrigatório)
- `cpf_rg`: string (obrigatório)
- `email`: string (obrigatório)
- `telefone`: string (obrigatório)
- `estado`: string (obrigatório)
- `cidade`: string (obrigatório)
- `cep`: string (obrigatório)
- `tipo_sanguineo`: string (obrigatório)
- `doacao_anteriores`: string (obrigatório)
- `medicacao`: string (opcional)
- `doenca`: string (obrigatório)
- `qual_doenca`: string (opcional)
- `termos`: 0 ou 1 (obrigatório – booleano)
- `data_envio`: gerado automaticamente no backend

---

## 📦 Banco de Dados

O arquivo `database.db` será criado automaticamente ao iniciar o app, contendo a tabela `doadores` com os campos definidos no `models.py`.

---

## 🌐 Integração com Frontend

Este backend foi desenvolvido para ser consumido pelo frontend hospedado via GitHub Pages, disponível no repositório:
[Frontend - Rede Vermelha](https://github.com/1606200617/Projeto-desenvolvimento-web)

---

## 📎 Links importantes

- 🎨 [Design Figma](https://www.figma.com/design/s2taholiw9xc05JfWIFhXR/Untitled?node-id=0-1&m=dev&t=y9lTSJYdCDIuvbYM-1)
- 📚 Documentação Flask: https://flask.palletsprojects.com/
- 📘 Validator W3C: https://validator.w3.org/

---

## 📄 Licença

Projeto acadêmico. Uso livre com atribuição aos autores.

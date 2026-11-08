# Estrutura inicial do projeto

## Stack escolhida

A melhor opção para iniciar neste momento é:

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Docker (opcional)

### Por quê?

Essa stack combina bem com o perfil profissional atual:

- Python e SQL: fortemente alinhados com dados e BI
- FastAPI: rápido para criar APIs REST
- PostgreSQL: excelente para projetos de backend e dados
- SQLAlchemy: facilita a camada de persistência
- Estrutura simples: ideal para evoluir em projetos reais

## Estrutura criada

```text
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── health.py
│   └── core/
│       ├── __init__.py
│       └── config.py
├── .gitignore
├── requirements.txt
├── README_PROJECT.md
└── .env.example
```

## Como rodar

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou .venv\Scripts\activate  # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints iniciais

- `/` — mensagem inicial
- `/api/health` — verificação de serviço
- `/api/projects` — lista de projetos de exemplo

## Próximos passos sugeridos

1. Adicionar autenticação
2. Integrar banco PostgreSQL
3. Criar modelos de dados
4. Implementar CRUD
5. Adicionar testes automatizados
6. Deploy em render, railway ou heroku

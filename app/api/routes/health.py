from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["health"])
def health_check():
    return {
        "status": "ok",
        "service": "portfolio-api",
        "message": "API em execução com sucesso.",
    }


@router.get("/projects", tags=["projects"])
def list_projects():
    return {
        "projects": [
            {
                "name": "Dashboard de BI",
                "category": "Business Intelligence",
                "tech": ["Python", "Streamlit", "Pandas"],
            },
            {
                "name": "API de Cadastro",
                "category": "Backend",
                "tech": ["FastAPI", "SQLAlchemy", "PostgreSQL"],
            },
            {
                "name": "Sistema de Segurança",
                "category": "Cibersegurança",
                "tech": ["Python", "Segurança", "Monitoramento"],
            },
        ]
    }

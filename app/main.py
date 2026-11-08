from fastapi import FastAPI
from app.api.routes.health import router as health_router

app = FastAPI(
    title="Maristela Costa Portfolio API",
    description="API inicial para projetos em dados, BI, backend e segurança da informação.",
    version="0.1.0",
)

app.include_router(health_router, prefix="/api")


@app.get("/")
def read_root():
    return {
        "message": "Bem-vindo(a) ao projeto inicial de Maristela Costa.",
        "status": "online",
        "stack": "Python + FastAPI",
    }

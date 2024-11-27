from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import shutdown_db, startup_db
from routers.termos import router as termos_router

app = FastAPI(title='SITE MATEMATICA')


# Inicialização e fechamento do banco de dados
app.add_event_handler("startup", startup_db)
app.add_event_handler("shutdown", shutdown_db)

# Middleware CORS para permitir conexões de outros domínios
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota para verificar status da API
@app.get("/")
def status():
    return {"message": "Hello World"}

app.include_router(termos_router)
from pydantic import BaseModel

class TermoCreate(BaseModel):
    termo_nome: str
    termo_conteudo: str

class TermoRead(BaseModel):
    id_termo: int
    termo_nome: str
    termo_conteudo: str

class TermoUpdate(BaseModel):
    termo_nome: str
    termo_conteudo: str

class TermoReadMany(BaseModel):
    termos: list[TermoRead]

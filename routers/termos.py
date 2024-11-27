from fastapi import APIRouter, HTTPException
from models.termos import TermoDB
from schemas.termos import (
    TermoCreate,
    TermoRead,
    TermoReadMany,
    TermoUpdate
)

router = APIRouter(prefix='/termos', tags=['TERMOS'])

@router.post('', response_model=TermoRead)
def criar_cultura(nova_cultura: TermoCreate):
    termo = TermoDB.create(**nova_cultura.dict())
    return termo

@router.get('', response_model=TermoReadMany)
def listar_culturas():
    termos = TermoDB.select()
    return {'termos': termos}

@router.get('/{cultura_id}', response_model=TermoRead)
def listar_cultura(termo_id: int):
    termo = TermoDB.get_or_none(TermoDB.id_termo == termo_id)
    if not termo:
        raise HTTPException(status_code=404, detail="Termo não encontrada")
    return termo

@router.patch('/{cultura_id}', response_model=TermoRead)
def atualizar_cultura(termo_id: int, termo_atualizado: TermoUpdate):
    termo = TermoDB.get_or_none(TermoDB.id_termo == termo_id)
    if not termo:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")

    termo.termo_nome = termo_atualizado.nome_cultura or termo.nome_cultura
    termo.save()
    termo
@router.delete('/{cultura_id}', response_model=dict)
def excluir_cultura(termo_id: int):
    termo = TermoDB.get_or_none(TermoDB.id_cultura == termo_id)
    if not termo:
        raise HTTPException(status_code=404, detail="Termo não encontrada")

    termo.delete_instance()
    return {'message': 'Termo excluída com sucesso'}

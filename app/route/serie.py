from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.serie import SerieModel
from app.schema.serie import SerieSchema

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/series")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

@serie.patch("/update")
async def atualizar_series(id:int, titulo: str,descricao: str, ano_lancamento:int, db: Session = Depends(get_db)):
    resultados = {"titulo": titulo, "descricao": descricao, "ano_lancamento": ano_lancamento}   
    db.commit()
    db.refresh(resultados)
    return resultados
    

@serie.delete("/deletar/{id}")
async def deletar_series(id:int, db: Session = Depends(get_db)):
    id = db.query(SerieModel).filter(SerieModel.id == id).first()

    if not id:
        return("nao tem ID")
    db.delete(id)
    db.commit()
    return("deletado")
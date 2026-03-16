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

@serie.put("/update/")
async def atualizar_serie(id: int, dados: SerieSchema, db: Session = Depends(get_db)):
    serie = db.query(SerieModel).filter(SerieModel.id == id).first()
    if not serie:
        return ("Série não encontrada")

    db.query(SerieModel).filter(SerieModel.id == id).update(dados.model_dump(exclude_unset=True))
    db.commit()
    return (dados)


@serie.delete("/deletar/")
async def deletar_series(id:int, db: Session = Depends(get_db)):
    id = db.query(SerieModel).filter(SerieModel.id == id).first()

    if not id:
        return("nao tem ID")
    db.delete(id)
    db.commit()
    return("deletado")
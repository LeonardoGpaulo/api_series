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

# @serie.put("/update/")
# async def atualizar_serie(id: int, dados: SerieSchema, db: Session = Depends(get_db)):
#     serie = db.query(SerieModel).filter(SerieModel.id == id).first()
#     if not serie:
#         return ("Série não encontrada")

#     db.query(SerieModel).filter(SerieModel.id == id).update(dados.model_dump(exclude_unset=True))
#     db.commit()
#     return (dados)

@serie.put("/serie/{id}/update")
async def atualizar_serie(id: int, dados: SerieSchema, db: Session = Depends(get_db)):

    #busca os dados no banco
    serie = db.query(SerieModel).filter(SerieModel.id == id).first()

    #verifica se existe
    if not serie:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"A série com ID {id} não foi eencontrada"
        )
    
    # Atualiza os campos com os novos dados
    for campo, valor in dados.model_dump().items():
        setattr(serie, campo, valor)

    db.commit()
    db.refresh(serie)
    return serie


@serie.delete("/serie/{id}/delete")
async def deletar_series(id:int, db: Session = Depends(get_db)):
    id = db.query(SerieModel).filter(SerieModel.id == id).first()

    if not id:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"A série com ID {id} não foi encontrada"
        )

    db.delete(id)
    db.commit()
    return("deletado")
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Coche
from database import engine
from database import Base
from dependencies import get_db
from pydantic import BaseModel

app = FastAPI()

class cocheCreate(BaseModel):
    matricula: str
    marca: str
    modelo: str
    

class cocheResponse(cocheCreate):

    class Config:
        orm_mode = True

@app.post("/coches/", response_model=cocheResponse)
async def create_coche(coche: cocheCreate, db: AsyncSession = Depends(get_db)):
    db_coche = Coche(**coche.dict())
    db.add(db_coche)
    await db.commit()
    await db.refresh(db_coche)
    return db_coche

@app.get("/coches/{coche_id}", response_model=cocheResponse)
async def read_coche(coche_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Coche).where(Coche.matricula == coche_id))
    coche = result.scalar_one_or_none()
    if not coche:
        raise HTTPException(status_code=404, detail="coche no encontrado")
    return coche

@app.get("/coches/", response_model=list[cocheResponse])
async def list_coches(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Coche))
    return result.scalars().all()

@app.put("/coches/{coche_id}", response_model=cocheResponse)
async def update_coche(coche_id: str, coche: cocheCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Coche).where(Coche.matricula == coche_id))
    db_coche = result.scalar_one_or_none()
    if not db_coche:
        raise HTTPException(status_code=404, detail="coche no encontrado")
    for key, value in coche.dict().items():
        setattr(db_coche, key, value)
    await db.commit()
    await db.refresh(db_coche)
    return db_coche

@app.delete("/coches/{coche_id}")
async def delete_coche(coche_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Coche).where(Coche.matricula == coche_id))
    coche = result.scalar_one_or_none()
    if not coche:
        raise HTTPException(status_code=404, detail="coche no encontrado")
    await db.delete(coche)
    await db.commit()
    return {"mensaje": "coche eliminado"}
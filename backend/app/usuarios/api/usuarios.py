from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.usuarios import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    tags=["usuarios"]
)

# Dependencies
def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()

@router.post("/usuarios/", response_model=schemas.Usuario)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario_by_username(db, username = usuario.usuario)

    if db_usuario:
        raise HTTPException(status_code=400, detail="Usuario ya se encuentra registrado")
    
    return crud.create_usuario(db, usuario)

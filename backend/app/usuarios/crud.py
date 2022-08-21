from sqlalchemy.orm import Session

from app.usuarios import models, schemas


def get_usuario_by_id(db: Session, id_usuario: int):
    return db.query(models.Usuarios).filter(models.Usuarios == id_usuario).first()


def get_usuario_by_username(db: Session, username: str):
    return db.query(models.Usuarios).filter(models.Usuarios.usuario == username).first()


def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuarios).offset(skip).limit(limit).all()


def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    pwd_falsa = usuario.password + '1234'
    db_usuario = models.Usuarios(
        usuario=usuario.usuario,
        hashed_password=pwd_falsa,
        nombre=usuario.nombre,
        aPaterno = usuario.aPaterno,
        aMaterno = usuario.aMaterno)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

from pydantic import BaseModel


class UsuarioBase(BaseModel):
    nombre: str | None = None
    aPaterno: str | None = None
    aMaterno: str | None = None
    email: str | None = None
    cargo: str | None = None


class UsuarioCreate(UsuarioBase):
    usuario: str
    password: str
    nivel_acceso: int


class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True

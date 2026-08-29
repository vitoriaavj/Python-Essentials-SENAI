from fastapi import APIRouter

from database import SessionLocal

from controllers.pessoa_controller import PessoaController
from schemas.pessoa_schema import PessoaSchema

router = APIRouter(
    prefix="/pessoa",
    tags=["Pessoa"]
)

controle_rota = PessoaController()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar():
    db = next(get_db())

    return controle_rota.listar_controle_listar_pessoa(db)

@router.get("/{id}")
def listar_id(id: int):
    db = next(get_db())

    return controle_rota.listar_controle_listar_pessoa_id(db, id)

@router.post("/")
def listar_id(pessoa: PessoaSchema):
    db = next(get_db())

    return controle_rota.cadastrar_controle_pessoa(db, pessoa)

@router.put("/{id}")
def listar_id(id:int, pessoa: PessoaSchema):
    db = next(get_db())

    return controle_rota.alterar_controle_pessoa(db, id, pessoa)


@router.delete("/{id}")
def listar_id(id:int):
    db = next(get_db())

    return controle_rota.excluir_controle_pessoa(db, id)
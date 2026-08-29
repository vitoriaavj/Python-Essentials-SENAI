from pydantic import BaseModel
from datetime import date

class PessoaSchema(BaseModel):
    nome: str
    data_nascimento: date
    peso: float
    altura: float



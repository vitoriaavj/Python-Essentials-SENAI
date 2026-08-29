from sqlalchemy.orm import Session
from models.pessoa_model import PessoaModel

class PessoaRepository:
    #FUNÇÃO PARA LISTAR AS PESSOAS  
    def listar_pessoa(self, db: Session):
        return db.query(PessoaModel).all()

    #FUNÇÃO PARA LISTAR POR ID
    def listar_pessoa_id(self, db: Session, id: int):
        return db.query(PessoaModel).filter(PessoaModel.idpessoas == id).first()

    #FUNÇÃO PARA CADASTRAR PESSOA
    def cadastrar_pessoa(self, db: Session, pessoa):
        nova_pessoa = PessoaModel(
            nome = pessoa.nome,
            data_nascimento = pessoa.data_nascimento,
            peso = pessoa.peso,
            altura = pessoa.altura
        )

        db.add(nova_pessoa)
        db.commit()
        db.refresh(nova_pessoa)

        return nova_pessoa

    #FUNÇÃO PARA ALTERAR UMA PESSOA 
    def alterar_pessoa(self, db: Session, id: int, pessoa ):
        pessoa_model_db = self.listar_pessoa_id(db, id)

        pessoa_model_db.nome = pessoa.nome
        pessoa_model_db.data_nascimento = pessoa.data_nascimento
        pessoa_model_db.peso = pessoa.peso
        pessoa_model_db.altura = pessoa.altura

        db.commit()
        db.refresh(pessoa_model_db)

        return pessoa_model_db

    #FUNÇÃO PARA EXCLUIR
    def excluir_pessoa(self, db: Session, id: int):
        pessoa_model_db = self.listar_pessoa_id(db, id)

        db.delete(pessoa_model_db)
        db.commit()

        return {"Mensagem": "Pessoa Excluída!!!!"}
        
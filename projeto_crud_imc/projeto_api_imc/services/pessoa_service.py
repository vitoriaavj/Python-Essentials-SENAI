from repositories.pessoa_repository import PessoaRepository

class PessoaService:
    #MÉTODO CONSTRUTOR
    def __init__(self):
        self.repositorio = PessoaRepository()

    #FUNÇÃO SERVIÇO PARA LISTAR TODOS
    def listar_servico_pessoa(self, db):
        return self.repositorio.listar_pessoa(db)

    #FUNÇÃO SERVIÇO PARA LISTAR PELO ID
    def listar_servico_pessoa_id(self, db, id):
     
       return self.repositorio.listar_pessoa_id(db, id)
       

    #FUNÇÃO SERVIÇO PARA CADASTRAR
    def cadastrar_servico_pessoa(self, db, pessoa):
        if(pessoa != any ):
            return self.repositorio.cadastrar_pessoa(db, pessoa)
        else:
            return
       

    #FUNÇÃO SERVIÇO ALTERAR
    def alterar_servico_pessoa(self, db, id, pessoa):
        if(pessoa != any ):
            return self.repositorio.alterar_pessoa(db, id, pessoa)
        else:
            return

    #FUNÇÃO SERVIÇO EXCLUIR 
    def excluir_servico_pessoa(self, db, id):
        if(id > 0):
            return self.repositorio.excluir_pessoa(db, id)
        else:
            return


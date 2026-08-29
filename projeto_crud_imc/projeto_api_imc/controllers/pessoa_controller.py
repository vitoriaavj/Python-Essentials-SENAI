from services.pessoa_service import PessoaService

class PessoaController:
    #MÉTODO CONSTRUTOR
    def __init__(self):
        self.servico = PessoaService()

    #FUNÇÃO CONTROLE PARA LISTAR TODOS -  GET
    def listar_controle_listar_pessoa(self, db) :
        return self.servico.listar_servico_pessoa(db)

    #LISTAR CONTROLE PARA LISTAR PESSOA POR ID - GET
    def listar_controle_listar_pessoa_id(self, db, id):
        return self.servico.listar_servico_pessoa_id(db, id)

    #CADASTRAR CONTROLE PESSOA - POST
    def cadastrar_controle_pessoa(self, db, pessoa):
        return self.servico.cadastrar_servico_pessoa(db, pessoa)

    #ALTERAR CONTROLE PESSOA
    def alterar_controle_pessoa(self, db, id, pessoa):
        return self.servico.alterar_servico_pessoa(db, id, pessoa)

    #EXCLUIR CONTROLE PESSOA
    def excluir_controle_pessoa(self, db, id):
        return self.servico.excluir_servico_pessoa(db, id)
import {addPessoaApi, listarPessoaApi,  excluirPessoaApi, alterarPessoaApi } from './scripts_api.js'

/**PEGANDO ELEMENTOS DO DOM */
const formPessoa = document.querySelector('#form-pessoa')
const divLista = document.querySelector('#div-lista')

//DECLARANDO UM ARRAY
let pessoas = []

/*
//outra possibilidade de pegara elementos do dom
const formPessoa2 = document.getElementById('form-pessoa')
const divPessoa2 = document.getElementById('div-lista')
*/

/**CAPTURANDO EVENTO DO FORMULÁRIO */
formPessoa.addEventListener('submit', async (evt) => {
    //INTERROMPER A AÇÃO PADRÃO DE SUBMETER O FORMULÁRIO
    evt.preventDefault()

    //CRIANDO UM OBJETO DO FORMULÁRIO
    const dadosForm = new FormData(formPessoa)

    //CRIA UM OBJETO LITERAL DE PESSOA. DADO NO FORMATO json
    const pessoa = {
        idpessoas: 0,
        nome: dadosForm.get('nome'),
        data_nascimento: dadosForm.get('data-nascimento'),
        sexo: dadosForm.get('sexo'),
        altura: Number(dadosForm.get('altura')),
        peso: Number(dadosForm.get('peso'))
    }

    //ADICIONA O OBJETO LITERAL NO ARRAY
    //pessoas.push(pessoa)

    //ADICIONAR NA API
    const respotaApi = await addPessoaApi(pessoa)

    //CHAMA A FUNÇÃIO listarPessoas
    listarPessoas()

})

//FUNÇÃO PARA LISTAR PESSOAS NO ARRAY
const listarPessoas =  async () => {
    //LIMPA A DIV LISTA
    divLista.innerHTML = ''

    //CARREGAR ARRAY DADOS API
    pessoas = await listarPessoaApi()

    //PERCORRE O ARRAY pessoas
    pessoas.forEach((elem, i) => {
        /*divLista.innerHTML += elem.nome + elem.dataNascimento + elem.sexo + elem.altura + elem.peso*/
        //CONCATENAÇÃO TAMPLATE
        const divItemPessoa = document.createElement('div')
        divItemPessoa.setAttribute('class', 'div-pessoa')

        divItemPessoa.innerHTML += `<div class='div-pessoa'> ${elem.nome} ${elem.data_nascimento} ${elem.altura} ${elem.peso}</div>`

        const lnkAlterar = document.createElement('a')
        lnkAlterar.innerHTML = "A"
        lnkAlterar.setAttribute('href', '#')
        lnkAlterar.setAttribute('title', 'Alterar')
        lnkAlterar.setAttribute('alt', 'Alterar')
        lnkAlterar.addEventListener('click',(evt)=>{
            if(confirm(`Tem certeza que deseja alterar a pessoa `)){
                excluirPessoaApi(elem.idpessoas)
                window.location = '../index.html'
            }
        })

        const lnkExcluir = document.createElement('a')
        lnkExcluir.innerHTML = "E"
        lnkExcluir.setAttribute('href', '#')
        lnkExcluir.setAttribute('title', 'Excluir')
        lnkExcluir.setAttribute('alt', 'Excluir')
        lnkExcluir.addEventListener('click',(evt)=>{
            if(confirm(`Tem certeza que deseja excluir a pessoa `)){
                excluirPessoaApi(elem.idpessoas)
                window.location = '../index.html'
            }
        })

        divItemPessoa.appendChild(lnkAlterar)
        divItemPessoa.appendChild(lnkExcluir)

        divLista.appendChild(divItemPessoa)
    })
}

listarPessoas()


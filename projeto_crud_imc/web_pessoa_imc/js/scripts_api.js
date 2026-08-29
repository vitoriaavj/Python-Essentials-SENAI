//SALVAR PESSOA
const addPessoaApi = async (objPessoa) => {
    //const urlApi = `https://6a807072ec7a640e63abc47f.mockapi.io/imc/pessoa`
    const urlApi = `http://127.0.0.1:8000/pessoa/`

    console.log(objPessoa)

    try {
        const resposta = await fetch(
            urlApi, {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(objPessoa)
        }
        )

        if (!resposta.ok) {
            const txtErroResposta = await resposta.json()
            throw new Error(txtErroResposta)
        }

        const dadosResposta = await resposta.json()
        return dadosResposta

    } catch (erro) {
        console.log("Erro ao cadastrar A pessoa ", erro)
    }
}

//LISTAR PESSOAS
const listarPessoaApi = async () => {
    //const urlApi = `https://6a807072ec7a640e63abc47f.mockapi.io/imc/pessoa`
    const urlApi = `http://127.0.0.1:8000/pessoa/`

    try {
        return await fetch(urlApi)
            .then(resposta => resposta.json())
            .catch(erro => {
                return []
            })

    } catch (erro) {
        console.log("Erro ao consulta a pessoa ", erro)
    }
}

//EXCLUIR PESSOA
const excluirPessoaApi = async (idPessoa) => {
    //const urlApi = `https://6a807072ec7a640e63abc47f.mockapi.io/imc/pessoa/${idPessoa}`
    const urlApi = `http://127.0.0.1:8000/pessoa/${idPessoa}`

    try {
        const resposta = await fetch(
            urlApi, {
            method: 'DELETE',
            headers: { "Content-Type": "application/json" },
        }
        )

        if (!resposta.ok) {
            const txtErroResposta = await resposta.json()
            throw new Error(txtErroResposta)
        }

        const dadosResposta = await resposta.json()
        return dadosResposta

    } catch (erro) {
        console.log("Erro ao cadastrar A pessoa ", erro)
    }
}

//ALTERAR PESSOA
const alterarPessoaApi = async (objPessoa) => {
    //const urlApi = `https://6a807072ec7a640e63abc47f.mockapi.io/imc/pessoa/${objPessoa.idPessoa}`
    const urlApi = `http://127.0.0.1:8000/pessoa/${objPessoa.idPessoa}`

    try {
        const resposta = await fetch(
            urlApi, {
            method: 'PUT',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(objPessoa)
        }
        )

        if (!resposta.ok) {
            const txtErroResposta = await resposta.json()
            throw new Error(txtErroResposta)
        }

        const dadosResposta = await resposta.json()
        return dadosResposta

    } catch (erro) {
        console.log("Erro ao cadastrar A pessoa ", erro)
    }
}

export { addPessoaApi, listarPessoaApi, excluirPessoaApi, alterarPessoaApi }
import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print("\nInformações do CEP:")
            print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
            print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
            print(f"Estado: {dados.get('uf', 'Não disponível')}")
    except requests.RequestException:
        print("Erro na requisição.")

def menu_interativo():
    print("Consulta de CEP - ViaCEP")
    while True:
        cep = input("\nDigite o CEP (somente números) ou 'sair' para encerrar: ").strip()
        if cep.lower() == 'sair':
            print("Encerrando...")
            break
        elif len(cep) == 8 and cep.isdigit():
            consultar_cep(cep)
        else:
            print("CEP inválido.")

menu_interativo()

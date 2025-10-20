import requests


def buscar_usuario_ficticio():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    except requests.exceptions.RequestException:
        print("\n Falha na conexão com a API.")


def programa_interativo():
    while True:
        escolha = input("\nDeseja gerar um novo usuário? (s/n): ").strip().lower()
        if escolha == "s":
            buscar_usuario_ficticio()
        elif escolha == "n":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

programa_interativo()

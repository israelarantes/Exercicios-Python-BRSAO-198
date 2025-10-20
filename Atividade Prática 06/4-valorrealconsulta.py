import requests

while True:
    moeda = input("\nDigite o código da moeda (ex: USD, EUR, JPY) ou 'sair': ").strip().upper()
    if moeda == 'SAIR':
        print("Encerrando...")
        break

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        r = requests.get(url)
        dados = r.json()
        chave = moeda + 'BRL'

        if chave in dados:
            info = dados[chave]
            print(f"\n{moeda} → BRL")
            print(f"Valor atual: R$ {info['bid']}")
            print(f"Máxima: R$ {info['high']}")
            print(f"Mínima: R$ {info['low']}")
            print(f"Atualizado em: {info['create_date']}")
        else:
            print("Moeda não encontrada.")
    except:
        print("Erro na consulta.")
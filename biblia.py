# Importa as extensões necessarias
import requests
import textwrap
import time
from unidecode import unidecode 


# Faz com que o código seja executado infinitamente
while True:
    
    # Cria os inputs necesarios e com o strip() remove os espaços necessarios 
    nomeLivro = input("\nQual o livro? ").strip().lower()
    capitulo = int(input("\nQual o capitulo? ").strip())
    
    versiculoQuestion = input("\nQuer um versiculo especifico? [S/N] ").lower()

    # Faz uma verificação se o usúario quer procurar um versiculo especifico
    if versiculoQuestion == 'n':
        url = f"https://bible-api.com/{nomeLivro}+{capitulo}?translation=almeida"

    elif versiculoQuestion == 's':
        versiculo = int(input("\nQual versiculo? "))
        url = f"https://bible-api.com/{nomeLivro}+{capitulo}:{versiculo}?translation=almeida"

    # Chama a extensão "requests" para fazer uma requisição a variavel 'url' criada no if e então define a variavel 'data' como o resultado da requisição em .json
    response = requests.get(url)
    data = response.json()

    # Cria um loop que será executado até que todos os versiculos tenham sido printados
    for verse in data["verses"]:
        if verse['verse'] == 1:
            text = textwrap.fill(verse['text'], width=160)

            print(f"\n\n\n{verse['book_name']}, capitulo: {verse['chapter']}\n")
            print(f"\n{verse['chapter']}:{verse['verse']} - {text}\n")
        else:
            text = textwrap.fill(verse['text'], width=160)
            print(f"{verse['chapter']}:{verse['verse']} - {text}\n")

    # Pergunta se o usuario deseja outro versiculo/capitulo e se a resposta não for 's' finaliza o programa
    continuar = input("\nDeseja buscar outro versiculo/capitulo? [S/N] ").lower()
    if continuar != 's':
        print("\nAté logo!\n")
        time.sleep(5)
        break
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertou = 0
errou = 0  

for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']} \n')
    print('Opções:\n')
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
   
    resposta = int(input(f'\nEscolha uma opção: '))
    
    
    if opcoes[resposta] == pergunta['Resposta']:
        acertou += 1
        print('\n\nVocê acertou! 👍')
    else:
        errou +=1
        print('\nVocê errou! ❌\n' )
print('\n\n\n\n\n\n\nFIM DE JOGO\n')
print(f'Você acertou {acertou} perguntas de {len(perguntas)}\n\n\n\n\n\n')
        




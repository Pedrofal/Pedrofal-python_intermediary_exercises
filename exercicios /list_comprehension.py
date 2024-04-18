

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]



acrecimo_10_porcento = [
    {**produto , 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in produtos
    
    ]
   
produtos_ordonados_por_nome = sorted(acrecimo_10_porcento, key=lambda x: x['nome'])
produtos_ordonados_por_preco = sorted(acrecimo_10_porcento, key=lambda x: x['preco'])

print('\nProdutos originais: \n')
print(*produtos, sep='\n')
print('\nAcrecimo de 10%: \n')
print(*acrecimo_10_porcento, sep='\n')
print('\nProdutos ordenados por nome: \n')
print(*produtos_ordonados_por_nome, sep='\n')
print('\nProdutos ordenados por preço: \n')
print(*produtos_ordonados_por_preco, sep='\n')


cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

def unir_listas(lista1, lista2):
    tamanho_minimo = min(len(lista1), len(lista2))
    lista_unida = [(lista1[i], lista2[i]) for i in range(tamanho_minimo)]
    return lista_unida


cidades_e_estados = unir_listas(cidades,estados)
print(*cidades_e_estados, sep='\n')


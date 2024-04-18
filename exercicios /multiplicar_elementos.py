def multiplicacao(*args):
    total = 1
    for numero in args:
        total*= numero
    return total
mult = multiplicacao(9,4,5, 20, 39,39)

print(f' O total da multiplicação é {mult}')



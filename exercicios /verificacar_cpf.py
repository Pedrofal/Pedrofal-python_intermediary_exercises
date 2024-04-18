
def verificar_cpf(cpf):
    def verificar_primeiro_digito(cpf):
        digitos = []
        peso = list(range(10,-1,-1))
        multiplicacao = 0

        for digito in cpf:
            try:
                digitos.append(int(digito))
                
            except ValueError:
                continue 
        digitos = digitos[:-2]

        for i in range(len(digitos)):
            multiplicacao += digitos[i] * peso[i]

        primeiro_digito = (multiplicacao*10)%11
        primeiro_digito_verificacao = 0 if primeiro_digito >= 10 else primeiro_digito
            
        return primeiro_digito_verificacao
    
    def verificar_segundo_digito(cpf):
        digitos = []
        peso = list(range(11,-1,-1))
        multiplicacao = 0

        for digito in cpf:
            try:
                digitos.append(int(digito))
                
            except ValueError:
                continue 
        digitos = digitos[:-1]

        for i in range(len(digitos)):
            multiplicacao += digitos[i] * peso[i]

        segundo_digito = (multiplicacao*10)%11
        segundo_digito_verificacao = 0 if segundo_digito >= 10 else segundo_digito
            
        return segundo_digito_verificacao

    primeiro_digito = verificar_primeiro_digito(cpf)
    segundo_digito = verificar_segundo_digito(cpf)

    if primeiro_digito == int(cpf[-2]) and segundo_digito == int(cpf[-1]):
        return 'Seu CPF é válido'
    else:
        return 'CPF inválido'


resultado = verificar_cpf(cpf)
print(resultado)

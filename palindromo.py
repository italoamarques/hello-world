#Exercicio Palidromo
texto = input('Digite uma palavra ou texto e vamos checar se é um palindromo: ')

def palindromo(texto):
    #texto_reverso = texto[::-1]
    texto_reverso = ''.join(reversed(texto))
    if texto == texto_reverso:
        print ('É um palindromo')
    else: 
        print('Não é um palindromo')

palindromo(texto)


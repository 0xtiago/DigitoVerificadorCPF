#!/usr/bin/python3
lista = []
rangeDigito1 = []
rangeDigito2 = []
resultadoMultiplicacao = []
primeiroDigito = 0
segundoDigito = 0

#Recebe 9 primeiros digitos do CPF
cpf = input("Digite os primeiros 9 numero do CPF (apenas numeros): ")

def caculoPrimeiroDigito(cpf):
    global primeiroDigito
    #Adiciona todos os números em uma lista para o calculo
    for numero in cpf:
        lista.append(int(numero))

    #Cria range de 10 a 2 e insere em uma lista
    for numeroRange in range(10,1,-1):
        rangeDigito1.append(numeroRange)
    
    #Cria lista de resultado de multiplicação
    for i in range(0, len(lista)):
        resultadoMultiplicacao.append(lista[i] * rangeDigito1[i])
    
    #Soma todos os numeros, divide por 11, e verifica quociente
    for i in range (0,len(resultadoMultiplicacao)):
        primeiroDigito =  primeiroDigito + resultadoMultiplicacao[i]
    if primeiroDigito % 11 < 2:
        primeiroDigito = 0
    primeiroDigito = 11 - (primeiroDigito % 11)



def caculoSegundoDigito(cpf):
    global segundoDigito
    #Adiciona todos os números em uma lista para o calculo
    for numero in cpf:
        lista.append(int(numero))
    
    #Adiciona o primeiro digito verificador ao final da lista
    lista.append(int(primeiroDigito))
    
    #Cria range de 11 a 2 e insere em uma lista
    for numeroRange in range(11,1,-1):
        rangeDigito2.append(numeroRange)
    
    #Cria lista de resultado de multiplicação
    for i in range(0, len(lista)):
        resultadoMultiplicacao.append(lista[i] * rangeDigito2[i])
    
    #Soma todos os numeros, divide por 11, e verifica quociente
    for i in range (0,len(resultadoMultiplicacao)):
        segundoDigito =  segundoDigito + resultadoMultiplicacao[i]
    if segundoDigito % 11 < 2:
        segundoDigito = 0
    segundoDigito = 11 - (segundoDigito % 11)



caculoPrimeiroDigito(cpf)
caculoSegundoDigito (cpf)

print (lista)
print (rangeDigito1)
print (resultadoMultiplicacao)
print (primeiroDigito)
print (segundoDigito)
    




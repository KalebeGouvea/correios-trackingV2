# Programa em Python que consome API REST para rastrear encomendas dos Correios
# ao inserir um codigo de rastreamento.

#API de rastreamento a objeto dos Correios disponível em:
#https://github.com/chipytux/correiosApi

import requests

def consultar(cod):
    #Método GET utilizado para obter o JSON da API REST
    response = requests.get('https://api.linketrack.com/track/json?user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&codigo=' + str(cod))
    return response.json()

#INÍCIO DO PROGRAMA

print('#######################################')
print('###########CORREIOS TRACKING###########')
print('#######################################')
print('Descrição: Este programa rastreia encomendas dos Correios utilizando REST API')
print()

cod = str(input('Informe o código de rastreamento do objeto: '))
json = consultar(cod)

#Loop for utilizado para separar os itens do dicionário
resultado = ''
for evento in json['eventos']:
    resultado += '\n' + '-'*50 + '\n'
    #O print seguinte formata os itens do dicionário para a saída do programa
    resultado += str(evento['data']) + ' ' + str(evento['hora']) + '\n' + str(evento['status'])
    #Mais um loop for utilizado, para imprimir os resultados de outra lista dentro do dicionário
    for subStatus in evento['subStatus']:
        resultado += '\n' + subStatus
print(resultado)

while True:
    salvar_txt = input('\nDeseja salvar o resultado? (s/n) ')
    if salvar_txt.casefold() == 's':
        f = open('results.txt','w')
        f.write('Resultado da consulta:\n' + resultado)
        f.close()
        break
    elif salvar_txt.casefold() == 'n':
        break
    else:
        print('Resposta inválida. Responda apenas s ou n.')
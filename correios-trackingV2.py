# Programa em Python que utiliza Web Scraping para rastrear encomendas dos Correios
# ao inserir um codigo de rastreamento.

import requests

#Funcao de introducao ao usuario 
def welcome():
    print('#######################################')
    print('###########CORREIOS TRACKING###########')
    print('#######################################')
    print('Descrição: Este programa rastreia encomendas dos Correios utilizando Web Scraping')
    print()

#Funcao para salvar o resultado no arquivo results.txt
#Ela recebe como argumento os elementos retornados pelo Beautiful Soup na funcao rastrear()
def salvar(elementos):
    salvar_txt = input('Deseja salvar o resultado? (s/n) ')
    if salvar_txt.casefold() == 's':
        f = open('results.txt','w')
        for ul in elementos:
            f.write(ul.text)
            f.write('\n')
            f.write('-'*40)
        f.close()
    elif salvar_txt.casefold() == 'n':
        pass
    else:
        print('Resposta inválida. Responda apenas s ou n.')
        salvar(elementos)

#Funcao para rastrear um novo objeto
def again():
    run_again = input('Deseja rastrear outro objeto? (s/n) ')
    if run_again.casefold() == 's':
        rastrear()
    elif run_again.casefold() == 'n':
        pass
    else:
        print('Resposta inválida. Responda apenas s ou n.')
        again()

welcome()
rastrear()

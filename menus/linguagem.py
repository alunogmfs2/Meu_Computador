from module import *
from funcoes.comandos.comandos import *


def menuLinguagem(tipo: str) -> int:
    while True:
        limpar_terminal()
        espaco()
        print(f'Bem vindo ao {colorir('verde', f'Menu de {tipo.capitalize()}')}')
        opcoes()
        
        try:
            escolha = int(input('Escolha: '))
            if escolha > 5 or escolha < 0:
                espaco()
                raise TypeError
        except ValueError:
            erro('Escreva um Número')
            continue
        except TypeError:
            erro('Escolha uma opcao válida')
            continue
            
        
        if escolha == 0:
            espaco(2)
            print(colorir('amarelo', 'Saindo...'))
            pausar_terminal()
            break
        
        return escolha
    return 0

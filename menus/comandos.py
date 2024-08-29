from module import *

def menuComandos() -> int:
    while True:
        limpar_terminal()
        espaco()
        print(f'Bem vindo ao {colorir('verde', 'Menu de Comandos')}')
        espaco()
        print(f' 0 - {colorir('vermelho', 'Sair')}')
        print(f' 1 - {colorir('roxo', 'Python')}')
        print(f' 2 - {colorir('roxo', 'Javascript')}')
        print(f' 3 - {colorir('roxo', 'C++')}')
        print(f' 4 - {colorir('roxo', 'Java')}')
        print(f' 5 - {colorir('roxo', 'HTML')}')
        print(f' 6 - {colorir('roxo', 'CSS')}')
        print(f' 7 - {colorir('roxo', 'SQL')}')
        print(f' 8 - {colorir('roxo', 'Powershell')}')
        print(f' 9 - {colorir('roxo', 'Linux')}')
        print(f' 10 - {colorir('roxo', 'Lua')}')
        print(f' 11 - {colorir('roxo', 'Vim')}')
        espaco()
        
        try:
            escolha: int = int(input('Escolha: '))
            if escolha > 12 or escolha < 0:
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
            break
        
        return escolha
    return 0

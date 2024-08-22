from module import *

def numeros() -> tuple[float]:
    while True:
        limpar_terminal()
        try:
            n1 = int(input('Escreva o primeiro número: '))
            n2 = int(input('Escreva o segundo número: '))
        except ValueError:
            erro('Escreva um Número')
            continue

        return n1, n2

def somar() -> None:
    n1, n2 = numeros()
    resultado: float = n1 + n2
    
    espaco()
    print(f'{n1} + {n2} = {colorir('rosa', str(resultado))}')
    espaco()
    
    pausar_terminal()

def subtrair() -> None:
    n1, n2 = numeros()
    resultado: float = n1 - n2
    
    espaco()
    print(f'{n1} - {n2} = {colorir('rosa', str(resultado))}')
    espaco()
    
    pausar_terminal()

def multiplicar() -> None:
    n1, n2 = numeros()
    resultado: float = n1 * n2
    
    espaco()
    print(f'{n1} x {n2} = {colorir('rosa', str(resultado))}')
    espaco()
    
    pausar_terminal()

def dividir() -> None:
    while True:
        n1, n2 = numeros()
        try:
            resultado: float = n1 / n2
        except ZeroDivisionError:
            erro('Não é possível dividir por zero')
            continue
        
        espaco()
        print(f'{n1} / {n2} = {colorir('rosa', f'{resultado:.5f}')}')
        espaco()
        
        pausar_terminal()
        break

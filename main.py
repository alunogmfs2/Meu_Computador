from module import *
from menus.principal import menuPrincipal
from menus.calculadora import menuCalculadora
from funcoes.calculadora.calculos import *
from funcoes.modos.modos import *
from menus.modos import *

escolhaMain: int = -1
escolhaModos: int = menuModos()

if escolhaModos == 1:
    abrirTudo(1)
elif escolhaModos == 2:
    abrirTudo(2)
elif escolhaModos == 3:
    abrirTudo(3)
elif escolhaModos == 4:
    abrirTudo(4)
elif escolhaModos == 5:
    abrirTudo(5)
else:
    exit()

while True:
    if escolhaMain == 1:
        while True:
            escolhaCalc: int = menuCalculadora()
            if escolhaCalc == 1:
                somar()
            elif escolhaCalc == 2:
                subtrair()
            elif escolhaCalc == 3:
                multiplicar()
            elif escolhaCalc == 4:
                dividir()
            else:
                break
    elif escolhaMain == 0:
        exit()
    escolhaMain = menuPrincipal()

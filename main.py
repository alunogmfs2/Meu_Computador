from module import *
from menus.principal import menuPrincipal
from menus.calculadora import menuCalculadora
from funcoes.calculadora.calculos import *

escolhaMain: int = -1

while True:
    if escolhaMain == 1:
        escolhaCalc: int = menuCalculadora()
        if escolhaCalc == 1:
            somar()
        elif escolhaCalc == 2:
            subtrair()
        elif escolhaCalc == 3:
            multiplicar()
        elif escolhaCalc == 4:
            dividir()
    elif escolhaMain == 0:
        exit()
    escolhaMain = menuPrincipal()

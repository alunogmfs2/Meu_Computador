from module import *
import os
import shutil


def perguntarCaminhoArquivo() -> str:
    return input(f'Digite o {colorir('rosa', 'Caminho')} do seu Arquivo: ')

def existeCaminhoArquivo(caminho: str) -> bool:
    return os.path.exists(caminho)

def fazerBackup() -> None:
    while True:
        caminho = perguntarCaminhoArquivo()
        
        if not existeCaminhoArquivo(caminho):
            erro('O Caminho nao existe')
            continue
        
        espaco()
        
        descisao = input(f'Você quer continuar {colorir('roxo', '[Y/N]')}? ').lower() == 'y'
        
        espaco()
        
        if not descisao:
            espaco(2)
            print(colorir('amarelo', 'Cancelando...'))
            break
        
        shutil.copy(caminho, 'G:\\Meu Drive\\')
        
        print(colorir('verde', 'Pronto'))
        
        espaco()
        pausar_terminal()
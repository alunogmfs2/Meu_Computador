from module import *
import os
import json
import datetime


def opcoes() -> None:
    espaco()
    print(f' 0 - {colorir('vermelho', 'Sair')}')
    print(f' 1 - {colorir('roxo', 'Procurar Comando')}')
    print(f' 2 - {colorir('roxo', 'Adicionar Comando')}')
    print(f' 3 - {colorir('roxo', 'Atualizar Comando')}')
    print(f' 4 - {colorir('roxo', 'Deletar Comando')}')
    print(f' 5 - {colorir('roxo', 'Listar Comandos')}')

def criarArquivoComando(tipo: str) -> None:
    with open(f'E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\{tipo}.json', 'w') as f:
        f.write('[]')

def existeArquivoComando(tipo: str) -> bool:
    return os.path.exists(f'E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\{tipo}.json')

def lerArquivoComando(tipo: str) -> list:
    with open(f'E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\{tipo}.json', 'r') as f:
        return json.loads(f.read())

def adicionarComandoEmArquivoComando(tipo: str, comando: str, descricao: str) -> None:
    if not existeArquivoComando(tipo):
        criarArquivoComando(tipo)
    with open(f'E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\{tipo}.json', 'r') as f:
        cmds: list = json.load(f)

    if not lerArquivoComando(tipo):
        id: int = 1
    else:
        id: int = lerArquivoComando(tipo)[-1]['id'] + 1
    
    cmd = {
        'id': id,
        'comando': comando,
        'descricao': descricao,
        'data_criacao': f'{datetime.datetime.now()}',
        'data_atualizacao': f'{datetime.datetime.now()}'
    }
    
    
    cmds.append(cmd)
    
    with open(f'E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\{tipo}.json', 'w') as f:
        t = json.dumps(cmds)
        f.write(t)

def perguntarComando() -> str:
    cmd = input('Digite o nome do Comando: ')
    return cmd

def perguntarDescricao() -> str:
    descricao = input('Digite a Descricao do Comando: ')
    return descricao

def procurarComando(tipo: str) -> None:
    limpar_terminal()
        
    try:
        comandos = lerArquivoComando(tipo)
    except:
        erro('Escreva algum Comando primeiro')
        return
    
    if not len(lerArquivoComando(tipo)):
        erro('Escreva algum Comando primeiro')
        return
    
    comando = perguntarComando()
    
    for cmd in comandos:
        if cmd['comando'] == comando:
            limpar_terminal()
            
            print(f'{colorir('rosa', 'Comando:')} {cmd['comando']}')
            print(f'{colorir('rosa', 'Descricao:')} {cmd['descricao']}')
            
            espaco()
            pausar_terminal()
            return
    
    erro('Comando nao Achado')

def adicionarComando(tipo: str) -> None:
    limpar_terminal()
    comando = perguntarComando()
    descricao = perguntarDescricao()
    espaco()
    
    adicionarComandoEmArquivoComando(tipo, comando, descricao)
    
    print(f'{colorir('rosa', 'Comando')} adicionado')
    espaco()
    pausar_terminal()

def atualizarComando(tipo: str) -> None:
    while True:
        limpar_terminal()
        
        try:
            comandos = lerArquivoComando(tipo)
        except:
            erro('Escreva algum Comando primeiro')
            return
        
        if not len(lerArquivoComando(tipo)):
            erro('Escreva algum Comando primeiro')
            return
        
        listarComandos(tipo)
        
        espaco()
        try:
            comando = int(input('ID do Comando: '))
        except ValueError:
            erro('Escreva um Número')
            continue
        
        espaco()
        for cmd in comandos:
            if cmd['id'] == comando:
                print(f'Descricao anterior: {colorir('roxo', cmd['descricao'])}')
                novaDescricao = input('Escreva a nova descricao: ')
                cmd['descricao'] = novaDescricao
                cmd['data_atualizacao'] = f'{datetime.datetime.now()}'
                with open(f'E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\{tipo}.json', 'w') as f:
                    t = json.dumps(comandos)
                    f.write(t)
                return
        
        erro('Descricao nao achada')
        espaco()
        pausar_terminal()
    erro('Escreva um Comando primeiro')

def deletarComando(tipo: str) -> None:
    while True:
        limpar_terminal()
        
        try:
            comandos = lerArquivoComando(tipo)
        except:
            erro('Escreva algum TODO primeiro')
            return
        
        if not len(lerArquivoComando(tipo)):
            erro('Escreva algum TODO primeiro')
            return
        
        listarComandos(tipo)
        espaco()
        try:
            id = int(input('Digite o ID do Comando: '))
        except ValueError:
            erro('Escreva um Número')
            continue
        
        for cmd in comandos:
            print(cmd)
            if cmd['id'] == id:
                comandos.remove(cmd)
                with open(f'E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\{tipo}.json', 'w') as f:
                    t = json.dumps(comandos)
                    f.write(t)
                return
        
        erro('ID nao achado')

def listarComandos(tipo: str) -> None:
    limpar_terminal()
    try:
        comandos: list = lerArquivoComando(tipo)
    except:
        erro('Escreva algum Comando primeiro')
        return
    
    if not len(lerArquivoComando(tipo)):
        erro('Escreva algum Comando primeiro')
        return
    
    lim = 10
    
    cont = 0
    
    for cmd in comandos:
        print(f'{colorir('azul', cmd['id'])} - {colorir('rosa', cmd['comando'])}:\n{colorir('roxo', cmd['descricao'])}')
        espaco()
        
        if cont == lim:
            cont = 0
            pausar_terminal()
            limpar_terminal()
            continue
        
        cont += 1
    
    pausar_terminal()


from datetime import date
from typing import Dict, List
import csv
import os

meses_dict: Dict[int, str] = {
    1:'Janeiro',
    2:'Fevereiro',
    3:'Março',
    4:'Abril',
    5:'Maio',
    6:'Junho',
    7:'Julho',
    8:'Agosto',
    9:'Setembro',
    10:'Outubro',
    11:'Novembro',
    12:'Dezembro'
}


while True: 

    funcao = input('Adicionar horas[h]\nMostrar relatório[r]\nSair[s]\n\n')

    if funcao == 'h':

        # dados referentes à data
        dia: str = input('Hoje? Sim[s] Não[n] ')

        if dia == 's':
            data: int = date.today()
            dia: int = data.day
            mes: int = data.month
            ano: int = data.year
        else:
            dia: int = int(input('Dia: '))
            mes: int = int(input('Mês: '))
            ano: int = int(input('Ano: '))

        # dados referentes às horas trabalhadas
        horas: int = int(input('Quantas horas trabalhadas: '))
        minutos: int = int(input('Quantas minutos trabalhados: '))
        commit: str = input('Commit referente: ')

        # cria ou abre um arquivo csv
        nome_arquivo: str = f'horas_{meses_dict[mes]}_{ano}.csv'
        path: str = 'dados/'
        with open(path+nome_arquivo, 'a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([dia, mes, ano, horas, minutos, commit])
        
        print('\nDados cadastrados com sucesso!\n')

    elif funcao == 'r':

        mes_atual: str = input('Relatório do mês atual? Sim[s] Não[n] ')

        if mes_atual == 's':
            ano_relatorio: int = date.today().year
            mes_relatorio: int = date.today().month
        else:
            ano_relatorio: int = int(input('Qual o ano para o relatório? '))
            mes_relatorio: int = int(input('Qual o mês para o relatório? '))

        dia: List[int] = list()
        mes: List[int] = list()
        ano: List[int] = list()
        horas: List[int] = list()
        minutos: List[int] = list()
        commit: List[str] = list()

        arquivo_relatorio_data: str = f'horas_{meses_dict[mes_relatorio]}_{ano_relatorio}.csv'
        path: str = 'dados/'

        if not os.path.exists(path+arquivo_relatorio_data):
            print('\nDiretório não encontrado!\n')
            
        else:
            with open(path+arquivo_relatorio_data, 'r') as csv_file:
                for linha in csv_file:
                    dados_tabela = linha.split(',')
                    dia.append(dados_tabela[0])
                    mes.append(dados_tabela[1])
                    ano.append(dados_tabela[2])
                    horas.append(dados_tabela[3])
                    minutos.append(dados_tabela[4])
                    commit.append(dados_tabela[5])

        soma_minutos: int = 0
        soma_horas: int = 0
        for min in minutos:
            soma_minutos += int(min)
            if soma_minutos > 60:
                soma_horas += 1
                soma_minutos -= 60
        for hor in horas:
            soma_horas += int(hor)

        arquivo_relatorio = f'relatorio_{meses_dict[mes_relatorio]}_{ano_relatorio}.txt'
        path: str = 'relatorios/'

        if not os.path.exists(path+arquivo_relatorio):
            print('\nDiretório não encontrado!\n')

        with open(path+arquivo_relatorio , 'w') as relatorio:
            relatorio.write(f'Horas trabalhadas no mês de {meses_dict[mes_relatorio]}:')
            relatorio.write('\n\n')
            relatorio.write('Dia\t\tHoras\tCommit')
            relatorio.write('\n')
            relatorio.write('-'*42)
            relatorio.write('\n')
            for i, _ in enumerate(dia):
                relatorio.write(f'{dia[i]}/{mes[i]}\t{horas[i]}:{minutos[i]}\t{commit[i]}')
            relatorio.write(f'\nTotal de horas trabalhadas para o mês de {meses_dict[mes_relatorio]}: {soma_horas}:{soma_minutos}h')

        print('')
        print('Dia\tHoras\tCommit')
        print('-'*42)
        for i, _ in enumerate(dia):
            print(f'{dia[i]}/{mes[i]}\t{horas[i]}:{minutos[i]}\t{commit[i]}', end='')
            
        print('')
        print(f'Total de horas trabalhadas para o mês de {meses_dict[mes_relatorio]}: {soma_horas}:{soma_minutos}h')

    else:
        break
print('\n\nObrigado!\n')
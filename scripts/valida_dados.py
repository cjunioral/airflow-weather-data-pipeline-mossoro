import os
import pandas as pd
from datetime import datetime

PASTA_PROCESSED = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'processed')

def validar_dados():
    hoje = datetime.today().strftime('%Y-%m-%d')

    arquivos = [
        f'temperaturas_{hoje}.csv',
        f'condicoes_{hoje}.csv',
        f'clima_consolidado_{hoje}.csv'
    ]

    for arquivo in arquivos:
        caminho = os.path.join(PASTA_PROCESSED, arquivo)

        if not os.path.exists(caminho):
            raise FileNotFoundError(f'Arquivo não encontrado: {caminho}')

        df = pd.read_csv(caminho)

        if df.empty:
            raise ValueError(f'Arquivo vazio: {caminho}')

        print(f'Arquivo validado com sucesso: {arquivo} | Linhas: {len(df)}')

if __name__ == '__main__':
    validar_dados()
import os
import pandas as pd
from datetime import datetime, timedelta

def extrair_dados():

    data_inicio = datetime.today()
    data_fim = data_inicio + timedelta(days=7)


    data_inicio = data_inicio.strftime('%Y-%m-%d')
    data_fim = data_fim.strftime('%Y-%m-%d')

    city = 'Mossoro'
    key = '467JQJ935X3KDX53ABDS2RXJ9'

    url = (f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
        f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')
    
    try:
        dados = pd.read_csv(url)
    except Exception as e:
        raise RuntimeError(f'Erro ao buscar dados da API: {e}')
    
    print(dados.head())

    pasta_raw = f'/root/Documents/datapipeline/data/raw'
    os.makedirs(pasta_raw, exist_ok=True)
    
    nome_arquivo = f'clima_mossoro_raw_{data_inicio}.csv'
    caminho_arquivo = os.path.join(pasta_raw, nome_arquivo)

    dados = pd.read_csv(url)
    dados.to_csv(caminho_arquivo, index=False)
    
    print(f'Arquivo bruto salvo em: {caminho_arquivo}')
    

if __name__ == '__main__':
    extrair_dados()

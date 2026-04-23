import os
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def extrair_dados():

    data_inicio = datetime.today()
    data_fim = data_inicio + timedelta(days=7)


    data_inicio = data_inicio.strftime('%Y-%m-%d')
    data_fim = data_fim.strftime('%Y-%m-%d')

    city = 'Mossoro'
    key = os.getenv('VISUAL_CROSSING_KEY')

    url = (f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
        f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')
    
    try:
        dados = pd.read_csv(url)
    except Exception as e:
        raise RuntimeError(f'Erro ao buscar dados da API: {e}')
    
    print(dados.head())

    pasta_raw = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'raw')
    os.makedirs(pasta_raw, exist_ok=True)
    
    nome_arquivo = f'clima_mossoro_raw_{data_inicio}.csv'
    caminho_arquivo = os.path.join(pasta_raw, nome_arquivo)

    dados = pd.read_csv(url)
    dados.to_csv(caminho_arquivo, index=False)
    
    print(f'Arquivo bruto salvo em: {caminho_arquivo}')
    

if __name__ == '__main__':
    extrair_dados()

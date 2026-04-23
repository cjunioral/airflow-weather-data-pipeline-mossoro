import os
import pandas as pd
from datetime import datetime


PASTA_RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'raw')
PASTA_PROCESSED = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'processed')


def transformar_dados():
    hoje = datetime.today().strftime('%Y-%m-%d')
    arquivo_raw = os.path.join(PASTA_RAW, f'clima_mossoro_raw_{hoje}.csv')
    
    if not os.path.exists(arquivo_raw):
        raise FileNotFoundError(f'Arquivo dados brutos não encontrado: {arquivo_raw}')
    
    os.makedirs(PASTA_PROCESSED, exist_ok=True)
    
    df = pd.read_csv(arquivo_raw)
    
    temperaturas = df[['datetime', 'tempmin', 'temp', 'tempmax']].copy()
    temperaturas['cidade'] = 'Mossoro'
    temperaturas['data_coleta'] = hoje
    
    temperaturas.rename(columns={
        'datetime': 'data',
        'tempmin': 'temperatura_minima',
        'temp': 'temperatura_media',
        'tempmax': 'temperatura_maxima'   
    }, inplace=True)
    
    condicoes = df[['datetime', 'description', 'icon']].copy()
    condicoes['cidade'] = 'Mossoro'
    condicoes['data_coleta'] = hoje

    condicoes.rename(columns={
        'datetime': 'data',
        'description': 'descricao',
        'icon': 'icone'
    }, inplace=True)
    
    
    consolidado = df[[
        'datetime', 'tempmin', 'temp', 'tempmax', 'humidity',
        'precip', 'windspeed', 'description', 'icon'
    ]].copy()
    
    consolidado['cidade'] = 'Mossoro'
    consolidado['data_coleta'] = hoje
    
    consolidado.rename(columns={
        'datetime': 'data',
        'tempmin': 'temperatura_minima',
        'temp': 'temperatura_media',
        'tempmax': 'temperatura_maxima',
        'humidity': 'umidade',
        'precip': 'precipitacao',
        'windspeed': 'velocidade_vento',
        'description': 'descricao',
        'icon': 'icone'
    }, inplace=True)
    
    temperaturas.to_csv(
        os.path.join(PASTA_PROCESSED, f'temperaturas_{hoje}.csv'),
        index=False
    )

    condicoes.to_csv(
        os.path.join(PASTA_PROCESSED, f'condicoes_{hoje}.csv'),
        index=False
    )

    consolidado.to_csv(
        os.path.join(PASTA_PROCESSED, f'clima_consolidado_{hoje}.csv'),
        index=False
    )

    print('Arquivos tratados salvos com sucesso.')
    
    
if __name__ == '__main__':
    transformar_dados()
    
    
    
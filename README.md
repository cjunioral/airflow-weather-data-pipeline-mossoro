# 🌦️ Airflow Weather Data Pipeline -- Mossoró

Este projeto implementa um **pipeline de dados climáticos** utilizando
**Python e Apache Airflow** para coletar, transformar e validar dados
meteorológicos da cidade de **Mossoró (RN)**.

O pipeline é executado automaticamente e demonstra conceitos importantes
de **Engenharia de Dados**, como:

-   Extração de dados via API
-   Transformação e limpeza de dados
-   Validação de dados
-   Orquestração de pipelines com Airflow

------------------------------------------------------------------------

# 🚀 Tecnologias utilizadas

-   Python
-   Apache Airflow
-   Pandas
-   Visual Crossing Weather API
-   Git & GitHub

------------------------------------------------------------------------

# 📊 Arquitetura do Pipeline

O pipeline segue as seguintes etapas:

1.  **Extração**
    -   Coleta dados climáticos da API Visual Crossing.
2.  **Transformação**
    -   Filtra e organiza os dados relevantes.
3.  **Validação**
    -   Verifica consistência e integridade dos dados.
4.  **Finalização**
    -   Pipeline finalizado após validação.

Fluxo da DAG:

    inicio_pipeline
          ↓
    extrai_dados_climaticos
          ↓
    transforma_dados_climaticos
          ↓
    valida_dados_climaticos
          ↓
    fim

------------------------------------------------------------------------

# 📁 Estrutura do projeto

    airflow-weather-data-pipeline-mossoro
    │
    ├── scripts
    │   ├── extrai_dados.py
    │   ├── transforma_dados.py
    │   └── valida_dados.py
    │
    ├── dags
    │   └── dados_climaticos_mossoro.py
    │
    ├── data
    │   ├── raw
    │   └── processed
    │
    ├── requirements.txt
    ├── README.md
    └── .gitignore

------------------------------------------------------------------------

# ⚙️ Como executar o projeto

## 1️⃣ Instalar dependências

``` bash
pip install -r requirements.txt
```

## 2️⃣ Iniciar o Airflow

``` bash
airflow standalone
```

## 3️⃣ Acessar o Airflow

Abra no navegador:

    http://localhost:8080

Ative a DAG:

    dados_climaticos_mossoro

------------------------------------------------------------------------

# 🌍 Fonte dos dados

Os dados meteorológicos são obtidos através da:

**Visual Crossing Weather API**

https://www.visualcrossing.com/

------------------------------------------------------------------------

# 👨‍💻 Autor

Projeto desenvolvido como estudo de **Engenharia de Dados**, utilizando
Python e Airflow para construção de pipelines de dados.

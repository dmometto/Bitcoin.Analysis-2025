# 📈 Bitcoin Analysis 2025  
### Sazonalidade e Volatilidade do Mercado

Este projeto apresenta uma **análise de dados do Bitcoin ao longo do ano de 2025**, com foco na identificação de **padrões de sazonalidade** e na mensuração da **volatilidade do ativo**.  

O objetivo é oferecer uma visão clara sobre **momentos de maior risco e oportunidade**, utilizando métricas estatísticas e visualizações intuitivas para apoiar decisões no mercado financeiro.

---

## 🎯 Objetivos do Projeto

- Identificar padrões de rendimento mensal do Bitcoin (sazonalidade)
- Avaliar o nível de instabilidade do ativo por meio da volatilidade diária
- Facilitar a visualização de períodos de lucro e prejuízo
- Criar uma base de dados limpa e estruturada para análises futuras

---

## ⚙️ Funcionalidades

- **Processamento ETL Automático**  
  Conversão de timestamps, tratamento de duplicatas e limpeza de dados brutos.

- **Filtragem Temporal**  
  Recorte exclusivo para o ano de **2025**, eliminando ruídos históricos.

- **Cálculo de Performance**  
  Geração automática da variação percentual entre períodos selecionados.

- **Métricas de Risco**  
  Cálculo da amplitude diária dos preços para análise de volatilidade.

- **Visualização de Dados**  
  Gráficos de barras com paletas divergentes para fácil distinção entre lucros e perdas.

---

## 🔬 Metodologia

### 📌 Pontos de Controle
A base original (dados minuto a minuto) foi filtrada para capturar apenas:
- **Dia 01** (abertura do mês)
- **Dia 15** (meio do mês)
- **Último dia** (fechamento do mês)

### 📊 Variação Percentual
A variação percentual é calculada da seguinte forma:

((Preço Atual - Preço Anterior) / Preço Anterior) * 100


### 📁 Dataset
O arquivo original utilizado na análise (btcusd_1-min_data.csv) possui um volume muito grande de dados, ultrapassando os limites de armazenamento recomendados para versionamento no GitHub.

Por esse motivo, o arquivo não foi disponibilizado no repositório, sendo assim segue o link para download da base original: https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data 


### 📉 Indicador de Volatilidade
A volatilidade é mensurada pela **amplitude diária**, utilizando a diferença absoluta entre:

- Preço máximo (**High**)
- Preço mínimo (**Low**)

Essa métrica representa o nível de risco e instabilidade do ativo no período.

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Pandas**
- **Matplotlib**
- **Seaborn**

---

## 📂 Estrutura do Projeto

📦 bitcoin-analysis-2025
├── main.py
├── Graficos.ipynb
├── result_bitcoin_2025.csv
└── .gitignore

---

## 🚀 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/dmometto/bitcoin-analysis-2025.git

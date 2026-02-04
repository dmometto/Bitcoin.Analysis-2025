📈 Bitcoin Analysis 2025: Sazonalidade e Volatilidade

Este projeto consiste em uma análise de dados focada no comportamento do Bitcoin durante o ano de 2025. O estudo visa identificar padrões de rendimento mensal (sazonalidade) e medir o nível de instabilidade do ativo através da amplitude de preços (volatilidade), fornecendo uma visão clara sobre os momentos de maior risco e oportunidade no mercado financeiro.

⚙️ Funcionalidades
Processamento ETL Automático: Conversão de Timestamps e limpeza de dados brutos para garantir a integridade da análise.

Filtragem Temporal: Recorte específico para o ano de 2025, eliminando ruídos de anos anteriores.

Cálculo de Performance: Geração automática da variação percentual entre os períodos selecionados.

Métricas de Risco: Cálculo de amplitude diária para análise de volatilidade e exposição ao risco.

Visualização de Dados: Geração de gráficos de barras com paletas divergentes para facilitar a distinção visual entre lucros e prejuízos.

🔬 Metodologias

Pontos de Controle: A base original minuto a minuto foi filtrada para capturar apenas os dados do dia 01 (abertura), 15 (meio) e último dia (fechamento) de cada mês.

Variação Percentual: A variação é calculada comparando o preço de fechamento atual com o preço de fechamento do período anterior, multiplicando o resultado por 100 para obter o valor percentual.

Indicador de Volatilidade: Utilização da diferença absoluta entre os preços máximo (High) e mínimo (Low) registrados no mesmo dia para mensurar a amplitude de negociação e o risco sistêmico.

🛠️ Tecnologias Usadas

Python

Pandas

Seaborn e Matplotlib

Jupyter Notebook

📂 Estrutura do Projeto
O repositório está organizado de forma modular, separando as etapas de tratamento e análise visual:

TratamentoDados.ipynb: Script principal responsável pela carga do dataset, aplicação dos filtros de data, tratamento de duplicatas e exportação da base limpa.

VariacaoMedia.ipynb: Notebook dedicado à análise visual da sazonalidade e performance mensal do Bitcoin.

Volatilidade.ipynb: Notebook focado no mapeamento do risco e análise da amplitude de preços.

bitcoin_2025.csv: Arquivo de dados processados contendo o resumo estratégico do ano de 2025.

requirements.txt: Lista de dependências para instalação e replicação do ambiente de desenvolvimento.

.gitignore: Configuração para impedir o envio de arquivos temporários e datasets brutos de grande escala para o repositório.

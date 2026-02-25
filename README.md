# 📊 Projeto BI — Distribuidora Max
Este projeto simula um cenário real de uma distribuidora, onde uma base de dados bruta passa por um processo de limpeza e tratamento
##  🧠  Objetivo do Projeto
- Qual categoria mais fatura?
- Quais produtos são estratégicos para a empresa?
- Onde o estoque está crítico?
- Qual o potencial de faturamento parado em estoque?
- Quais fornecedores e cidades mais impactam o resultado?
---
##  🛠️  Tecnologias Utilizadas
- Python
- Pandas
- Power BI
- Git e GitHub
---
##  🔄  Processo de Tratamento de Dados (ETL)
O script `etl_produtos.py` realiza:
- Padronização de colunas textuais
- Cálculo do preço com desconto
- Cálculo do faturamento mensal
- Classificação do status de estoque
- Classificação da faixa de avaliação
- Identificação de produtos estratégicos
- Cálculo do potencial de faturamento
- Geração do arquivo `produtos_tratados.csv`
---
## ▶️  Como Executar o Projeto
### 1️⃣  Clonar o repositório
```bash
git clone https://github.com/ThiagoMarques16/AnaliseDeVendasMax.git
cd AnaliseDeVendasMax
```
### 2️⃣ Criar o ambiente virtual
```bash
python -m venv venv
```
### 3️⃣ Ativar o ambiente
Windows:
```
venv\Scripts\activate
```
Mac/Linux:
```
source venv/bin/activate
```
### 4️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```
### 5️⃣ Executar o script
```bash
python python/etl_produtos.py
```
---
## 👨‍💻 Autor
Thiago Marques
🌐 https://thiagomarques.netlify.app/

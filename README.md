# 📊 Projeto BI — Distribuidora Max

Este projeto simula um cenário real de uma distribuidora, onde uma base de dados bruta passa por um processo de **ETL com Python (Pandas)** para se tornar uma **base analítica** utilizada na construção de dashboards gerenciais no **Power BI**.

O foco do projeto é demonstrar, na prática, como dados operacionais se transformam em **informação estratégica para tomada de decisão**.

---

## 🧠 Objetivo do Projeto

Transformar uma planilha de produtos em uma base preparada para responder perguntas de negócio como:

- Qual categoria mais fatura?
- Quais produtos são estratégicos para a empresa?
- Onde o estoque está crítico?
- Qual o potencial de faturamento parado em estoque?
- Quais fornecedores e cidades mais impactam o resultado?

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- Power BI
- Git e GitHub

---
## 🔄 Processo de Tratamento de Dados (ETL)

O script `etl_produtos.py` realiza automaticamente:

- Padronização de colunas textuais
- Cálculo do preço com desconto
- Cálculo do faturamento mensal
- Classificação do status de estoque (Crítico, Alerta, Normal)
- Classificação da faixa de avaliação do produto
- Identificação de produtos estratégicos
- Cálculo do potencial de faturamento com base no estoque
- Geração do arquivo final `produtos_tratados.csv`

Este arquivo tratado é a fonte de dados utilizada no Power BI.

---
## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/ThiagoMarques16/AnaliseDeVendasMax.git
cd projeto-bi-distribuidora

### 2️⃣ Criar o ambiente virtual
python -m venv venv

### 3️⃣ Ativar o ambiente virtual

- Windows
venv\Scripts\activate

- Mac/Linux
source venv/bin/activate

### 4️⃣ Instalar as dependências
pip install -r requirements.txt

### 5️⃣ Executar o script de tratamento
python python/etl_produtos.py

Isso irá gerar o arquivo tratado em:
data/produtos_tratados.csv

### 6️⃣ Abrir o Power BI
Abra o arquivo: 
powerbi/dashboard.pbix

Atualize a fonte de dados apontando para:
data/produtos_tratados.csv

---
##🎯 Habilidades Demonstradas

Este projeto demonstra na prática:
ETL com Python e Pandas
Enriquecimento e padronização de dados
Organização profissional de projeto
Integração entre Python e Power BI
Criação de indicadores estratégicos de negócio

##👨‍💻 Autor
Thiago Marques
🌐 Portfólio: https://thiagomarques.netlify.app/
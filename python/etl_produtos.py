import pandas as pd
import os

def main():
      caminho_entrada = os.path.join("data", "produtos.csv")
      caminho_saida = os.path.join("data", "produtos_tratados.csv")
      df = pd.read_csv(caminho_entrada)

      df_tratado = df.copy()

      colunas_texto = ['nome_produto', 'categoria', 'marca', 'fornecedor', 'cidade_fornecedor']

      df_tratado[colunas_texto] = df_tratado[colunas_texto].apply(lambda x: x.str.title())

      df_tratado['preco_com_desconto'] = (
            df_tratado['preco'] * (1 - df_tratado['desconto'] / 100)
      )

      df_tratado['faturamento_mensal'] = (
            df_tratado['preco_com_desconto'] * df_tratado['vendas_mensais']
      )

      df_tratado['status_estoque'] = pd.cut(
            df_tratado['estoque'],
            bins = [-1, 10, 30, float('inf')],
            labels= ['Crítico', 'Alerta', 'Normal']
      )
            
      df_tratado['faixa_avaliacao'] = pd.cut(
            df_tratado['avaliacao'],
            bins=[0, 4.4, 4.69, 5],
            labels=['Regular', 'Boa', 'Excelente']
      )

      df_tratado['produto_estrategico'] = (
            (df_tratado['avaliacao'] >= 4.7) &
            (df_tratado['vendas_mensais'] >= 50)
      ).map({True: "Sim", False: "Não"})

      df_tratado['potencial_faturamento'] = df_tratado['estoque'] * df_tratado['preco_com_desconto']

      df_tratado['preco_com_desconto'] = df_tratado['preco_com_desconto'].round(2)
      df_tratado['faturamento_mensal'] = df_tratado['faturamento_mensal'].round(2)
      df_tratado['potencial_faturamento'] = df_tratado['potencial_faturamento'].round(2)

      ordem_colunas = [
            'id_produto',
            'nome_produto',
            'categoria',
            'marca',
            'fornecedor',
            'cidade_fornecedor',
            'preco',
            'desconto',
            'preco_com_desconto',
            'vendas_mensais',
            'faturamento_mensal',
            'estoque',
            'status_estoque',
            'avaliacao',
            'faixa_avaliacao',
            'produto_estrategico',
            'potencial_faturamento'
      ]

      df_tratado = df_tratado[ordem_colunas]
      df_tratado.to_csv(caminho_saida, index=False)

if __name__ == "__main__":
      main()
import pandas as pd

from googletrans import Translator

from translate import Translator as Translator2

df = pd.read_csv('water_quality_.csv')

#função para pular linha
def pularlinha (qtd_de_vezes):
    print("\n" * qtd_de_vezes)

#Instância do tradutor
translator = Translator()

#Segunda biblioteca para realizar a tradução de palavras que apresentaram erro com a biblioteca do googletrans
translator2 = Translator2(to_lang="pt")

#Nome da coluna para comparação após a tradução
print("Nome das colunas antes da tradução ",list(df.columns))

#Acessando a lista do nome das colunas para efetuar a tradução
for coluna in list(df.columns):

    #Tratamento dos NoneType, valor que não foi possível traduzido
    try:
        traducao = translator.translate(coluna, dest='pt', src='en')
        df.rename(columns={coluna : traducao.text}, inplace=True)
    except:
        pularlinha(2)
        print(f"erro na tradução do nome da coluna {coluna}.")
        pularlinha(1)
        print("Agurade enquanto tentamos realizar a tradução.")
        traducao2 = translator2.translate(coluna)
        df.rename(columns={coluna : traducao2}, inplace=True)

#Novos nomes das colunas
pularlinha(2)
print("Coluna após a tradução ",list(df.columns))

#Identificação e tratamento dos valores nulos

#Número de valores nulos no DataFrame
valores_nulos = df.isnull().sum()
pularlinha(2)
print("Contagem dos valores nulos no DataFrame.\n",valores_nulos)

#Como não é viável estipular valores para os dados nulos, pois os valores verdadeiros podem ultrapassar os \
#valores estipulados, portanto optei por eliminar todas as linhas com valores nulos
df.dropna(inplace=True)

#Verificação que os valores não estão mais no DataFrame
valores_nulos = df.isnull().sum()
pularlinha(1)
print("Contagem dos valores nulos no DataFrame depois do tratamento.\n",valores_nulos)

#Eliminando a coluna check para realizar a analise
df.drop(columns=[df.columns[-1]], inplace=True)
#Corrigindo o index das linhas, porquê a eliminação de linhas nulas apagou os index originais, assim \
#deixando fora de ordem
df.index = range(df.shape[0])
pularlinha(2)
#resultado final do DataFrame
print("Resultado final da tabela com a tradução das colunas, a exclução dos dados nulos e ajustando o index que foi atribuído às linhas.")
pularlinha(1)
print(df.head())
#criação do arquivo CSV tratado para fazer a análise estátistica
df.to_csv('qualidade_da_água.csv', sep=',', index=False)
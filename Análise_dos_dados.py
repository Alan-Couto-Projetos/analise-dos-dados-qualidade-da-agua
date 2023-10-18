import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

#Abrindo o arquivo CSV
df = pd.read_csv('qualidade_da_água.csv')

#faixa de PH considerada com maior nutrientes para o solo está em torno de 5,8 e 6,2\
#fonte do dado para consulta nas notas

#Filtragem da faixa de valores para o PH
faixa_ph = df[(df['ph'] >= 5.8) & (df['ph'] <= 6.2)]
#Usando a Regra de Sturges para calcular o número de bins para o gráfico
N = len(faixa_ph['ph'])
numero_bins = 1 + int(np.log2(N))
#adicionando a figura que criará o gráfico
plt.figure(1)
#gráfico com os valores de PH
sns.histplot(faixa_ph['ph'], bins=numero_bins, kde=True)
#Rótulo e título do gráfico
plt.title('Faixa com mais nutrientes')
plt.ylabel('contagem')

#Determinando a média aritmética de dados agrupados em intervalos
media_PH = (5.8 + 6.2) / 2

#valores que estão abaixo, igual e acima da média no DataFrame
categorias = ['Abaixo da média', 'Igual da média', 'Acima da média']
valores_abaixo = [x for x in df['ph'] if x < media_PH]
valores_igual = [x for x in df['ph'] if x == media_PH]
valores_acima = [x for x in df['ph'] if x > media_PH]
contagens = [len(valores_abaixo), len(valores_igual), len(valores_acima)]


#Verificando que não há nenhum valor igual a 6
valores_contados = df[df['ph'] == media_PH]

#adicionando a figura que criará o gráfico
plt.figure(2)
#Gerando um gráfico da contagem do PH ideal no DataFrame todo
total_media = plt.bar(categorias, contagens, color=['red', 'green', 'blue'])
#Adicionando o valor total em cima de cada barra
for barra in total_media:
    #Medindo a altura total da barra
    altura = barra.get_height()
    #Determinando as coordenadas X e Y 
    x, y = barra.get_xy()
    #Adicionando um rótulo ao gráfico após determinar a posição no qual irá ficar
    plt.annotate(f'{altura}',
                 (x + barra.get_width() / 2, altura),
                 ha='center',
                 va='bottom')
#Rótulos do eixo X e Y, e títulos
plt.title('PH acima, abaixo e igual a média de 5,8 a 6,2')

#optei por case para n precisar realizar o tratamento de erros na entrada do nome da coluna, visto que é \
#necessário que o nome seja identico, escreve essa nota na documentação


#determinando a média do PH para todo o DataFrame
media_geral_ph = df['ph'].sum() / df.shape[0]
#adicionando a figura que criará o gráfico
plt.figure(3)
#Gráfico de dispersão do PH em comparação a média
plt.scatter(range(len(df['ph'])), df['ph'], label='Dados')
plt.axhline(y=media_geral_ph, color='red', linestyle='--', label='Valor Médio Fixo')
#Rótulo do eixo X e Y, e título
plt.title('Dispersão do PH')
plt.ylabel('PH')
plt.xlabel('Número da linha')
# Criando uma legenda personalizada
legenda = "Estilo da linha: '--'\nSignificado: Média dos dados"
# Adiciona a legenda ao gráfico
plt.legend([legenda], loc='lower right', bbox_to_anchor=(0.3, 1))

#determinando a média da dureza para todo o DataFrame
media_geral_dureza = df['Dureza'].sum() / df.shape[0]

#adicionando a figura que criará o gráfico
plt.figure(4)
#Gráfico de dispersão da dureza em comparação a média 
plt.scatter(range(len(df['Dureza'])), df['Dureza'], label='Dados')
plt.axhline(y=media_geral_dureza, color='red', linestyle='--', label='Valor Médio Fixo')
#Rótulo do eixo X e Y, e título
plt.title('Dispersão da dureza')
plt.ylabel('Dureza')
plt.xlabel('Número da linha')
# Criando uma legenda personalizada
legenda = "Estilo da linha: '--'\nSignificado: Média dos dados"
# Adiciona a legenda ao gráfico
plt.legend([legenda], loc='lower right', bbox_to_anchor=(0.3, 1))

#determinando a média do sólido para todo o DataFrame
media_geral_sólidos = df['Sólidos'].sum() / df.shape[0]
#adicionando a figura que criará o gráfico
plt.figure(5)
#Gráfico de dispersão do sólido em comparação a média
plt.scatter(range(len(df['Sólidos'])), df['Sólidos'], label='Dados')
plt.axhline(y=media_geral_sólidos, color='red', linestyle='--', label='Valor Médio Fixo')
#Rótulo do eixo X e Y, e título
plt.title('Dispersão do sólido')
plt.ylabel('Sólidos')
plt.xlabel('Número da linha')
# Criando uma legenda personalizada
legenda = "Estilo da linha: '--'\nSignificado: Média dos dados"
# Adiciona a legenda ao gráfico
plt.legend([legenda], loc='lower right', bbox_to_anchor=(0.3, 1))

#determinando a média da cloramina para todo o DataFrame
media_geral_cloraminas = df['Cloraminas'].sum() / df.shape[0]
#adicionando a figura que criará o gráfico
plt.figure(6)
#Gráfico de dispersão da cloramina em comparação a média 
plt.scatter(range(len(df['Cloraminas'])), df['Cloraminas'], label='Dados')
plt.axhline(y=media_geral_cloraminas, color='red', linestyle='--', label='Valor Médio Fixo')
#Rótulo do eixo X e Y, e título
plt.title('Dispersão da cloramina')
plt.ylabel('Cloraminas')
plt.xlabel('Número da linha')
# Criando uma legenda personalizada
legenda = "Estilo da linha: '--'\nSignificado: Média dos dados"
# Adiciona a legenda ao gráfico
plt.legend([legenda], loc='lower right', bbox_to_anchor=(0.3, 1))

#determinando a média do sulfato para todo o DataFrame
media_geral_sulfato = df['Sulfato'].sum() / df.shape[0]
#adicionando a figura que criará o gráfico
plt.figure(7)
#Gráfico de dispersão do sulfato em comparação a média
plt.scatter(range(len(df['Sulfato'])), df['Sulfato'], label='Dados')
plt.axhline(y=media_geral_sulfato, color='red', linestyle='--', label='Valor Médio Fixo')
#Rótulo do eixo X e Y, e título
plt.title('Dispersão do sulfato')
plt.ylabel('Sulfato')
plt.xlabel('Número da linha')
# Criando uma legenda personalizada
legenda = "Estilo da linha: '--'\nSignificado: Média dos dados"
# Adiciona a legenda ao gráfico
plt.legend([legenda], loc='lower right', bbox_to_anchor=(0.3, 1))

#determinando a média do carbono organico para todo o DataFrame
media_geral_Carbono_organico = df['Carbono organico'].sum() / df.shape[0]
#adicionando a figura que criará o gráfico
plt.figure(8)
#Gráfico de dispersão do carbono orgânico em comparação a média
plt.scatter(range(len(df['Carbono organico'])), df['Carbono organico'], label='Dados')
plt.axhline(y=media_geral_Carbono_organico, color='red', linestyle='--', label='Valor Médio Fixo')
#Rótulo do eixo X e Y, e título
plt.title('Dispersão do carbono orgânico')
plt.ylabel('Carbono orgânico')
plt.xlabel('Número da linha')
# Criando uma legenda personalizada
legenda = "Estilo da linha: '--'\nSignificado: Média dos dados"
# Adiciona a legenda ao gráfico
plt.legend([legenda], loc='lower right', bbox_to_anchor=(0.3, 1))


#determinando a média do trihalometano para todo o DataFrame
media_geral_trihalometanos = df['Trihalometanos'].sum() / df.shape[0]
#adicionando a figura que criará o gráfico
plt.figure(9)
#Gráfico de dispersão do trihalometano em comparação a média
plt.scatter(range(len(df['Trihalometanos'])), df['Trihalometanos'], label='Dados')
plt.axhline(y=media_geral_trihalometanos, color='red', linestyle='--', label='Valor Médio Fixo')
#Rótulo do eixo X e Y, e título
plt.title('Dispersão do trihalometano')
plt.ylabel('Trihalometanos')
plt.xlabel('Número da linha')
# Criando uma legenda personalizada
legenda = "Estilo da linha: '--'\nSignificado: Média dos dados"
# Adiciona a legenda ao gráfico
plt.legend([legenda], loc='lower right', bbox_to_anchor=(0.3, 1))


#determinando a média da turbidez para todo o DataFrame
media_geral_turbidez = df['Turbidez'].sum() / df.shape[0]
#adicionando a figura que criará o gráfico
plt.figure(10)
#Gráfico de dispersão da turbidez em comparação a média 
plt.scatter(range(len(df['Turbidez'])), df['Turbidez'], label='Dados')
plt.axhline(y=media_geral_turbidez, color='red', linestyle='--', label='Valor Médio Fixo')
#Rótulo do eixo X e Y, e título
plt.title('Dispersão da turbidez')
plt.ylabel('Turbidez')
plt.xlabel('Número da linha')
# Criando uma legenda personalizada
legenda = "Estilo da linha: '--'\nSignificado: Média dos dados"
# Adiciona a legenda ao gráfico
plt.legend([legenda], loc='lower right', bbox_to_anchor=(0.3, 1))
plt.show()

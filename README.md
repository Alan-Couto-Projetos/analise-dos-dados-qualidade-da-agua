# analise-dos-dados-qualidade-da-agua

dados retirados de https://www.kaggle.com/datasets/abhishekkhanna004/water-quality-dataset-for-crop

Dados da faixa de valores de ph com a maior taxa de nutrientes para o solo usado como medida para a análise
https://extensao.cecierj.edu.br/material_didatico/geo09/popups/ph.htm#:~:text=Os%20solos%20t%C3%AAm%2C%20geralmente%2C%20pH,pH%20acima%20de%207%2C%20alcalinos.

Atenção a unidade de medida para as colunas do DataSet não foi especificado, logo a análise feita foi apenas para prática, pois os dados estão sujeitos a erros devido a conversão de unidade de medida que deveria ser realizada para obter precisão na comparação dos dados.

O nível ideal de trihalometanos, cloraminas, carbono orgânico na água para irrigação não é especificamente determinado, não vou realizar toda a análise para essas colunas, e vou gerar apenas o gráfico de dispersão delas, ademais para as outras colunas foi possível encontrar valores recomendados.

Nesse projeto vou dar uma ênfase em analisar os dados da coluna de PH, pois creio que os valores dessa coluna seguem a escala de PH que é normalmente utilizada na química, e na minha pesquisa não encontrei nada que determine que a unidade de medida do PH muda para outros países. Tendo em vista tudo isso os processos que realizei no código estão listados abaixo:

    1 - Excluindo os valores nulos.
    2 - Tradução dos nomes das colunas para PT/BR.
    3 - Excluir a coluna check.
    4 – Arquivo CSV com dados tratados para uso nos passos seguintes.
    5 - Gerar os seguintes gráficos:
	    1 - Gerar um gráfico que exiba a faixa dos valores de PH com mais nutrientes no solo junto com a contagem do total de valores que corresponde a aquela faixa de PH.

	    2 - Gerar um gráfico que mostre os valores que estão acima, abaixo e igual a média dos valores recomendados de PH com mais nutrientes no solo.

	    3 - Gerar um gráfico da dispersão dos valores para cada colunas do DataFrame em comparação com o valor médio da respectiva coluna.
     
É necesário primeiro realizar a execução do código de tratamento_dos_dados.py para conseguir obter o arquivo que será utilizado no código de Análise_dos_dados.py.

Todo o projeto foi desenvolvido pelo Visual Studio Code, com isso em vista a versão do python e das bibliotecas usadas deve ser especificadas, vou deixar o passo a passo de como criar um ambiente virtual pelo Visual Studio Code com a versão correta do python e demais bibliotecas para evitar eventuais erros no código devido a novas atualizações.

Dowloand do Visual Studio Code, siga os passos listados:

    1 - Acesse o site oficial do Visual Studio Code em https://code.visualstudio.com/
    2 - Clique no botão "Download" para baixar o instalador apropriado para o seu sistema operacional (Windows, macOS ou Linux).
    3 - Execute o instalador e siga as instruções para instalar o VS Code no seu computador.
    4 - Abra o VS Code após a instalação.
  
    Vá para a aba extensão  na barra lateral à esquerda e procure por "Python". Se você não encontrar essa aba você pode abrir usando ctrl+shift+x.
  
    Após instalar a extensão Python, você verá um ícone de engrenagem no canto superior direito do VS Code. Clique nele e selecione "Python: Select Interpreter". Isso permite que 	você escolha a versão do Python que deseja usar, mas para isso você precisa baixar a versão utlizada nesse projeto, para fazer isso acesse o site https://www.python.org/downloads/ e instale a versão python==3.11.4.

Para testar o código é necessário criar um ambiente virtual com as versões das bibliotecas utilizadas no projeto, para isso copie e cole um a um o código a seguir no terminal do Visual Studio Code:

    Abra o terminal integrado no Visual Studio Code no Windows ou Linux com o atalho Ctrl+', e no Mac Cmd + ', ou pelo menu View(Ver)> terminal.
    
    # Criando um ambiente virtual
    No macOS ou Linux:
    python -m venv myenv
    
    No Windows:
    python -m venv myenv
    
    
    
    # Ativando o ambiente virtual
    No macOS ou Linux:
    source myenv/bin/activate
    
    No Windows:
    .\myenv\Scripts\activate
    
    Obs.: Talvez o powershell não permita a ativação do ambiente, então execute os passos a seguir:
    
    1 - Abra o Prompt de Comando como administrador. Para fazer isso, pressione Win+X e escolha "Prompt de Comando 	(Admin)" no Windows, ou clique em win e pesquise por prompt de 
            comando, clique com o botão direito e execute como administrador.
    
    2 - Navegue até a pasta do seu ambiente virtual:
    cd caminho\para\pasta\Scripts (para isso vá até a pasta e clique com o botão direito na região do topo da página que exiba algo parecido com arquivos > nome da pasta).
    
    3 - Execute activate:
    activate
    
    Isso ativará o ambiente virtual usando o prompt de comando.
    
    # Instalando as dependências
    pip install -r requisitos.txt
    
    #execute o teste do arquivo
    python Tratamento_dos_dados.py
    
    Após testar o código você pode desativar o ambiente virtual usando o comando deactivate no macOS e no Linux, ou .\myenv\Scripts\deactivate no Windows.  

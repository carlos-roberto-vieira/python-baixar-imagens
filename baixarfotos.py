import requests
from requests.models import Response
import pandas as pd

def baixar_arquivos( url, endereco ):
    # faz a requisicao ao servidor
    resposta = requests.get( url )
    with open( endereco, 'wb' ) as novo_arquivo:
        novo_arquivo.write( resposta.content )
      
      
tabela = pd.read_excel( 'fotos.xlsx' )
df =pd.DataFrame( tabela, columns=['codigo','link'] )

for row in df.itertuples():
    print( row.codigo, row.link )
    imagem = str(row.codigo )+ '.jpg'
    baixar_arquivos( row.link, imagem )

 
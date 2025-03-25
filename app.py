import fitz #PyMuPDF
import nltk #Processamento de linguagem natural
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation

#Baixar pacotes necessários do NLTK
nltk.download('punkt')
nltk.download('spotwords')

def ler_pdf(caminho_pdf):
    '''Lê e extrai texto de um arquivo PDF.'''
    documento = fitz.open(caminho_pdf)
    texto = ""

    #Itera sobre cada página do documento
    for pagina in documento:
        texto += pagina.get_text("text") + " "

    
    documento.close()

    #Limpeza inicial do texto
    texto = texto.replace('\n',' ').replace('\t',' ').strip()
    return texto if texto else "Nenhum texto extraído."
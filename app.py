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

def resumir_texto(texto, tamanho_resumo=5):
    '''Gera um resumo utilizando a frequência de palavras para selecionar frases mais relevantes.'''
    frases = sent_tokenize(texto)

    #Se o resumo for maior que as frases -> texto curto demais
    if len(frases) < tamanho_resumo:
        return "Texto muito curto para resumir."
    
    #Remover stopwords e pontuação
    stop_words = set(stopwords.words('portuguese'))
    palavras = word_tokenize(texto.lower())
    palavras_filtradas = [palavra for palavra in palavras if palavra not in stop_words and palavra not in punctuation]

    #Calcula a frequência das palavras
    frequencia = nltk.FreqDist(palavras_filtradas)

    #Pontua as frases com base na frequência das palavras
    pontuacao_frases = {}
    for frase in frases:
        for palavra in word_tokenize(frase.lower()):
            if palavra in frequencia:
                pontuacao_frases[frase] = pontuacao_frases.get(frase, 0) + frequencia[palavra]

    #Ordena frases pela pontuação e seleciona as mais relevantes
    frases_importantes = sorted(pontuacao_frases, key=pontuacao_frases.get, reverse=True)
    resumo = ' '.join(frases_importantes[:tamanho_resumo])
    return resumo
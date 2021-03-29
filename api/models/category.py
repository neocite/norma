import nltk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import tokenize
from string import punctuation
import unidecode
from os.path import join


headlines = pd.read_csv(join('data', 'manxetes.csv'), delimiter=";")

regressao_logistica = LogisticRegression()


class Classificacao:
    def __init__(self, score, category_id):
        self.score = score
        self.category_id = category_id


def classificar_texto(vetorizar, texto, coluna_texto, coluna_classificacao, text_predicao):
    bag_of_words = vetorizar.fit_transform(texto[coluna_texto])
    predict_bag_of_words = vetorizar.transform([text_predicao]).toarray()
    treino, teste, class_treino, classe_test = train_test_split(bag_of_words,
                                                                texto[coluna_classificacao],
                                                                random_state=42)

    regressao_logistica.fit(treino, class_treino)
    acuracia = regressao_logistica.score(teste, classe_test)
    predicao = regressao_logistica.predict(predict_bag_of_words)

    classificacao = Classificacao(acuracia, predicao)

    return classificacao


def remove_palavras_irrelevantes(dataframe, coluna_texto):
    palavras_irrelevantes = nltk.corpus.stopwords.words("portuguese")
    frase_processada = list()
    token_espaco = tokenize.WhitespaceTokenizer()
    for opiniao in dataframe[coluna_texto]:
        nova_frase = list()
        palavras_texto = token_espaco.tokenize(opiniao)
        for palavra in palavras_texto:
            if (palavra not in palavras_irrelevantes):
                nova_frase.append(palavra)
        frase_processada.append(' '.join(nova_frase))

    return frase_processada


def remove_pontuacoes(dataframe, coluna_texto):
    stemmer = nltk.RSLPStemmer()
    pontuacoes = list()
    for pontuacao in punctuation:
        pontuacoes.append(pontuacao)

    frase_processada = list()
    token_pontuacao = tokenize.WordPunctTokenizer()
    for opiniao in dataframe[coluna_texto]:
        nova_frase = list()
        palavras_texto = token_pontuacao.tokenize(opiniao)
        for palavra in palavras_texto:
            if (palavra not in pontuacoes):
                nova_frase.append(stemmer.stem(palavra))
        frase_processada.append(' '.join(nova_frase))

    return frase_processada


def remove_acentos(dataframe, coluna_texto):
    frase_processada = [unidecode.unidecode(
        texto.lower()) for texto in dataframe[coluna_texto]]
    return frase_processada


def download_nltk():
    nltk.download("all")


def classify(predict_text):

    headlines["trat_1"] = remove_acentos(
        headlines, "classificacao")

    headlines["trat_2"] = remove_palavras_irrelevantes(
        headlines, "trat_1")

    headlines["trat_3"] = remove_pontuacoes(
        headlines, "trat_2")

    tfid_vectorizer = TfidfVectorizer()

    classificacao = classificar_texto(
        tfid_vectorizer,
        headlines,
        "classificacao",
        "category_id",
        predict_text)

    return classificacao

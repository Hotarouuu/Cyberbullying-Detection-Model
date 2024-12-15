import numpy as np
import ollama
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


class SYAEmbedding(BaseEstimator, TransformerMixin):
    def __init__(self, model_name="nomic-embed-text"):
        self.model_name = model_name

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Verifica se X é uma Series
        if isinstance(X, pd.Series): # Para processar grande quantidade de dados
            X = X.values  # Converte a Series para um array de valores
       

            response = []
            for frases in X:
                f1 = ollama.embeddings(model=self.model_name, prompt=frases)
                response.append(f1)

            words = []
            for responses in response:
                words.append(responses['embedding'])

            words = np.array(words)
            return words
        else: # Para processar dados de entrada unicos
            f2 = ollama.embeddings(model='nomic-embed-text', prompt=X)  # Processa o texto (NLP)
    

            w1 = f2['embedding'] # Extrai o vetor de embeddings da resposta
            
            w1 = np.array(w1) # Transforma a lista de vetores em um array numpy, para maior eficiência
            

            X1 = w1.reshape(1, -1)  # Através de um modelo treinado de PCA diminuimos as dimensões da array de vetores. Além de permitir rodarmos o modelo pois foi assim que ele foi treinado, diminuimos a necessidade de recursos computacionais robustos
            
            return X1
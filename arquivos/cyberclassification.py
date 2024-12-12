import numpy as np
import ollama
from sklearn.decomposition import PCA
import warnings



def pipeline2(mensagem, modeloembedding, pce):
    # Pipeline para ativação do modelo

    warnings.filterwarnings("ignore")  # Ignora os warnings que não vão impactar no uso do modelo

   
    f2 = ollama.embeddings(model='nomic-embed-text', prompt=mensagem)  # Processa o texto (NLP)
    

    w1 = f2['embedding'] # Extrai o vetor de embeddings da resposta
    
    w1 = np.array(w1) # Transforma a lista de vetores em um array numpy, para maior eficiência
    

    X1 = pce.transform(w1.reshape(1, -1))  # Através de um modelo treinado de PCA diminuimos as dimensões da array de vetores. Além de permitir rodarmos o modelo pois foi assim que ele foi treinado, diminuimos a necessidade de recursos computacionais robustos
    
    resposta = modeloembedding.predict(X1)
    
    if resposta == 1:
        print('This message is not allowed')
    else:
        print('Pass')

# Modelo de Detecção de Cyberbullying em Mensagens

## Início

Esse é projeto visado em criar um modelo de classificação para processar textos em mensagens e classificar se é uma mensagem agressiva ou não-agressiva. 

## Descrição

Esse projeto, visando contribuir com a detecção de Cyberbullying na internet, utiliza o dataset "Cyberbullying Detection Dataset for Online Content" disponilizado no Kaggle para o treinamento.
O processo para o desenvolvimento do modelo pode ser separado em:

- Pré-Analise dos dados
- Processamento de Linguagem Natural
- Embedding
- Treinamento utilizando o algoritmo RandomForest do Scikit-learn
- Validação cruzada
- Teste com dados novos

Para melhor performance no modelo, utilizamos o modelo de embedding chamado 'nomic-embed-text' juntamente do Ollama (Ollama e não Llama) para rodar ele no código de maneira mais simples.

Dentro do arquivo Jupyter Notebook, onde foi gerado o modelo final, tem explicações em texto de pensamentos e processos. Peço desculpas se não houver muito entendimento dos meus textos, já que usei muito para visualização das minhas ideias.

## Tecnologias usadas

- Linguagem Python
- Bibliotecas: Ollama, Scikit-learn, Numpy, nltk
- Modelo de Embedding: 'nomic-embed-text'
- Jupyter Notebook
  

# Modelo de Detecção de Cyberbullying em Mensagens

## Início

Este é um projeto voltado para a criação de um modelo de classificação, denominado SYA-D1, com o objetivo de processar mensagens de texto e classificá-las como agressivas ou não-agressivas.

## Descrição

Esse projeto, visando contribuir com a detecção de Cyberbullying na internet, utiliza o dataset "Cyberbullying Detection Dataset for Online Content" disponilizado no Kaggle para o treinamento.

O processo para o desenvolvimento do SYA-D1 pode ser separado em:

- Pré-Analise dos dados
- Processamento de Linguagem Natural
- Embedding
- Treinamento utilizando o algoritmo RandomForest do Scikit-learn
- Validação cruzada
- Teste com dados novos

Para melhor performance no SYA-D1, foi utilizado o modelo de embedding chamado 'nomic-embed-text' juntamente do Ollama (Ollama e não Llama) para rodar ele no código de maneira mais simples.


## Tecnologias usadas

- Linguagem Python
- Bibliotecas: Ollama, Scikit-learn, Numpy, Pandas, NLTK
- Modelo de Embedding: 'nomic-embed-text'
- Jupyter Notebook

## Como usar?

O SYA-D1 foi treinado através de etapas e cada etapa é crucial para que o modelo possa classificar os dados que você deseja. No nosso caso os dados são mensagem, textos em linguagem natural.

Para isso você deve seguir as seguintes etapas:

- Embedding dos dados
- Transformar a lista retornada pelo Embedding em um array numpy para melhor performance
- Uso do PCA, disponibilizado como modelo também, para diminuir as dimensões do array de vetores

As etapas descritas são essenciais para o correto funcionamento do SYA-D1, porém, eu ofereço uma solução mais simples:

Juntamente com os modelos, forneci dois arquivos .py. O primeiro contém uma função que simplifica o uso do modelo, tornando a implementação mais fácil, mas também pode servir como base para outros códigos. O segundo arquivo é dedicado a testar o modelo de forma isolada.

## Avisos Importantes

- Os arquivos fornecidos podem ser modificados ou usados como base para a criação do seu código. No entanto, é importante destacar que as etapas descritas são obrigatórias para o funcionamento do SYA-D1. Se não forem seguidas corretamente, o modelo não funcionará.
- O PCA foi treinado e ajustado especificamente para os dados de treinamento, portanto, também é obrigatório para garantir um desempenho adequado do SYA-D1. Sem ele, a performance do modelo será comprometida.
- Como mencionado, o modelo de embeddings utilizado foi o nomic-embed-text em conjunto com o Ollama. Embora seja recomendado usar essa configuração, você tem liberdade para testar com outros modelos de embeddings, se desejar.


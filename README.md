# Modelo de Detecção de Cyberbullying em Mensagens

![istockphoto-1498830411-612x612](https://github.com/user-attachments/assets/bc8b682b-5064-4e76-8b05-4daa2f2a4988)


## Início

Este é um projeto voltado para a criação de um modelo de classificação, denominado SYA-D2, com o objetivo de processar mensagens de texto e classificá-las como agressivas ou não-agressivas.

## Descrição

Esse projeto, visando contribuir com a detecção de Cyberbullying na internet, utiliza o dataset "Cyberbullying Detection Dataset for Online Content" disponilizado no Kaggle para o treinamento.

O processo para o desenvolvimento do SYA-D2 pode ser separado em:

- Pré-Analise dos dados
- Embedding (NLP)
- Treinamento utilizando Rede Neural (MultiLayer Perceptron Classifier) do Scikit-learn
- Validação cruzada
- Teste com dados novos

Para melhor performance no SYA-D2, foi utilizado o modelo de embedding chamado 'nomic-embed-text' juntamente do Ollama (Ollama e não Llama) para rodar ele no código de maneira mais simples.


## Tecnologias usadas

- Linguagem Python
- Bibliotecas: Ollama, Scikit-learn, Numpy, Pandas
- Modelo de Embedding: 'nomic-embed-text'
- Jupyter Notebook

## Como usar?

O SYA-D2 foi treinado através de etapas e cada etapa é crucial para que o modelo possa classificar os dados que você deseja. No nosso caso os dados são mensagem, textos em linguagem natural.

Para isso você deve seguir as seguintes etapas:

- Baixa o Ollama no seu ambiente 
- Após baixar o Ollama baixe o modelo de embedding através do comando "ollama pull nomic-embed-text"
- Importe a classe SYAEmbedding do arquivo "embedding"
- Importe o modelo usando a biblioteca joblib dentro do seu código
- Caso necessário teste usando o arquivo de teste incluso na pasta arquivo

As etapas descritas são essenciais para o correto funcionamento do SYA-D2.


## Avisos Importantes

- Como mencionado, o modelo de embeddings utilizado foi o nomic-embed-text em conjunto com o Ollama. Embora seja recomendado usar essa configuração, você tem liberdade para testar com outros modelos de embeddings, se desejar. Basta modificar a classe.
- O modelo SYA-D2 foi treinado com um número limitado de dados, aproximadamente 40.000 linhas, devido a restrições computacionais. Embora esteja em uma fase inicial de desenvolvimento, sua arquitetura é mais avançada em comparação com o modelo SYA-D1. Com o tempo, o SYA-D2 será constantemente aprimorado e atualizado para melhorar seu desempenho e precisão.
- Atualmente o SYA-D2 apenas está disponível em inglês. Em breve será atualizado para português do Brasil.
- As resposta dos SYA-D2 são 1 para detecção de mensagens agressivas e 0 para não agressivas.

## Contato

Para mais informações sobre este projeto, você pode me contatar:

LinkedIn: [Seu LinkedIn](http://linkedin.com/in/lucas-moraes-4b3a30284)


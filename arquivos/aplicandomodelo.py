import joblib

modelo = joblib.load(r'G:\Meu Drive\ESTUDOS\PROJETOS PESSOAIS\Cyberbulling Project\modelos\SYA-D1.pkl')
PCA = joblib.load(r'G:\Meu Drive\ESTUDOS\PROJETOS PESSOAIS\Cyberbulling Project\modelos\pce.pkl')

# Não é possível usar o modelo sem tratar os dados, pois esse modelo classifica textos em string através de NLP. Vamos importar funções que façam isso

from cyberclassification import pipeline2

# O modelo possui duas saídas: Pass e This message is not allowed
# Pass significa que não é agressivo e o outro que é agressivo

mensagem = input('Qual sua mensagem? \n').lower()

resposta = pipeline2(mensagem, modelo, PCA)


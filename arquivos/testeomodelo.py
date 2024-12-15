import joblib
from embedding import SYAEmbedding


SYAD2 = joblib.load('Modelo')

mensagem = "I honestly don’t know what’s wrong with you sometimes. It’s like every time I try to help, you just turn around and make things worse. Why can’t you just listen for once and not make a complete mess of things? It’s so frustrating because I know you’re capable of better, but it’s like you just choose to be stubborn. It really gets to me sometimes, how you act like everything is fine when it’s clear that you’re just avoiding the truth. But, I also know that deep down, you’re a good person. You’ve helped me when no one else would, and there have been times when you’ve shown such incredible kindness and support. I remember when you stayed up all night to help me with my project, even when you were exhausted. That means the world to me. You have so much potential, and I really believe you can do great things if you stop letting your own doubts get in the way. I know you don’t always see it, but I see how much you care, and that’s something I truly admire.But seriously, sometimes your actions don’t match your heart, and it’s maddening. I hate seeing you struggle when I know you could have made things so much easier on yourself. I’m not giving up on you, though. I still believe in you. I just wish you would see how much you’re hurting yourself by not facing things head-on. You’re better than that, and I’ll keep reminding you, even if it takes a thousand tries."
resposta = SYAD2.predict(mensagem)

if resposta == 1:
    print('Mensagem agressiva')
else:
    print('Resposta permitida')
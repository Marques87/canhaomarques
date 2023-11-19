import time 
import math
g = float(10)

#AQUI É BASICAMENTE UMA CONVERSA COM O USER, NADA IMPORTANTE

print("Olá, caro espectador.")
time.sleep(2)
print("Você sabia que está conversando com uma inteligência artificial? Incrível né? (:")
time.sleep(2)
print("Espero que goste da nossa conversa.")
time.sleep(2)
print("Esse programa basicamente vai fazer uns cálculos aí, sou esperto e você também, então você já deve saber o que ele faz.")
time.sleep(2)
print("Eu sei que você sabe.")
time.sleep(2)

#O USER DÁ AS INFOS NECESSÁRIAS.

cordx = float(input("Primeiro coloque o valor da coordenada x: \n"))
cordy = float(input("Agora coloque o valor da coordenada y: \n"))
força = float(input("Insira a força em newtons: \n"))
angulo = float(input("Por último, coloque o ângulo em graus: \n"))

angulorad = math.radians(angulo)
seno = math.sin(angulorad)
cosseno = math.cos(angulorad)

print("Espere a magia acontecer... Esqueci de dizer que a bala tem 0.5kg, blz?")
time.sleep(2)

massa = 0.5
def veloini():
    veini = força / massa
    return veini

print(f"A velocidade inicial é: {veloini()}")

#ESSAS FUNÇÕES CALCULAM A VELOCIDADE INICIAL Y E O TEMPO MÁXIMO.

def veloiniy():
    veliniy = veloini() * seno
    return veliniy

def tempomax():
    iy = 2 * veloiniy()
    iym = iy / g
    return iym 

print(f"O tempo total de voo é: {tempomax():.4f}")

# ESSAS FUNÇÕES CALCULAM A VELOCIDADE INICIAL X E O XMAX (Horizontal)

def veloinix():
    ui = veloini() * cosseno
    return ui
velox = veloinix()


def xmax():
    uin = veloinix() * tempomax()
    uin2 = cordx + uin
    return uin2 

print(f"Local de queda: {xmax():.4f}")

#VELOCIDADE VERTICAL E HORIZONTAL EM CADA INSTANTE DO VOO


finalizar2 = False
finalizar = False

while(not finalizar2):
    o = input("Digite y para colocar um tempo específico para o tamanho da lista (lembre que o limite é o tempo máximo)")
    if o == "y":
        finalizar2 = True
        while(not finalizar):
            t = float(input("Digite aqui o tempo que você quer (lembre que o limite é o tempo máximo): "))
            if t < tempomax():
                finalizar = True
           
                def veloy1(t):
                    g_local = -g
                    haha = g_local * t
                    veloy22 = veloiniy() + haha
                    return veloy22
            print(f"A velocidade y nesse tempo é: {veloy1(t):.4f}")
        else:
            print("Escreva um número menor do que o tempo máximo.")




print(f"A velocidade horizontal é {veloinix():.3f}")

def dist():
    my = xmax() - cordx
    return my 

print(f"A distância entre o ponto de lançamento e local da queda: {dist():.3f}")

import time 
import math
g = float(10)

velocidades_y = []

#LOOP QUE CALULA AS VELOCIDADES EM CASA INSTANTE O VOO

for t in range(int(tempomax()) + 1):
    vel_y = veloy1(t)
    velocidades_y.append(vel_y)

#IMPRIME AS VELOCIDADES DE Y EM CADA INSTANTE DO VOO

print("Velocidades de y em cada instante do voo:")
for t, vel_y in enumerate(velocidades_y):
    print(f"\tTempo {t}: Velocidade y = {vel_y:.4f}")

print(f"a distancia alcançada foi de: {xmax():.3f}")
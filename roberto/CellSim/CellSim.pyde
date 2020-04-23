from Simulazione import Simulazione
from Fiore import Fiore
import random


DIM_CAMPO = 50
DIM_CELLA = 10
INDICE_SOPRAVVIVENZA = 0.55
APE_MAX_DIST = 5
PROB_MUTAZIONE = 0.05

VELOCITA_ESECUZIONE = 100

simulazione = Simulazione(DIM_CAMPO, DIM_CELLA, INDICE_SOPRAVVIVENZA, APE_MAX_DIST, PROB_MUTAZIONE)

def setup():
    size(DIM_CAMPO*DIM_CELLA + 1, DIM_CAMPO*DIM_CELLA + 1)
    
    random.seed('seed_costante')
    
    done_x = []
    done_y = []
    for i in range(5):
        while True:
            x = random.randint(1, DIM_CAMPO - 1)
            y = random.randint(1, DIM_CAMPO - 1)
            if x not in done_x or y not in done_y:
                break
        done_x += [x, x - 1]
        done_y += [y, y - 1]
        
        fiore1 = Fiore()
        fiore2 = Fiore(fiore1.get_alleli())
        simulazione.aggiungi_fiore_con_ape(fiore1, x, y)


ultimo_avanzamento = 0;
finish = False
def draw():
    global ultimo_avanzamento
    global finish
    
    if not finish:
        if millis() - ultimo_avanzamento > VELOCITA_ESECUZIONE:
            ultimo_avanzamento = millis()
            if not simulazione.avanza_generazione():
                print('STOP!')
                finish = True
            
    simulazione.disegna()   

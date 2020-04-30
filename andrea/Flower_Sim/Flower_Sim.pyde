from Simulator import Simulator

sim = Simulator()
sim.initializeFlowers()

def setup():
    size((sim.sett.MATRIX_SIZE)*(sim.sett.FLOWER_SIZE) + 1, (sim.sett.MATRIX_SIZE)*(sim.sett.FLOWER_SIZE) + 1)
    # per evitare che venga richiamata 
    # piu volte in loop draw()
    noLoop() 
    

def draw():
    sim.field.render()
    
def keyPressed():
    if(keyCode == UP):
        sim.next_gen()
        redraw()

from Campo import Campo
from Flower import Flower
from Bee import Bee
from Dna import Dna

MATRIX_SIZE = 200 # numero di "slot" nella matrice
FLOWER_SIZE = 7 # dimensione in pixel della singola cella

field = Campo(FLOWER_SIZE, MATRIX_SIZE)

for i in range(20):
    flower_1 = Flower(Dna('AAAAABBCCBAAAAA'), 5*i, 10)
    field.add_flower(flower_1)
    bee_1 = Bee(flower_1)
    field.add_bee(bee_1)

    flower_2 = Flower(Dna('AACBBBBBBBBBCCA'), 5*i, 30)
    field.add_flower(flower_2)
    bee_2 = Bee(flower_2)
    field.add_bee(bee_2)
    
    flower_3 = Flower(Dna('CCCCCCACCCCBBAA'), 5*i, 50)
    field.add_flower(flower_3)
    bee_3 = Bee(flower_3)
    field.add_bee(bee_3)

    flower_4 = Flower(Dna('BBABCCACCCCAAAB'), 5*i, 70)
    field.add_flower(flower_4)
    bee_4 = Bee(flower_4)
    field.add_bee(bee_4)

    flower_5 = Flower(Dna('BBBBCCAAAAAAAAB'), 5*i, 90)
    field.add_flower(flower_5)
    bee_5 = Bee(flower_5)
    field.add_bee(bee_5)


def setup():
    size(MATRIX_SIZE*FLOWER_SIZE + 1, MATRIX_SIZE*FLOWER_SIZE + 1)
    # per evitare che venga richiamata 
    # piu volte in loop draw()
    noLoop() 
    

def draw():
    field.render()
    
def keyPressed():
    if(keyCode == UP):
        for i in range(len(field.bees)):
            field.bees[i].myFlower.tryToSurvive(field)
            if(not(field.flowers[field.bees[i].myFlower.y][field.bees[i].myFlower.x] == None)):
                field.bees[i].combineFlowers(field, 10)
        redraw()

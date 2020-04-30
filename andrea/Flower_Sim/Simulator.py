from Settings import Settings
from Campo import Campo
from Flower import Flower
from Bee import Bee
from Dna import Dna

class Simulator:
    
    def __init__(self):
        self.sett = Settings()
        self.field = Campo(self.sett.FLOWER_SIZE, self.sett.MATRIX_SIZE)
        
    def initializeFlowers(self):
        for i in range(int(round((self.sett.MATRIX_SIZE-1)/10)-1)):
            flower_1 = Flower(Dna('AAAAABBCCBAAAAA'), int(round((self.sett.MATRIX_SIZE-1)/10)-1), 10*i)
            self.field.add_flower(flower_1)
            bee_1 = Bee(flower_1)
            self.field.add_bee(bee_1)
        
            flower_2 = Flower(Dna('AACBBBBBBBBBCCA'), 2*int(round((self.sett.MATRIX_SIZE-1)/10)-1), 10*i)
            self.field.add_flower(flower_2)
            bee_2 = Bee(flower_2)
            self.field.add_bee(bee_2)
            
            flower_3 = Flower(Dna('CCCCCCACCCCBBAA'), 3*int(round((self.sett.MATRIX_SIZE-1)/10)-1), 10*i)
            self.field.add_flower(flower_3)
            bee_3 = Bee(flower_3)
            self.field.add_bee(bee_3)
        
            flower_4 = Flower(Dna('BBABCCACCCCAAAB'), 4*int(round((self.sett.MATRIX_SIZE-1)/10)-1), 10*i)
            self.field.add_flower(flower_4)
            bee_4 = Bee(flower_4)
            self.field.add_bee(bee_4)
        
            flower_5 = Flower(Dna('BBBBCCAAAAAAAAB'), 5*int(round((self.sett.MATRIX_SIZE-1)/10)-1), 10*i)
            self.field.add_flower(flower_5)
            bee_5 = Bee(flower_5)
            self.field.add_bee(bee_5)
            
    def next_gen(self):
        for i in range(len(self.field.bees)):
            self.field.bees[i].myFlower.tryToSurvive(self.field)
            if(not(self.field.flowers[self.field.bees[i].myFlower.y][self.field.bees[i].myFlower.x] == None)):
                self.field.bees[i].combineFlowers(self.field, self.sett.REPRODUCTION_DISTANCE)

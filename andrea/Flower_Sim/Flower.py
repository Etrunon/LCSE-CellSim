import random
from Settings import Settings
from Dna import Dna

class Flower:
    def __init__(self, dna, x, y):
        self.dna = dna
        self.x = x
        self.y = y
        self.sett = Settings()
        
    def tryToSurvive(self, field):
        toss = random.randint(1, 100)
        if(toss < self.sett.DEATH_RATE):
            field[self.y, self.x] = None
            del self
            
    def similar(self, other):
        myTraits = self.dna.analizeTraits()
        otherTraits = other.dna.analizeTraits()
        difference = abs(myTraits[0] - otherTraits[0]) + abs(myTraits[1] - otherTraits[1]) + abs(myTraits[2] - otherTraits[2])
        return difference <= self.sett.SIMILARITY_VALUE
        
    def combineDna(self, other):
        newDna = ""
        for i in range(len(self.dna.traits)):
            if(i%2==0):
                newDna += self.dna.traits[i]
            else:
                newDna += other.dna.traits[i]
        return Dna(newDna)
            
    def getRed(self):
        numbOfA = self.dna.analizeTraits()[0]
        return numbOfA * 17
    
    def getGreen(self):
        numbOfB = self.dna.analizeTraits()[1]
        return numbOfB * 17
    
    def getBlue(self):
        numbOfC = self.dna.analizeTraits()[2]
        return numbOfC * 17

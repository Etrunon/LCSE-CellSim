from Flower import Flower
from Dna import Dna

class Bee:
    def __init__(self, flower):
        self.myFlower = flower
        
        
    def findFlower(self, field, max_distance):
        for i in range(-max_distance, max_distance):
            for j in range(-max_distance, max_distance):
                if(i != self.myFlower.x and j != self.myFlower.y and field.checkValidity(self.myFlower.y, self.myFlower.x, j, i)):
                    if(not(field.emptyField(self.myFlower.y + j, self.myFlower.x + i))):
                        if(self.myFlower.similar(field[self.myFlower.y + j, self.myFlower.x + i])):
                            return field[self.myFlower.y + j, self.myFlower.x + i]
        
        return field[self.myFlower.y, self.myFlower.x]
    
    def combineFlowers(self, field, max_distance):
        otherFlower = self.findFlower(field, max_distance)
        newPos = self.findNearEmptyPos(field, 10000)
        if(self.myFlower == otherFlower):
            newFlower = Flower(self.myFlower.dna, newPos[0], newPos[1])
        else:
            newFlower = Flower(self.myFlower.combineDna(otherFlower), newPos[0], newPos[1])
        field.add_flower(newFlower)
        field.add_bee(Bee(newFlower))
    
    def findNearEmptyPos(self, field, N):
        offset = -1
        #### While da controllare
        while(offset > -N):
            #riga in alto
            for i in range(offset, -offset):
                if(field.checkValidity(self.myFlower.y, self.myFlower.x, offset, i) and (field.emptyField(self.myFlower.y + offset, self.myFlower.x + i))):
                    return [self.myFlower.x + i, self.myFlower.y + offset]    
                if(field.checkValidity(self.myFlower.y, self.myFlower.x, i, offset) and (field.emptyField(self.myFlower.y + i, self.myFlower.x + offset))):
                    return [self.myFlower.x + offset, self.myFlower.y + i]
                if(field.checkValidity(self.myFlower.y, self.myFlower.x, -offset, i) and (field.emptyField(self.myFlower.y - offset, self.myFlower.x + i))):
                    return [self.myFlower.x + i, self.myFlower.y - offset] 
                if(field.checkValidity(self.myFlower.y, self.myFlower.x, i, -offset) and (field.emptyField(self.myFlower.y + i, self.myFlower.x - offset))):
                    return [self.myFlower.x - offset, self.myFlower.y + i]
            offset = offset - 1
        

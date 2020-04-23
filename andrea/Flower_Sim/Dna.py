class Dna:
    def __init__(self, traits):
        self.traits = traits
        
    def analizeTraits(self):
        numberOfA = 0;
        numberOfB = 0;
        numberOfC = 0;
        
        for trait in self.traits:
            if(trait == "A"):
                numberOfA += 1
            if(trait == "B"):
                numberOfB += 1
            if(trait == "C"):
                numberOfC += 1
        
        return [numberOfA, numberOfB, numberOfC]

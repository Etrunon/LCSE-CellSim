import math
from Fiore import Fiore


class Campo:
    def __init__(self, dim_campo):
        self.dim_campo = dim_campo
        self.griglia = [ [ None for i in range(dim_campo) ] for j in range(dim_campo) ] 
    
    
    def aggiungi_fiore(self, fiore, x, y):
        if self.griglia[y][x] is not None:
            raise Exception('Aggiunta di un fiore in una cella gia occupata')

        self.griglia[y][x] = fiore
    
    
    def rimuovi_fiore(self, x, y):
        if self.griglia[y][x] is None:
            raise Exception('Rimozione di un fiore in una cella gia vuota')

        self.griglia[y][x] = None
    
    
    def get_dim_campo(self):
        return self.dim_campo
    
        
    def get_coordinate(self, fiore):
        x = -1
        y = -1
        
        j = 0
        while j < self.dim_campo and y < 0:
            i = 0
            while i < self.dim_campo and x < 0:
                # confronto l'istanza!
                if self.griglia[j][i] is fiore: 
                    x = i
                    y = j
                i+=1
            j+=1

        return [x, y]
        
 
    def get_posizione(self, x, y):
        return self.griglia[y][x]

        
        

import random
from Campo import Campo
from Fiore import Fiore
class Ape:

    def __init__(self, campo, fiore, dist_max):
        self.campo = campo
        self.fiore = fiore
        self.dist_max = dist_max
        
    
    def get_fiore(self):
        return self.fiore
    
    
    def trova_fiori_vicini(self, fiore, max_dist):
        orig_x, orig_y = self.campo.get_coordinate(fiore)
        dim_campo = self.campo.get_dim_campo()
        
        min_x = max(0, orig_x - max_dist)
        max_x = min(dim_campo - 1, orig_x + max_dist)
        min_y = max(0, orig_y - max_dist)
        max_y = min(dim_campo - 1, orig_y + max_dist)
        
        fiori_vicini = []
        
        for j in range(min_y, max_y):
            for i in range(min_x, max_x):
                # non deve valutare il fiore d'origine!
                if i != orig_x or j != orig_y: 
                    el_in_posizione = self.campo.get_posizione(i, j)
                    if el_in_posizione is not None:
                        fiori_vicini.append(el_in_posizione)
        
        return fiori_vicini
    
    
    def trova_spazio_vuoto(self):
        orig_x, orig_y = self.campo.get_coordinate(self.fiore)
        dim_campo = self.campo.get_dim_campo()
        
        min_dist = dim_campo
        for index in range(1, dim_campo):
            slot_vuoti = []
            min_x = max(orig_x - index, 0)
            max_x = min(orig_x + index, dim_campo - 1)
            min_y = max(orig_y - index, 0)
            max_y = min(orig_y + index, dim_campo - 1)
            
            # orizzontale
            for x in range(min_x, max_x):
                # sopra
                if self.campo.get_posizione(x, min_y) is None:
                    slot_vuoti.append([x, min_y])
                # sotto
                if self.campo.get_posizione(x, max_y) is None:
                    slot_vuoti.append([x, max_y])
                    
            # verticale
            for y in range(min_y + 1, max_y - 1):
                # sinistra
                if self.campo.get_posizione(min_x, y) is None:
                    slot_vuoti.append([min_x, y])
                # destra
                if self.campo.get_posizione(max_x, y) is None:
                    slot_vuoti.append([max_x, y])

            if len(slot_vuoti) > 0:
                return random.choice(slot_vuoti)
        return [-1, -1]
    

    def impollina(self, prob_mutazione):
        fiori = self.trova_fiori_vicini(self.fiore, self.dist_max)
        
        if len(fiori) > 0:
            max_uguaglianza = -1
            fiore_max_uguaglianza = None
            for fiore in fiori:
                cur_uguaglianza = self.fiore.confronta(fiore)
                if cur_uguaglianza > max_uguaglianza:
                    max_uguaglianza = cur_uguaglianza
                    fiore_max_uguaglianza = fiore
            fiore_scelto = fiore_max_uguaglianza
        else:
            fiore_scelto = self.fiore
        
        fiore_figlio = Fiore(self.fiore.combina(fiore_scelto, prob_mutazione))
        fiore_figlio_x, fiore_figlio_y = self.trova_spazio_vuoto()
  
        return [fiore_figlio, fiore_figlio_x, fiore_figlio_y]   

        
        
            
        
            
                
            
            

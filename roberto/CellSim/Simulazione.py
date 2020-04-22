from Campo import Campo
from Fiore import Fiore
from Ape import Ape


class Simulazione:
    
    def __init__(self, dim_campo, dim_cella, indice_sopravvivenza, ape_max_dist, prob_mutazione):
        self.dim_campo = dim_campo
        self.dim_cella = dim_cella
        self.indice_sopravvivenza = indice_sopravvivenza
        self.ape_max_dist = ape_max_dist
        self.prob_mutazione = prob_mutazione
        self.campo = Campo(dim_campo)
        self.api = []
        
        
    def invecchia_fiori(self):
        fiori_rimossi = []
        for j in range(0, self.dim_campo):
            for i in range(0, self.dim_campo):
                el_in_posizione = self.campo.get_posizione(i, j)
                if el_in_posizione is not None and not el_in_posizione.sopravvive(self.indice_sopravvivenza):
                    fiori_rimossi.append(el_in_posizione)
                    self.campo.rimuovi_fiore(i, j)
        self.api = [ape for ape in self.api if ape.get_fiore() not in fiori_rimossi]
        return True
    
    
    def mobilita_api(self):
        nuove_api = []
        for ape in self.api:
            fiore, x, y = ape.impollina(self.prob_mutazione)
            if x < 0 or y < 0:
                return False
            self.campo.aggiungi_fiore(fiore, x, y)
            nuove_api.append(Ape(self.campo, fiore, self.ape_max_dist))
        self.api += nuove_api
        return True


    def avanza_generazione(self):
        ok = self.mobilita_api()
        if ok:
            ok = ok and self.invecchia_fiori()
        return ok
        
        
    def aggiungi_fiore_con_ape(self, fiore, x, y): 
        self.campo.aggiungi_fiore(fiore, x, y)
        self.api.append(Ape(self.campo, fiore, self.ape_max_dist))
    
      
    def disegna(self):
        # Pulisco l'immagine e imposto il colore di sfondo
        background(84, 158, 63)
        
        # Imposto il colore delle linee 
        noFill()
        stroke(99, 176, 77)
        
        max_dim = self.dim_campo * self.dim_cella
        
        # Disegno i separatori verticali
        for i in range(0, self.dim_campo):
            x_start = i * self.dim_cella
            y_start = 0
            x_end = x_start # la linea verticale mantiene x costante
            y_end = self.dim_campo * self.dim_cella
            line(x_start, y_start, x_end, y_end)
            
        # Disegno i separatori orizzontali
        for i in range(0, self.dim_campo):
            x_start = 0
            y_start = i * self.dim_cella
            x_end = self.dim_campo * self.dim_cella
            y_end = y_start # la linea orizzontale mantiene y costante
            line(x_start, y_start, x_end, y_end)
        
        # disegno i fiori
        noStroke()
        fill(255, 0, 0)
        for j in range(0, self.dim_campo):
            for i in range(0, self.dim_campo):
                if self.campo.get_posizione(i, j) is not None:
                    cur_fiore = self.campo.get_posizione(i, j)
                    fill(cur_fiore.get_colore())
                    
                    x = self.dim_cella * i + self.dim_cella / 2
                    y = self.dim_cella * j + self.dim_cella / 2
                    diametro = self.dim_cella
                    ellipse(x, y, diametro, diametro)

import random

INTENSITA_ALTA = 255
INTENSITA_MEDIA = 205
INTENSITA_BASSA = 155

class Fiore:
    
    # Il dna conterra varie tipologie di alleli: 
    #  - 'R', 'G', 'B', 'I', 'S' in caso di allele dominante 
    #  - 'r', 'g', 'b', 'i', 's' in caso di allele recessivo
    # Ogni fiore ha nel suo genoma 4 alleli, due per il colore (tra r/R, g/G, b/B) e due per l'intensita del colore (tra i/I, s/S).
    # 
    # Gli alleli che definisco colore e intensita verranno gestiti separatamente.
    # In entrambi i casi, in caso di presenza di allele dominante per il colore/intensita,
    # il colore/intensita del fiore sara definito solamente da quelli. 
    # Al contrario, in caso di assenza di allele dominante per il colore/intensita, 
    # il colore/intensita sara definito dagli alleli recessivi.
    # 
    # Colore:
    # - R: rappresenta il rosso
    # - G: rappresenta il verde
    # - B: rappresenta il blu
    # In caso di coppia di alleli dominanti/recessivi, il colore sara il mix dei due colori definiti dagli alleli.
    # (es. "RB" => viola; "RR" => rosso; "Rg" => rosso (solo R dominante!); "rg" => giallo)
    #
    # Intensita:
    # - I: rappresenta un colore intenso
    # - S: rappresenta un colore scuro
    # Come per il colore, in caso di coppia di alleli dominanti/recessivi, l'intensita 
    # sara un mix delle due intensita, producendo un intensita media.
    # (es. "II" => intenso; "Is" => intenso; "is" => media; "IS" => media; "iS" => scuro; "ss" => scuro) 
    #
    # Durante la combinazione verra sempre preso un allele a caso da un fiore e uno dall'altro, 
    # sia per il colore sia per l'intensita. Il risultato dell'unione sara sempre
    # un fiore con due alleli per il colore e due alleli per l'intensita.
    # Alcuni esempi:
    # "RgSs" (rosso scuro) + "BbIi" (blu intenso) = "RbSI" (rosso medio)
    # "RGsi" (giallo medio) + "rgSI (giallo medio) = "RrSi" (rosso scuro) 
    # "BBsi" (blu medio) + "BBsi" (blu medio) = "BBsi" (blu medio)

    def __init__(self, alleli=False):
        c = ['R', 'r', 'B', 'b']
        i = ['I', 'i', 'S', 's']
        if not alleli:
            self.alleli = random.choice(c) + random.choice(c) + random.choice(i) + random.choice(i)
        else:
            self.alleli = alleli
        

    def get_alleli(self):
        return self.alleli
    
    
    def get_colore(self):
        r = 0
        g = 0
        b = 0
        
        intensity = INTENSITA_MEDIA
        if 'I' in self.alleli and 'S' in self.alleli or 'i' in self.alleli and 's' in self.alleli:
            intensity = INTENSITA_MEDIA
        elif 'I' in self.alleli:
            intensity = INTENSITA_ALTA
        elif 'S' in self.alleli:
            intensity = INTENSITA_BASSA
        elif 'i' in self.alleli:
            intensity = INTENSITA_ALTA
        elif 's' in self.alleli:
            intensity = INTENSITA_BASSA
            
        if 'R' in self.alleli or 'G' in self.alleli or 'B' in self.alleli:
            if 'R' in self.alleli:
                r = intensity
            if 'G' in self.alleli:
                g = intensity
            if 'B' in self.alleli:
                b = intensity
        else:
            if 'r' in self.alleli:
                r = intensity
            if 'g' in self.alleli:
                g = intensity
            if 'b' in self.alleli:
                b = intensity
                
        return color(r, g, b)
    
        
    def sopravvive(self, indice_sopravvivenza):
        return random.random() < indice_sopravvivenza
    
    
    def confronta(self, fiore):
        fiore_1 = self.get_alleli()
        fiore_2 = fiore.get_alleli()
        
        indice_uguaglianza = 0
        for i in range(0, 4):
            indice_uguaglianza += 1 if fiore_1[i] == fiore_2[i] else 0
        
        return indice_uguaglianza
    
        
    def combina(self, fiore, prob_mutazione):
        genitore_1 = self.get_alleli()
        genitore_2 = fiore.get_alleli()
        figlio = genitore_1[random.randint(0, 1)] + genitore_2[random.randint(0, 1)] + genitore_1[random.randint(2, 3)] + genitore_2[random.randint(2, 3)]
        
        c = ['R', 'r', 'G', 'g', 'B', 'b']
        i = ['I', 'i', 'S', 's']
        if random.random() < prob_mutazione:
            indice_mutazione = random.randint(0, 3)
            if indice_mutazione < 2:
                figlio = figlio[:indice_mutazione] + random.choice(c) + figlio[indice_mutazione + 1:]
            else:
                 figlio = figlio[:indice_mutazione] + random.choice(i) + figlio[indice_mutazione + 1:]
        return figlio
         

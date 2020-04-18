class Matrix:
    def __init__(self, cell_size, matrix_size):
        self.cell_size = cell_size
        self.matrix_size = matrix_size
        
        self.cells = [[None for x in range(0, matrix_size)] for y in range(0, matrix_size)] 
                 

    def render(self):
        # Pulisco l'immagine e imposto il colore di sfondo
        background(0, 0, 0)
        
        # Imposto il colore delle linee 
        noFill()
        stroke(60, 60, 60)
        
        max_dim = self.matrix_size*self.cell_size
        
        # Disegno i separatori verticali
        for i in range(0, self.matrix_size):
            line(i*self.cell_size, 0, i*self.cell_size, max_dim)
            
        # Disegno i separatori orizzontali
        for i in range(0, self.matrix_size):
            line(0, i*self.cell_size, max_dim, i*self.cell_size)
            
        noStroke()
        fill(255, 0, 0)
        for j in range(0, self.matrix_size):
            for i in range(0, self.matrix_size):
                if self.cells[j][i] is not None:
                    ellipse(self.cell_size*i + self.cell_size/2, self.cell_size*j + self.cell_size/2, self.cell_size, self.cell_size)
        
                
    
    def add_cell(self, cell, x, y):
        self.cells[y][x] = cell

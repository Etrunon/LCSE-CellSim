class Campo:
    def __init__(self, flower_size, matrix_size):
        self.flower_size = flower_size
        self.matrix_size = matrix_size
        
        self.flowers = [[None for x in range(0, matrix_size)] for y in range(0, matrix_size)] 
        self.bees = []
                 

    def render(self):
        # Pulisco l'immagine e imposto il colore di sfondo
        background(0, 0, 0)
        
        # Imposto il colore delle linee 
        noFill()
        stroke(60, 60, 60)
        
        max_dim = self.matrix_size*self.flower_size
        
        # Disegno i separatori verticali
        for i in range(0, self.matrix_size):
            line(i*self.flower_size, 0, i*self.flower_size, max_dim)
            
        # Disegno i separatori orizzontali
        for i in range(0, self.matrix_size):
            line(0, i*self.flower_size, max_dim, i*self.flower_size)
            
        noStroke()
        for j in range(0, self.matrix_size):
            for i in range(0, self.matrix_size):
                if self.flowers[j][i] is not None:
                    fill(self.flowers[j][i].getRed(), self.flowers[j][i].getGreen(), self.flowers[j][i].getBlue())
                    ellipse(self.flower_size*i + self.flower_size/2, self.flower_size*j + self.flower_size/2, self.flower_size, self.flower_size)
        
    #####################################
    
    def add_flower(self, flower):
        self.flowers[flower.y][flower.x] = flower;
        
    def add_bee(self, bee):
        self.bees.append(bee)
        
    def checkValidity(self, y, x, j ,i):
        return x+i >= 0 and x+i <= self.matrix_size-1 and y+j >= 0 and y+j <= self.matrix_size-1
    
    def emptyField(self, y, x):
        return self[y, x] == None
        
    def __getitem__(self, couple):
        y, x = couple
        return self.flowers[y][x]

    def __setitem__(self, couple, newValue):
        y, x = couple
        self.flowers[y][x] = newValue

class Matrix:
    def __init__(self, settings):
        self.settings = settings

        self.cells = [[None for x in range(0, (settings.MATRIX_SIZE)+2)] for y in range(0, (settings.MATRIX_SIZE)+2)]
        self.free_slots = settings.MATRIX_SIZE ** 2

    def render(self):
        # Pulisco l'immagine e imposto il colore di sfondo
        background(0, 0, 0)
        
        # Imposto il colore delle linee 
        noFill()
        stroke(60, 60, 60)
        
        max_dim = self.settings.MATRIX_SIZE * self.settings.CELL_SIZE
        
        # Disegno i separatori verticali
        for i in range(0, self.settings.MATRIX_SIZE):
            line(i*self.settings.CELL_SIZE, 0, i*self.settings.CELL_SIZE, max_dim)
            
        # Disegno i separatori orizzontali
        for i in range(0, self.settings.MATRIX_SIZE):
            line(0, i*self.settings.CELL_SIZE, max_dim, i*self.settings.CELL_SIZE)
            
        noStroke()
        fill(255, 0, 0)
        for j in range(1, self.settings.MATRIX_SIZE):
            s = ""
            for i in range(1, self.settings.MATRIX_SIZE):
                s += str(self.cells[j][i]) + " "
                if self.cells[j][i] is not None:
                    print("A!")
                    ellipse(self.settings.CELL_SIZE*i + self.settings.CELL_SIZE/2, self.settings.CELL_SIZE*j + self.settings.CELL_SIZE/2, self.settings.CELL_SIZE, self.settings.CELL_SIZE)
            print(s+"\n")

    def add_cell(self, cell, x, y):
        self.cells[y+1][x+1] = cell
        self.free_slots -= 1

    def setup_neighbours(self):
        for i in range(1, self.settings.MATRIX_SIZE):
            for j in range(1, self.settings.MATRIX_SIZE):

                current_cell = self.cells[i][j]
                if current_cell is not None:
                    for ii in range(i-1, i-1):
                        for jj in range(j-1, j+1):
                            if self.cells[ii][jj] is not None:
                                current_cell.add_neighbour(self.cells[ii][jj].dna_duplicate)

    def reproduction_round(self):
        sons = []
        for i in range(1, self.settings.MATRIX_SIZE):
            for j in range(1, self.settings.MATRIX_SIZE):

                current_cell = self.cells[i][j]
                if current_cell is not None and self.free_slots > 0:
                    print(1)
                    son = current_cell.reproduce()
                    relative_place = self.find_place_for_son(son, i, j)
                    print("relative: " + str(relative_place[0]) + ":" + str(relative_place[1]))
                    print("absolute: " + str(relative_place[0]+i) + ":" + str(relative_place[1]+j))
                    sons.append((son, i+relative_place[0]-1, j+relative_place[1]-1))

        for son_tup in sons:
            self.add_cell(son_tup[0], son_tup[1], son_tup[2])
        # Add each new cell as neighbour
        # ToDo check duplicates
        self.setup_neighbours()

        print("k")

    def find_place_for_son(self, son, i, j):
        for ii in range(i - 1, i + 2):
            for jj in range(j - 1, j + 2):
                print("ii " + str(ii) + " jj " + str(jj))
                if self.cells[ii][jj] is None:
                    return ii, jj



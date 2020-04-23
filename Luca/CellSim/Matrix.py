import string

class Matrix:
    def __init__(self, settings):
        self.settings = settings
        # Add some boundaries before and after each side to avoid getting out of the matrix
        self.cells = [[None for x in range(0, settings.MATRIX_SIZE)] for y in range(0, settings.MATRIX_SIZE)]
        self.free_slots = settings.MATRIX_SIZE ** 2

    def debug_print_matrix(self):
        for i in range(self.settings.MATRIX_SIZE):
            riga = ""
            for j in range(self.settings.MATRIX_SIZE):
                if self.cells[i][j] is not None:
                    riga += "Cell "
                else:
                    riga += "None "

            print(riga)

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

        # print("#####################################################")
        # self.debug_print_matrix()
        # print("#####################################################")
        for j in range(0, self.settings.MATRIX_SIZE):
            s = ""
            for i in range(0, self.settings.MATRIX_SIZE):
                cell = self.cells[j][i]
                if cell is not None:
                    fraction_per_letter = 255/self.settings.DNA_LENGTH
                    r = string.count(cell.dna, "R") * fraction_per_letter
                    g = string.count(cell.dna, "G") * fraction_per_letter
                    b = string.count(cell.dna, "B") * fraction_per_letter
                    fill(r, g, b)
                    ellipse((self.settings.CELL_SIZE)*i + self.settings.CELL_SIZE/2, (self.settings.CELL_SIZE)*j + self.settings.CELL_SIZE/2, self.settings.CELL_SIZE, self.settings.CELL_SIZE)

    def add_cell(self, cell, x, y):
        self.cells[x][y] = cell
        self.free_slots -= 1

    def kill_cell(self, x, y):
        self.cells[x][y] = None
        self.free_slots += 1

    def setup_neighbours(self):
        for i in range(0, self.settings.MATRIX_SIZE):
            for j in range(0, self.settings.MATRIX_SIZE):

                current_cell = self.cells[i][j]
                if current_cell is not None:
                    current_cell.set_grown_status()
                    current_cell.reset_neighbours()
                    for ii in range(i-1, i-1):
                        for jj in range(j-1, j+1):
                            if self.cells[ii][jj] is not None:
                                current_cell.add_neighbour(self.cells[ii][jj].dna_duplicate)

    def reproduction_round(self):
        print("Starting new reproduction round")
        deaths = 0
        for i in range(0, self.settings.MATRIX_SIZE):
            for j in range(0, self.settings.MATRIX_SIZE):

                current_cell = self.cells[i][j]
                if current_cell is not None and self.free_slots > 0:
                    if current_cell.is_not_new():
                        son = current_cell.reproduce()
                        if son is not None:
                            son_place = self.find_place_for_son(i, j)
                            if son_place is not None:
                                self.add_cell(son, son_place[0], son_place[1])
                        else:
                            self.kill_cell(i, j)
                            deaths += 1
        print("deaths: " + str(deaths))

        # Add each new cell as neighbour
        # ToDo check duplicates
        self.setup_neighbours()

    def find_place_for_son(self, ci, cj):
        a = max(ci-1, 0)
        b = min(ci+2, self.settings.MATRIX_SIZE)
        c = max(cj-1, 0)
        d = min(cj+2, self.settings.MATRIX_SIZE)
        for i in range(a, b):
            for j in range(c, d):
                if self.cells[i][j] is None:
                    return (i, j)

        # print("No place for son found")
        return None
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
        fill(255, 0, 0)

        print("#####################################################")
        self.debug_print_matrix()
        print("#####################################################")
        for j in range(0, self.settings.MATRIX_SIZE):
            s = ""
            for i in range(0, self.settings.MATRIX_SIZE):
                if self.cells[j][i] is not None:
                    print("A!")
                    ellipse((self.settings.CELL_SIZE)*i + self.settings.CELL_SIZE/2, (self.settings.CELL_SIZE)*j + self.settings.CELL_SIZE/2, self.settings.CELL_SIZE, self.settings.CELL_SIZE)

    def add_cell(self, cell, x, y):
        self.cells[y][x] = cell
        self.free_slots -= 1

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
        for i in range(0, self.settings.MATRIX_SIZE):
            for j in range(0, self.settings.MATRIX_SIZE):

                current_cell = self.cells[i][j]
                if current_cell is not None and self.free_slots > 0:
                    if current_cell.is_not_new():
                        print("--------------------------")
                        print(1)
                        print("parent_place: " + str(i) + ":" + str(j))
                        son = current_cell.reproduce()
                        relative_place = self.find_place_for_son(i, j)
                        print("putting son in: " + str(relative_place))
                        self.add_cell(son, relative_place[0], relative_place[1])

        # Add each new cell as neighbour
        # ToDo check duplicates
        self.setup_neighbours()

    def find_place_for_son(self, ci, cj):
        print("\nI'm trying to add a cell centered in " + str(ci) + "," + str(cj))
        # self.debug_print_matrix()

        a = ''
        aa = max(ci-1, 0)
        b = min(ci+2, self.settings.MATRIX_SIZE)
        c = max(cj-1, 0)
        d = min(cj+2, self.settings.MATRIX_SIZE)
        for i in range(aa, b):
            for j in range(c, d):
                a += str(i) + "," + str(j)
                a += str(self.cells[i][j]) + "\n"
        print(a)

        #
        # for ii in range(i - 1, i + 2):
        #     for jj in range(j - 1, j + 2):
        #         if ii < 0 or jj < 0:
        #             print("Skipping lower search " + str(ii) + "," + str(jj))
        #         elif ii > self.settings.MATRIX_SIZE or jj > self.settings.MATRIX_SIZE:
        #             print("Skipping higher search " + str(ii) + "," + str(jj))
        #         else:
        #             print("self.cells["+ str(ii) + "][" + str(jj) +"]: " + str(self.cells[ii][jj]))
        #             if self.cells[ii][jj] is None:
        #                 return ii, jj
        #             else:
        #                 print("Skipping full cell" + str(ii) + "," + str(jj))
        # print("No place found")

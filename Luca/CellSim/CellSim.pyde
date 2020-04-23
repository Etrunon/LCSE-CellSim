from Matrix import Matrix
from Cell import Cell
from Settings import Settings

sett = Settings()

matrix = Matrix(sett)
init_dna = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'G', 'G', 'G']
matrix.add_cell(Cell(sett, init_dna), 1, 1)
init_dna = ['G', 'B', 'B', 'B', 'R', 'R', 'R', 'G', 'G', 'G']
matrix.add_cell(Cell(sett, init_dna), 10, 12)
# matrix.add_cell(Cell(sett, init_dna), 5, 13)
# matrix.add_cell(Cell(sett, init_dna), 13, 5)
# matrix.add_cell(Cell(sett, init_dna), 32, 21)

def setup():
    sett = Settings()
    size((sett.MATRIX_SIZE * sett.CELL_SIZE) + 1, (sett.MATRIX_SIZE * sett.CELL_SIZE) + 1)
    # per evitare che venga richiamata 
    # piu volte in loop draw()
    noLoop()


def draw():
    matrix.render()

def keyPressed():
    matrix.reproduction_round()

    print("test")
    a = matrix.cells[3:6][3:6]
    for i in range(len(a)):
        s = ''
        for j in range(len(a)):
            if a[i][j] is None:
                s += "None"
            else:
                s += "Cell"
        print(s)
    print("fine test")

    redraw()

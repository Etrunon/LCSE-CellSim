from Matrix import Matrix
from Cell import Cell
from Settings import Settings

sett = Settings()

matrix = Matrix(sett)
matrix.plant_individuals()

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

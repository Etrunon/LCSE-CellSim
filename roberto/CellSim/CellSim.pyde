from Matrix import Matrix
from Cell import Cell

MATRIX_SIZE = 50 # numero di "slot" nella matrice
CELL_SIZE = 20 # dimensione in pixel della singola cella

matrix = Matrix(CELL_SIZE, MATRIX_SIZE)
matrix.add_cell(Cell('HELLOWORLD'), 1, 1)

def setup():
    size(MATRIX_SIZE*CELL_SIZE + 1, MATRIX_SIZE*CELL_SIZE + 1)
    # per evitare che venga richiamata 
    # piu volte in loop draw()
    noLoop() 
    

def draw():
    matrix.render()

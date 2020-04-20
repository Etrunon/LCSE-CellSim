from Matrix import Matrix
from Cell import Cell
st = Settings()

matrix = Matrix(st.CELL_SIZE, st.MATRIX_SIZE)
matrix.add_cell(Cell('HELLOWORLD'), 1, 1)
matrix.add_cell(Cell('HELLOWORLD'), 5, 13)
matrix.add_cell(Cell('HELLOWORLD'), 13, 5)
matrix.add_cell(Cell('HELLOWORLD'), 32, 21)

def setup():
    size(st.MATRIX_SIZE * st.CELL_SIZE + 1, st.MATRIX_SIZE * st.CELL_SIZE + 1)
    # per evitare che venga richiamata 
    # piu volte in loop draw()
    noLoop() 
    

def draw():
    matrix.render()

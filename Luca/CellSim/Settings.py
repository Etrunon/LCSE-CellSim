class Settings:
    def __init__(self):
        self.DNA_POSSIBLE_CHARS = ["R", "G", "B", "r", "g", "b"]
        self.DNA_LENGTH = 10
        self.DEATH_RATE = 0.40

        self.REPRODUCTION_MAX_DISTANCE = 4

        self.MATRIX_SIZE = 50  # numero di "slot" nella matrice
        self.CELL_SIZE = 10  # dimensione in pixel della singola cella

    def __str__(self):
        s = ""
        s += "DNA_POSSIBLE_CHARS: " + str(self.DNA_POSSIBLE_CHARS) + "\n"
        s += "DNA_LENGTH: " + str(self.DNA_LENGTH) + "\n"
        s += "REPRODUCTION_MAX_DISTANCE: " + str(self.REPRODUCTION_MAX_DISTANCE) + "\n"
        s += "MATRIX_SIZE: " + str(self.MATRIX_SIZE) + "\n"
        s += "CELL_SIZE: " + str(self.CELL_SIZE)
        return s

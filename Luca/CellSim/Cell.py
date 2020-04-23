import random

class Cell:
    def __init__(self, settings, dna):
        self.settings = settings
        self.dna = dna
        self.dna_duplicate = None
        self.neighbours_dna = []
        self.status = "new"
        random.seed()

    def set_grown_status(self):
        self.status = "grown"

    def is_not_new(self):
        return self.status != "new"

    def reset_neighbours(self):
        self.neighbours_dna = []

    def move(local_area):
        move = False
        i = 0
        choices = random.shuffle(range(9))
        while not move and i < 9:
            if local_area[choices[i]] is None:
                return i

        return 5

    def duplicate_dna(self):
        duplicated_seq = ""
        for i in range(self.settings.DNA_LENGTH):

            char = self.dna[i]
            if char.islower():
                duplicated_seq += char.upper()
            else:
                duplicated_seq += char.lower()

        self.dna_duplicate = duplicated_seq

    def add_neighbour_dna(self, dna):
        neighbours.append(dna)

    def reproduce(self):
        if not self.death():
            partner = []
            if len(self.neighbours_dna) > 0:
                partner = random.choice(self.neighbours_dna)

            join_dna = self.dna + partner
            son_dna = random.sample(join_dna, self.settings.DNA_LENGTH)

            return Cell(self.settings, son_dna)
        else:
            return None

    def death(self):
        return random.random() < self.settings.DEATH_RATE

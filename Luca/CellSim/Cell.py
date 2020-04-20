class Cell:
    def __init__(self, settings, dna):
        self.settings = settings
        self.dna = dna
        self.dna_duplicate = None

    def move(local_area):
        """
        Data una sottomatrice 3x3 restituisce l'indice della cella in cui ci si muove
        """
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

    def reproduce(self, local_area):
        choices = []
        for i in range(9):
            if i != 5:
                choices.append(local_area[i].duplicated_dna)
        return Cell()



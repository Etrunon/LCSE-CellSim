class Dna:
    sequence = ""

    def __init__(self, settings, sequence=None):
        if sequence is None:
            for i in range(settings.DNA_LENGTH):
                self.sequence += random.choice(settings.DNA_POSSIBLE_CHARS)
        else:
            self.sequence = sequence
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if strbases == "NULL":
            print("NULL seq created")
        else:
            if not self.valid_sequence():
                self.strbases = "ERROR"
                print("INVALID seq!")
            else:
                print("New sequence created!")

    @staticmethod
    def valid_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence):
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid


    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases):
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid



    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.valid_sequence():
            return len(self.strbases)
        else:
            return 0


    def count(self):
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        for i in self.strbases:
            if i == "A":
                count_a += 1
            elif i == "C":
                count_c += 1
            elif i == "G":
                count_g += 1
            elif i == "T":
                count_t += 1
        return count_a, count_c, count_g, count_t



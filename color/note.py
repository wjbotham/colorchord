import color.chord

class Note:
    def __init__(self, frequency):
        assert(frequency > 0)
        self.frequency = frequency
        self.intensity = 1

    def __add__(self, other):
        if other.__class__ is Note:
            if other.frequency == self.frequency:
                return color.chord.Chord(Note(self.frequency) * (self.intensity+other.intensity))
            else:
                return color.chord.Chord(self, other)
        else:
            return NotImplemented

    def __mul__(self, other):
        n = Note(self.frequency)
        n.intensity = self.intensity * other
        return n

    def __div__(self, other):
        return self * (1/other)

    def __eq__(self, other):
        if other.__class__ is Note:
            return other.frequency == self.frequency and other.intensity == self.intensity
        else:
            return NotImplemented

    def __repr__(self):
        if self.intensity == 1:
            return "Note(%r)" % self.frequency
        else:
            return "Note(%r)*%r" % (self.frequency, self.intensity)

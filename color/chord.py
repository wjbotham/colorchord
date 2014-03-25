# note[0] is frequency, note[1] is intensity
isInvalidNote = lambda note: note[0] <= 0 or note[1] < 0

class Chord:
    def __init__(self, notes):
        # TODO replace these with descriptive `raise` lines
        if not isinstance(notes, dict):
            raise Exception("Argument to Chord constructor must be a dict")
        if not len(notes.keys()) > 0:
            raise Exception("Chord constructor arguments must include at least one note")
        if any(map(isInvalidNote, notes.items())):
            raise Exception("All notes of a Chord must have frequency > 0 and intensity >= 0")
        self.notes = { k:v for k,v in notes.items() if v > 0 }

    def get_frequencies(self):
        return list(self.notes.keys())
    frequencies = property(get_frequencies)

    def __mul__(self, other):
        return Chord({ k: other*v for k,v in self.notes.items() })

    def __add__(self, other):
        if other == 0:
            return self
        if not isinstance(other, Chord):
            return NotImplemented
        freqs = set(self.frequencies + other.frequencies)
        notes = {}
        for freq in freqs:
            self_intensity = self.notes.get(freq) or 0
            other_intensity = other.notes.get(freq) or 0
            notes[freq] = self_intensity + other_intensity
        return Chord(notes)

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        noteReprs = []
        for freq in sorted(self.notes.keys()):
            noteRepr = "Note(%r)" % freq
            if self.notes[freq] != 1:
                noteRepr += "*%r" % self.notes[freq]
            noteReprs.append(noteRepr)
        return " + ".join(noteReprs)

    def __eq__(self, other):
        if not isinstance(other, Chord):
            return False
        elif len(self.notes.keys()) != len(other.notes.keys()):
            return False
        elif any(self.notes[key] != other.notes.get(key) for key in self.notes.keys()):
            return False
        else:
            return True

def Note(frequency):
    return Chord({ frequency: 1 })

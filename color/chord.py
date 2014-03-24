import color.note

class Chord:
    def __init__(self, *args):
        assert(all(map(lambda n: n.__class__ is color.note.Note, args)))
        notes = sorted(args, key = lambda note: note.frequency)
        frequencies = [note.frequency for note in notes]
        notes_dict = { freq: sum(note.intensity for note in notes if note.frequency == freq) for freq in frequencies }
        self.notes = [color.note.Note(frequency)*intensity for frequency,intensity in notes_dict.items()]

    def __add__(self, other):
        if other.__class__ is color.note.Note:
            return Chord(*(self.notes + [other]))
        elif other.__class__ is Chord:
            return Chord(*(self.notes + other.notes))
        else:
            return NotImplemented

    def __mul__(self, other):
        return Chord(*(map(lambda n: n*other, self.notes)))

    def __eq__(self, other):
        if other.__class__ is color.note.Note:
            return len(self.notes)==1 and self.notes[0] == other
        elif other.__class__ is Chord:
            return all(self.notes[i] == other.notes[i] for i in range(max(len(self.notes),len(other.notes))))

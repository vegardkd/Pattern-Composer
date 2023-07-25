from interfaces import Pattern
from interfaces import Chord
from utils.functions import repeat_until_done
from utils.constants import *
from utils.functions import get_close_to_frequency, get_notes, thread

class KidsMelody(Pattern):

    def __init__(self):
        notes = Chord(1, 'major_pentatonic').get_notes(octave=3)
        self.notes = notes + [notes[-1].next(2)]

    @repeat_until_done(0.125)
    def run(self):
        
        if self.is_beginning_of_bar():
            if self.get_cursor().bar % 4 == 0:
                self.ascending_motif()
            if self.get_cursor().bar % 4 == 1:
                self.top_descending()
            if self.get_cursor().bar % 4 == 2:
                self.last_two_notes()
    
    @thread()
    def ascending_motif(self):
        for note, pause in zip(self.notes[:-2], [1]*4):
            self.play(note, release=1, velocity=100)
            self.sleep(1)

    @thread()
    def top_descending(self):
        notes = [self.notes[-2], self.notes[-1], self.notes[-2], self.notes[-3]]
        for note, pause in zip(notes, [1, 0.5, 1, 1]):
            self.play(note, release=pause, velocity=100)
            self.sleep(pause)
    
    @thread(offset=-0.5, chord_offset=False)
    def last_two_notes(self):
        self.play(self.notes[2], release=4.5, velocity=100)
        self.sleep(4.5)
        self.play(self.notes[1], release=3.5, velocity=100)
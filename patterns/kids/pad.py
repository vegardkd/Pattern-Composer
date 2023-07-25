from interfaces import Pattern
from interfaces import Chord
from utils.functions import repeat_until_done
from utils.constants import *
from utils.functions import get_close_to_frequency
from utils.functions import *


class KidsPad(Pattern):

    def __init__(self):
        self.set_initial()
    
    def on_chord_change(self, chord):
        if self.get_cursor().bar % 4 == 0 and self.is_beginning_of_bar():
            self.set_initial()
        else:
            self.minimize_distance(chord)

    def set_initial(self):
        notes = self.get_current_chord().get_notes(octave=2)
        self.low, self.mid, self.high = notes
  
    def minimize_distance(self, chord):
        
        chord_notes = chord.get_notes(octave=2)
        steps = [n.step for n in chord_notes]

        self.high = get_closest_to_notes(
            self.high,
            get_notes(lambda note: note.step in steps)
        )


        self.mid = get_closest_to_notes(
            self.mid,
            get_notes(
                lambda note: note.step in steps 
                and note.step != self.high.step 
                and note < self.high
            )
        )

        self.low = get_closest_to_notes(
            self.low,
            get_notes(
                lambda note: note.step in steps 
                and not note.step in [self.high.step,self.mid.step] 
                and note < self.high 
                and note < self.mid
            )   
        )

    @repeat_until_done()
    def run(self):
        self.play([self.low, self.mid, self.high], release=4, velocity=100)
        self.sleep(4)


from interfaces import Pattern
from utils.functions import repeat_until_done
from utils.constants import *
from utils.functions import get_close_to_frequency

class KidsBass(Pattern):

    def __init__(self):
        step = self.get_current_chord().get_notes(octave=1)[0].step
        key = self.get_key()
        self.root = get_close_to_frequency('G#0', step, key)
    
    def on_chord_change(self, chord):
        chord_notes = chord.get_notes(octave=0)
        key = self.get_key()
        self.root = get_close_to_frequency('G#0', chord_notes[0].step, key)

    @repeat_until_done()
    def run(self):
        if self.is_part('verse2') and self.get_cursor().bar < 8:
            self.drawn_out()
        elif self.is_part('verse2') and self.get_cursor().bar >= 8:
            self.build_up()
        else:
            self.pulse()

    def pulse(self):
        self.play(self.root, release=0.5, velocity=100)
        self.sleep(0.5)
        self.play(self.root+12, release=0.5, velocity=100)
        self.sleep(0.5)

    def drawn_out(self):
        self.play(self.root, release=4, velocity=100)
        self.sleep(4)

    def build_up(self):
        self.play(self.root, release=1.5, velocity=100)
        self.sleep(1.5)
        self.play(self.root+12, release=2.5, velocity=100)
        self.sleep(2.5)

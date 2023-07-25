from interfaces import Pattern
from interfaces import Chord
from utils.functions import repeat_until_done
from utils.constants import *
from utils.functions import get_close_to_frequency
from utils.functions import thread

class KidsOtherMelody(Pattern):

    def __init__(self):
        self.velocity=60
        self.on_chord_change(self.get_current_chord())

    @repeat_until_done(0.125)
    def run(self):
        if self.is_part('verse') and self.get_cursor().bar < 8:
            return
        self.play_melody()

    def on_chord_change(self, chord):
        root, third, fifth = chord.get_notes(octave=2)

        self.first_motif = [
            [root, root, third, third, root, root, third, root, third.get_next(), fifth],
            [1, 1.5, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5]
        ]
        self.second_motif = [
            [root, root.get_next(), root, third, root.get_next(), root, root.get_previous(mode=chord.quality)],
            [1, 0.5, 1, 0.5, 0.5, 0.5, 0.5]
        ]
        self.third_motif = [
            [third.get_next(2), third.get_next(), root.get_previous(mode=chord.quality), root.get_next(1), third, root.get_next(1), root],
            [0.5]*3+[1]+[0.5]*3
        ]
    
    def play_melody(self):
        if self.is_beginning_of_bar():
            if self.get_cursor().bar % 4 == 0:
                self.standard_motif(self.first_motif)
            if self.get_cursor().bar % 4 == 3:
                if (self.get_cursor().bar // 4) % 2 == 0:
                    self.offset_motif(self.second_motif)
                else:
                    self.standard_motif(self.third_motif)

    @thread()
    def standard_motif(self, motif):
        self.play_notes(motif)

    @thread(offset=-0.5, chord_offset=False)
    def offset_motif(self, motif):
        self.play_notes(motif)

    def play_notes(self, motif):
        for note, pause in zip(*motif):
            self.play(note, release=self.get_pause(pause), velocity=self.velocity)
            self.sleep(pause)

    def get_pause(self, pause):
        return 0.75*pause if pause > 0.75 else pause
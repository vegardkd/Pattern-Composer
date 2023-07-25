from interfaces import Pattern
from interfaces import Chord, Note
from utils.functions import repeat_until_done
from utils.constants import *
from utils.functions import get_close_to_frequency
from utils.functions import thread
from utils.functions import *
from itertools import cycle

class KidsSolo(Pattern):

    def __init__(self):
        current_chord = self.get_current_chord()

        self.velocity=60 
        self.ascending = []
        self.sleep_time = 0.25
        self.cutoff_note = current_chord.get_notes(octave=2)[0]
        self.set_first_motif(current_chord)

    def on_chord_change(self, chord):
        self.set_first_motif(chord)
        self.set_second_motif(chord)
        self.set_third_motif(chord)

    def set_first_motif(self, chord):
        chord_notes = get_all_chord_notes(self.get_current_chord())

        ascending_notes = [x for x in chord_notes if x > self.cutoff_note][:4]
        self.ascending = ascending_notes[:-1] + [ascending_notes[3].get_previous()]
        self.zigzag_descending = [ascending_notes[3]] + generate_notes_from_movements(
            note=ascending_notes[3].get_previous(), 
            count=11, 
            vertical_movement=[-1, -1, -1, 1] 
        )

    def set_second_motif(self, chord):
        chord_notes = get_all_chord_notes(self.get_current_chord())
        cutoff = [x for x in chord_notes if x >= self.cutoff_note][0]

        notes = []
        for x in generate_notes_from_movements(cutoff, count=4, vertical_movement = [1]):
            motif = generate_notes_from_movements(x, count=4, vertical_movement = [1, 1, 2], mode='lydian')
            notes.extend(motif)
        self.lydian_notes = notes
    
    def set_third_motif(self, chord):
        chord_notes = get_all_chord_notes(self.get_current_chord())
        cutoff = [x for x in chord_notes 
        if x >= self.cutoff_note and x.step == chord.get_notes(octave=2)[0].step][0]
        self.last_motif_note = cutoff

    @repeat_until_done(0.125)
    def run(self):
        if self.is_beginning_of_bar():
            bar = self.get_cursor().bar
            if bar % 4 != 3:
                self.up_and_down_motif()
            elif bar == 3:
                self.lydian_motif()
            elif bar == 7:
                self.trumpet_motif()

    @thread()
    def lydian_motif(self):
        for x in self.lydian_notes:
            self.play(x, release=self.sleep_time, velocity=100)
            self.sleep(self.sleep_time)

    @thread()
    def up_and_down_motif(self):
        for x in self.ascending + self.zigzag_descending:
            self.play(x, release=self.sleep_time, velocity=100)
            self.sleep(self.sleep_time)

    @thread()
    def trumpet_motif(self):
        while self.get_cursor().bar == 7:
            if self.get_cursor().sixteenth_notes in [0, 2, 3, 4,  6, 8]:
                self.play(self.last_motif_note, release=0.25, velocity=100)
            self.sleep(self.sleep_time)
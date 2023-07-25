from interfaces import Pattern
from utils.functions import repeat_until_done
from utils.constants import *

class KidsDrums(Pattern):

    def __init__(self):
        self.bridge_toms_pause_switch = True
        self.standard_parts = [
            'intro', 
            'intro2', 
            'verse', 
            'chorus', 
            'chorus2',
            'chorus3', 
            'bridge',
            'bridge2'
        ]

        self.clap_parts = [
            'intro2', 
            'chorus', 
            'chorus2',
            'chorus3', 
            'bridge',
            'bridge2'
        ]

    @repeat_until_done(0.125)
    def run(self):
        if any([self.is_part(part) for part in self.standard_parts]):
            self.standard()
            if self.get_cursor().bar % 8 == 7:
                self.transition()
            
        if any([self.is_part(part) for part in self.clap_parts]):
            self.claps()

        if self.is_part('verse2'):
            bar = self.get_cursor().bar
            if 4 <= bar < 12:
                self.syncopated()
            if 12 <= bar < 15:
                self.eight_notes()
            if self.get_cursor().bar == 15:
                self.second_transition()

        if self.is_part('bridge'):
            bar = self.get_cursor().bar
            self.bridge_toms()

        if self.is_part('bridge2'):
            self.bridge2()

    def bridge2(self):
        if self.get_cursor().bar % 4 in [0,1] and self.get_cursor().eight_notes in range(8):
            self.play(OPEN_HI_HAT, release=0.5, velocity=100)
        if self.get_cursor().bar in [2, 4, 7] and self.get_cursor().sixteenth_notes in range(2,9):
            self.play(ACOUSTIC_SNARE, release=0.25, velocity=100)

    def standard(self):
        if self.get_cursor().quarter_notes in [0,2]:
            self.play(BASS_DRUM, release=0.5, velocity=100)
        if self.get_cursor().quarter_notes in [1,3]: 
            self.play(ACOUSTIC_SNARE, release=0.5, velocity=100)

    def syncopated(self):
        if self.get_cursor().eight_notes in [0, 3, 4]:
            self.play(BASS_DRUM, release=0.5, velocity=100)

    def eight_notes(self):
        if self.get_cursor().quarter_notes in range(4):
            self.play(BASS_DRUM, release=0.5, velocity=100)

    def claps(self):
        if self.get_cursor().quarter_notes in [1,3]:
            self.play(HAND_CLAP, release=0.5, velocity=100)
    
    def bridge_toms(self):
        eight_notes = self.get_cursor().eight_notes
        bar = self.get_cursor().bar
        if eight_notes in range(0,4) or eight_notes in [4,6]:
            self.play(LOW_TOM, release=0.5, velocity=100)
        if self.bridge_toms_pause_switch and eight_notes == 5:
            self.play(LOW_TOM, release=0.5, velocity=100)
        if self.is_beginning_of_bar():
            self.bridge_toms_pause_switch = not self.bridge_toms_pause_switch
    
    def transition(self):
        if self.get_cursor().sixteenth_notes == 7:
            self.play(ACOUSTIC_SNARE, release=0.5, velocity=100)
        if self.get_cursor().eight_notes in [5, 6]:
            self.play(HAND_CLAP, release=0.5, velocity=100)

    def second_transition(self):
        if (self.get_cursor().sixteenth_notes in [7, 10] 
            or self.get_cursor().quarter_notes in [0,1,2]):
            self.play(BASS_DRUM, release=0.5, velocity=100)
        if self.get_cursor().sixteenth_notes in [12, 15]:
            self.play([HAND_CLAP, ACOUSTIC_SNARE], release=0.5, velocity=100)



            
"""

Below is a notice of the license for gvoekl´s (github name) python-sonic
codebase available on Github: https://github.com/gkvoelkl/python-sonic

Most of the scales, notes and chord qualities in the rest of the file
is taken directly from an early version of the software:

https://github.com/gkvoelkl/python-sonic/blob/421fd2377358e34dc8c66f0cd45aee4be5068a7a/psonic.py

The MIT License (MIT)

Copyright (c) 2016 G. Völkl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


ACOUSTIC_BASS_DRUM = 35
BASS_DRUM = 36
SIDE_STICK = 37
ACOUSTIC_SNARE = 38
HAND_CLAP = 39
ELECTRIC_SNARE = 40
LOW_FLOOR_TOM = 41
CLOSED_HI_HAT = 42
HIGH_FLOOR_TOM = 43
PEDAL_HI_HAT = 44
LOW_TOM = 45
OPEN_HI_HAT = 46
LOW_MID_TOM = 47
HI_MID_TOM = 48
CRASH_CYMBAL_1 = 49
HIGH_TOM = 50
RIDE_CYMBAL_1 = 51
CHINESE_CYMBAL = 52
RIDE_BELL = 53
TAMBOURINE = 54
SPLASH_CYMBAL = 55
COWBELL = 56
CRASH_CYMBAL_2 = 57
VIBRA_SLAP = 58
RIDE_CYMBAL_2 = 59
HI_BONGO = 60
LOW_BONGO = 61
MUTE_HI_CONGA = 62
OPEN_HI_CONGA = 63
LOW_CONGA = 64
HIGH_TIMBALE = 65
LOW_TIMBALE = 66
HIGH_AGOGO = 67
LOW_AGOGO = 68
CABASA = 69
MARACAS = 70
SHORT_WHISTLE = 71
LONG_WHISTLE = 72
SHORT_GUIRO = 73
LONG_GUIRO = 74
CLAVES = 75
HI_WOOD_BLOCK = 76
LOW_WOOD_BLOCK = 77
MUTE_CUICA = 78
OPEN_CUICA = 79
MUTE_TRIANGLE = 80
OPEN_TRIANGLE = 81


SCALES = {
    'chromatic': [0,1,2,3,4,5,6,7,8,9,10,11],
    'diatonic': [0, 2, 4, 5, 7, 9, 11],
    'ionian': [0, 2, 4, 5, 7, 9, 11],
    'major_scale': [0, 2, 4, 5, 7, 9, 11],
    'dorian': [0, 2, 3, 5, 7, 9, 10],
    'phrygian': [0, 1, 3, 5, 7, 8, 10],
    'lydian': [0, 2, 4, 6, 7, 9, 11],
    'mixolydian': [0, 2, 4, 5, 7, 9, 10],
    'aeolian': [0, 2, 3, 5, 7, 8, 10],
    'minor_scale': [0, 2, 3, 5, 7, 8, 10],
    'locrian': [0, 1, 3, 5, 6, 8, 10],
    'hex_major6': [0, 2, 4, 5, 7, 9],
    'hex_dorian': [0, 2, 3, 5, 7, 10],
    'hex_phrygian': [0, 1, 3, 5, 8, 10],
    'hex_major7': [0, 2, 4, 7, 9, 11],
    'hex_sus': [0, 2, 5, 7, 9, 10],
    'hex_aeolian': [0, 3, 5, 7, 8, 10],
    'minor_pentatonic': [0, 3, 5, 7, 10],
    'yu': [0, 3, 5, 7, 10],
    'major_pentatonic': [0, 2, 4, 7, 9],
    'gong': [0, 2, 4, 7, 9],
    'egyptian': [0, 2, 5, 7, 10],
    'shang': [0, 2, 5, 7, 10],
    'jiao': [0, 3, 5, 8, 10],
    'zhi': [0, 2, 5, 7, 9],
    'ritusen': [0, 2, 5, 7, 9],
    'whole_tone': [0, 2, 4, 6, 8, 10],
    'whole': [0, 2, 4, 6, 8, 10],
    'chromatic': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'harmonic_minor': [0, 2, 3, 5, 7, 8, 11],
    'melodic_minor_asc': [0, 2, 3, 5, 7, 9, 11],
    'hungarian_minor': [0, 2, 3, 6, 7, 8, 11],
    'octatonic': [0, 2, 3, 5, 6, 8, 9, 11],
    'messiaen1': [0, 2, 4, 6, 8, 10],
    'messiaen2': [0, 1, 3, 4, 6, 7, 9, 10],
    'messiaen3': [0, 2, 3, 4, 6, 7, 8, 10, 11],
    'messiaen4': [0, 1, 2, 5, 6, 7, 8, 11],
    'messiaen5': [0, 1, 5, 6, 7, 11],
    'messiaen6': [0, 2, 4, 5, 6, 8, 10, 11],
    'messiaen7': [0, 1, 2, 3, 5, 6, 7, 8, 9, 11],
    'super_locrian': [0, 1, 3, 4, 6, 8, 10],
    'hirajoshi': [0, 2, 3, 7, 8],
    'kumoi': [0, 2, 3, 7, 9],
    'neapolitan_major': [0, 1, 3, 5, 7, 9, 11],
    'bartok': [0, 2, 4, 5, 7, 8, 10],
    'bhairav': [0, 1, 4, 5, 7, 8, 11],
    'locrian_major': [0, 2, 4, 5, 6, 8, 10],
    'ahirbhairav': [0, 1, 4, 5, 7, 9, 10],
    'enigmatic': [0, 1, 4, 6, 8, 10, 11],
    'neapolitan_minor': [0, 1, 3, 5, 7, 8, 11],
    'pelog': [0, 1, 3, 7, 8],
    'augmented2': [0, 1, 4, 5, 8, 9],
    'scriabin': [0, 1, 4, 7, 9],
    'harmonic_major': [0, 2, 4, 5, 7, 8, 11],
    'melodic_minor_desc': [0, 2, 3, 5, 7, 8, 10],
    'romanian_minor': [0, 2, 3, 6, 7, 9, 10],
    'hindu': [0, 2, 4, 5, 7, 8, 10],
    'iwato': [0, 1, 5, 6, 10],
    'melodic_minor': [0, 2, 3, 5, 7, 9, 11],
    'diminished2': [0, 2, 3, 5, 6, 8, 9, 11],
    'marva': [0, 1, 4, 6, 7, 9, 11],
    'melodic_major': [0, 2, 4, 5, 7, 8, 10],
    'indian': [0, 4, 5, 7, 10],
    'spanish': [0, 1, 4, 5, 7, 8, 10],
    'prometheus': [0, 2, 4, 6, 11],
    'diminished': [0, 1, 3, 4, 6, 7, 9, 10],
    'todi': [0, 1, 3, 6, 7, 8, 11],
    'leading_whole': [0, 2, 4, 6, 8, 10, 11],
    'augmented': [0, 3, 4, 7, 8, 11],
    'purvi': [0, 1, 4, 6, 7, 8, 11],
    'chinese': [0, 4, 6, 7, 11],
    'lydian_minor': [0, 2, 4, 6, 7, 8, 10],
    'i': [0, 2, 4, 5, 7, 9, 11],
    'ii': [0, 2, 3, 5, 7, 9, 10],
    'iii': [0, 1, 3, 5, 7, 8, 10],
    'iv': [0, 2, 4, 6, 7, 9, 11],
    'v': [0, 2, 4, 5, 7, 9, 10],
    'vi': [0, 2, 3, 5, 7, 8, 10],
    'vii': [0, 1, 3, 5, 6, 8, 10],
    'viii': [0, 2, 4, 5, 7, 9, 11]
 }

CHORD_QUALITY = {

    'major': [0, 4, 7],
    'minor': [0, 3, 7],
    'major7': [0, 4, 7, 11],
    'dom7': [0, 4, 7, 10],
    'minor7': [0, 3, 7, 10],
    'aug': [0, 4, 8],
    'dim': [0, 3, 6],
    'dim7': [0, 3, 6, 9],
    '1': [0],
    "5": [0, 7],
    "+5": [0, 4, 8],
    "m+5": [0, 3, 8],
    "sus2": [0, 2, 7],
    "sus4": [0, 5, 7],
    "6": [0, 4, 9],
    "m6": [0, 3, 8],
    "7sus2": [0, 2, 7, 10],
    "7sus4": [0, 5, 7, 10],
    "7b5": [0, 4, 6, 10],
    "m7b5": [0, 3, 6, 10],
    "m7b5b3": [0, 2, 6, 10],
    "7+5": [0, 4, 8, 10],
    "m7+5": [0, 3, 8, 10],
    "9": [0, 4, 7, 10, 14],
    "m9": [0, 3, 7, 10, 14],
    "m7+9": [0, 3, 7, 10, 14],
    "maj9": [0, 4, 7, 11, 14],
    "9sus4": [0, 5, 7, 10, 14],
    "6*9": [0, 4, 7, 9, 14],
    "m6*9": [0, 3, 9, 7, 14],
    "7b9": [0, 4, 7, 10, 13],
    "7#9": [0, 4, 7, 10, 15],
    "m7b9": [0, 3, 7, 10, 13],
    "7b10": [0, 4, 7, 10, 15],
    "9+5": [0, 10, 13],
    "m9+5": [0, 10, 14],
    "7+5b9": [0, 4, 8, 10, 13],
    "m7+5b9": [0, 3, 8, 10, 13],
    "11": [0, 4, 7, 10, 14, 17],
    "m11": [0, 3, 7, 10, 14, 17],
    "maj11": [0, 4, 7, 11, 14, 17],
    "11+": [0, 4, 7, 10, 14, 18],
    "m11+": [0, 3, 7, 10, 14, 18],
    "13": [0, 4, 7, 10, 14, 17, 21],
    "m13": [0, 3, 7, 10, 14, 17, 21],
    "m7b5addb9": [0, 3, 6, 10, 13],
    "m11b5b9": [0, 3, 6, 10, 13, 17],
    "m13b5b9": [0, 3, 6, 10, 13, 17, 21],
    "m11b9": [0, 3, 7, 10, 13, 17],
    "maj7addb9add#11": [0, 4, 7, 11, 13, 18],
    "maj9add#11": [0, 4, 7, 11, 14, 18],
    "m11addb13": [0, 3, 7, 10, 14, 17, 20],
    "m11b5b9addb13": [0, 3, 6, 10, 13, 17, 20],
    "maj13": [0, 4, 7, 11, 14, 17, 21],
    "m11b9addb13": [0, 3, 7, 10, 13, 17, 20],
    "maj13#11": [0, 4, 7, 11, 14, 18, 21],
    "M": [0, 4, 7],
    "m": [0, 3, 7],
    "7": [0, 4, 7, 10],
    "M7": [0, 4, 7, 11],
    "m7": [0, 3, 7],
    "augmented": [0, 4, 8],
    "a": [0, 4, 8],
    "diminished": [0, 3, 6],
    "i": [0, 3, 6],
    "diminished7": [0, 3, 6, 9],
    "i7": [0, 3, 6, 9]
}

PITCH_SETS = {**CHORD_QUALITY, **SCALES}

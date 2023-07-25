from abc import ABC, abstractmethod
from typing import List

class Pattern(ABC):
    """
    The Pattern class represents a musical pattern and serves as an interface for creating 
    different types of musical patterns.

    """

    def __init__(self):
        """
        Initializes a Pattern instance.
        """
        pass

    def get_key(self):
        """
        Returns the key of the song.
        """
        pass

    def is_part(self, name):
        """
        Returns True if the song is in the current part, else False.
        """
        pass

    def get_current_chord(self):
        """
        Returns a Chord instance representing the current chord being played.
        """
        pass

    def play(self, notes, release, velocity=20, until_chord_change=False):
        """
        Plays the given notes with the specified release and velocity.
        """
        pass

    def is_beginning_of_bar(self):
        """
        Checks if the current position of the cursor is at the beginning of a bar.
        """
        pass

    def get_cursor(self):
        """
        Returns a Cursor instance representing the current time of the song.
        """
        pass

    def sleep(self, quarter_notes):
        """
        Pauses the cursor for the specified number of quarter notes.
        """
        pass

    @abstractmethod
    def run(self):
        """
        Method stub for running the pattern. This method should be overridden by subclasses.
        """
        pass

    def on_chord_change(self, chord):
        """
        Method stub for actions to take on a chord change. This method can be overridden by subclasses.
        """
        pass


class Note:
    """
    The Note class represents a musical note with a certain step and octave.
    Inherits from the Step class.
    
    Instance variables:
    step (int): The note step in the octave (1 to 12).
    octave (int): The octave of the note.
    """

    def __init__(self, step, octave):
        """
        Initializes a Note instance. Inherits from the Step class.
        
        Parameters:
        step (int): The note step in the octave (1 to 12).
        octave (int): The octave of the note.
        """
        pass

    def get_next(self, steps=1, mode='diatonic'):
        """
        Returns the next note in a given mode.

        Parameters:
        steps (int): The number of steps forward.
        mode (str): The mode to use. If not provided, 'diatonic' is used.

        Returns:
        Note: The next Note instance in the mode.
        """
        pass

    def get_previous(self, steps=1, mode='diatonic'):
        """
        Returns the previous note in a given mode.

        Parameters:
        steps (int): The number of steps backward.
        mode (str): The mode to use. If not provided, 'diatonic' is used.

        Returns:
        Note: The previous Note instance in the mode.
        """
        pass

    def get_difference(self, other):
        """
        Returns the difference in semitones between this note and another.

        Parameters:
        other (Note): The other note to compare with.

        Returns:
        int: The difference in semitones.
        """
        pass


class Chord:
    """
    Represents a musical chord.

    Attributes:
        step (int): The step or root note of the chord, represented as an integer.
        quality (str): The quality of the chord, which defines the set of pitch intervals.
        inversion (int, optional): The inversion of the chord. Default is None, indicating no inversion.

    Methods:
        get_notes(octave: int) -> List[Note]: Returns a list of notes that make up the chord.
    """

    def __init__(self, step, quality, inversion=None):
        """
        Constructs a new 'Chord' object.

        Args:
            step (int): The step or root note of the chord, represented as an integer.
            quality (str): The quality of the chord.
            inversion (int, optional): The inversion of the chord. Default is None.
        """
        self.step = step
        self.quality = quality
        self.inversion = inversion

    def get_notes(self, octave: int):
        """
        Returns a list of 'Note' objects that make up the chord.

        The notes are calculated based on the chord's step, quality, and octave.
        If the chord has an inversion, the notes will be rearranged accordingly.

        Args:
            octave (int): The octave in which the chord should be generated.

        Returns:
            List[Note]: A list of 'Note' objects representing the notes in the chord.
        """
        pass


class CurrentCursor:
    """
    Represents a musical cursor for a specific part of a musical pattern, e.g., verse, chorus.

    The cursor object contains several properties, all representing different note durations 
    within a bar. These properties can be used to accurately navigate and manipulate the musical pattern. 

    It's important to note that half_notes through thirtytwo_notes properties are reset to zero 
    for every new bar, while the bar property is reset to zero for every new part of the pattern (verse, chorus, etc.).

    Each of the note duration properties can contain decimal values, meaning that checking for an exact value 
    (e.g., cursor.quarter_notes == 2) ensures that the cursor is at the exact moment within the bar 
    when quarter notes equal the specified value.

    However, the bar property does not have decimal values, and it only increments when 4 quarter notes have passed 
    (assuming a 4/4 time signature). Therefore, it is more suitable for operations that involve entire bars.

    Attributes:
        thirtytwo_notes (float): The current position within a bar in terms of thirty-second notes. Resets after each bar.
        sixteenth_notes (float): The current position within a bar in terms of sixteenth notes. Resets after each bar.
        eight_notes (float): The current position within a bar in terms of eighth notes. Resets after each bar.
        quarter_notes (float): The current position within a bar in terms of quarter notes. Resets after each bar.
        half_notes (float): The current position within a bar in terms of half notes. Resets after each bar.
        bar (int): The current bar number within a part of the pattern. Resets for every new part (e.g., verse, chorus).

    """
    def __init__():
        self.thirtytwo_notes = thirtytwo_notes
        self.sixteenth_notes = sixteenth_notes
        self.eight_notes = eight_notes
        self.quarter_notes = quarter_notes
        self.half_notes = half_notes
        self.bar = bar   

from typing import List
from itertools import cycle

def get_all_notes():
    """
    Returns all notes from all octaves.
    """
    pass


def get_notes(func):
    """
    Returns all notes that satisfy a given condition.
    """
    pass


def get_underlying_chord_notes(note, chord, number):
    """
    Returns the underlying notes of a chord below a given note.
    """
    pass


def get_all_chord_notes(chord):
    """
    Returns all notes from a specified chord.
    """
    pass


def get_notes_in_mode(mode):
    """
    Returns all notes that are in a specified mode.
    """
    pass


def get_diatonic_notes():
    """
    Returns all diatonic notes.
    """
    pass


def get_root_note(octave):
    """
    Returns the root note at a specified octave.
    """
    pass


def repeat_until_done(sleep_time=0):
    """
    Decorator that repeats a function until a track is finished, with an optional sleep time.
    """
    pass


def get_closest_to(note, steps):
    """
    Returns the note closest to a specified note in terms of pitch from a list of steps.
    """
    pass


def get_next(note, step):
    """
    Returns the next note after a given note, at a specified step.
    """
    pass


def get_note_from_str(reference_note_in_str, key):
    """
    Returns a note specified by a string representation and a key.
    """
    pass


def get_close_to_frequency(reference_note_in_str, desired_step, key):
    """
    Returns a note that is close to a specified frequency, given a reference note in string format, a desired step, and a key.
    """
    pass

def get_closest_to_notes(note, notes):
    """
    This function takes as input a reference note and a list of notes. It finds the note from the list that is 
    closest to the reference note in terms of steps in a chromatic scale. The closest note is returned.
    """

def generate_notes_from_movements(note, count, vertical_movement: List[int], mode='diatonic'):
    """
    This function generates a sequence of notes based on given movements. The start_note is the note where the generation starts. 
    The count parameter indicates how many notes will be generated. The vertical_movement parameter is a list of integers specifying 
    the steps up (positive integer) or down (negative integer) from the last generated note. The mode parameter determines the chord 
    or scale (defined in utils/constants.py) the generation will follow. If not provided, 'diatonic' is used by default.
    """

def thread(offset=0, chord_offset=True):
    """
    Decorator that allows a function to run on its own time from the current time until it's finished, then returns back to the original time.
    """
    def outer_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            thread_wrapper_internal(args, offset, chord_offset, func, kwargs)
        return wrapper
    return outer_wrapper

def frequency_from_key(key):
    """Returns the frequency of the note (key) keys from A0"""
    return 440 * 2 ** ((key - 49) / 12.0)

def frequency_from_note(note):
    """Returns the frequency of a note represented by a string"""
    return frequency_from_key(key_from_note(note))

def key_from_note(note):
    """Returns the key number (keys from A0) from a note represented by a string"""
    indices = { 'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11 }

    """Set the octave to 4 by default incase it has not been specified"""
    octave = 4

    """But lets check if the octave WAS specified and change it if it was"""
    if note[-1] in '012345678':
        octave = int(note[-1])

    """"get the tone of the base note of the scale"""
    tone = indices[note[0].upper()]
    
    """get the exact pitch of the starting tone at the correct octave"""
    key = 12 * octave + tone

    """if a sharp sign was given then move the key up by a half step, if flat then down a half step"""
    if len(note) > 1 and note[1] == '#':
        key += 1
    elif len(note) > 1 and note[1] == 'b':
        key -= 1

    return key - 8;

def note_from_key(key):
    """Returns a string representing a note which is (key) keys from A0"""
    notes = ['a','a#','b','c','c#','d','d#','e','f','f#','g','g#']

    octave = (key + 8) / 12
    note = notes[(key -1 ) % 12]

    return note.upper() + str(octave)


# Licensed under The MIT License (MIT)
# See LICENSE file for more

"""
Contains some utility functions.
"""

def bReturn(output, Type):
    """Returns a selected output assuming input is a list"""
    if isinstance(output, list):
        if Type.lower() == "list":
            return output
        elif Type.lower() == "tuple":
            return tuple([i for i in output])
        elif Type.lower() == "dict":
            O = {}
            for i in range(len(output)):
                O[i] = output[i]
            return O
        elif Type.lower() == "string":
            return ','.join(output)
        elif Type.lower() == "stringspace":
            return ' '.join(output)
        else:
            raise MelopyGenericError("Unknown type: " + Type)
    else:
        raise MelopyGenericError("Input to bReturn is not a list! Input: " + str(output))

def frequency_from_key(key):
    """Returns the frequency of the note (key) keys from A0"""
    return 440 * 2 ** ((key - 49) / 12.0)

def frequency_from_note(note):
    """Returns the frequency of a note represented by a string"""
    return frequency_from_key(key_from_note(note))

def key_from_note(note):
    """Returns the key number (keys from A0) from a note represented by a string"""
    indices = { 'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11 }

    octave = 4

    if note[-1] in '012345678':
        octave = int(note[-1])

    tone = indices[note[0].upper()]
    key = 12 * octave + tone

    if len(note) > 1 and note[1] == '#':
        key += 1
    elif len(note) > 1 and note[1] == 'b':
        key -= 1

    return key - 8;

def note_from_key(key):
    """Returns a string representing a note which is (key) keys from A0"""
    ## TODO: On generating scales and triad, they return 
    ## TODO: ['C4', 'C#4', 'D#4', 'E4', 'F#4', 'G4', 'A4', 'A#4', 'C5'] instead ['C4', 'Db4', 'E4', 'F#4', 'G4', 'G#4', 'A#4', 'B4', 'C5']
    ## TODO: In fact, they sound equal, but have different notation
    notes = ['a','a#','b','c','c#','d','d#','e','f','f#','g','g#']
    octave = (key + 8) / 12
    note = notes[(key -1 ) % 12]

    return note.upper() + str(octave)
    
def iterate(start, pattern, rType="list"):
    """Iterates over a pattern starting at a given note"""
    start_key = key_from_note(start)
    ret = [start_key]
    for step in pattern:
        ret.append(ret[-1] + step)
    ret = map(note_from_key, ret)
    return bReturn(ret, rType)


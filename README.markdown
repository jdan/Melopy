# Melopy (melo-pee)
### A python library for playing with sound. 
### by Jordan Scales (http://jordanscales.com)
### on Github: http://github.com/prezjordan/Melopy

For an example: check out canon.py 
    $ python examples/canon.py


## Library methods

    >>> melopy.frequency_from_key(key)

    # Returns the frequency of the note (key) keys from A0
    # frequency_from_key(49) => 440

* * *

    >>> melopy.frequency_from_note(note)

    # Returns the frequency of a note represented by a string
    # frequency_from_note('A4') => 440

* * *

    >>> melopy.key_from_note(note)

    # Returns the key number (keys from A0) from a note represented by a string
    # key_from_note('A4') => 49

* * *

    >>> melopy.note_from_key(key)

    # Returns a string representing a note which is (key) keys from A0
    # note_from_key(49) => 'A4'

* * *

    >>> melopy.generate_major_scale(start)

    # Calls iterate() with the starting note and the pattern [2,2,1,2,2,2]
    # generate_major_scale('D4') => ['D4','E4','F#4','G4','A4','B4','C#5']

* * *

    >>> melopy.generate_minor_scale(start)

    # Calls iterate with the starting note and the pattern [2,1,2,2,1,2]
    # generate_minor_scale('C4') => ['C4','D4','E4','F4','G4','A4','A#4']

* * *

    >>> melopy.generate_major_triad(start)

    # Calls iterate with the starting note and the pattern [4, 3]
    # generate_major_triad('A4') => ['A4', 'C#5', 'E5']

* * *

    >>> melopy.generate_minor_triad(start)

    # Calls iterate with the starting note and the pattern [3, 4]
    # generate_minor_triad('C5') => ['C5', 'D#5', 'G5']

* * *


## Melopy Class

    class melopy.Melopy

        melopy_writer # bitwise writer for creating the .wav file
        rate          # sample rate (usually 44100)
        volume        # volume of wav track (from 0 to 32767)
        data          # array containing bytes to write to the wav file
        octave        # default octave if one is not specified in a melody
        tempo         # self explanitory
        wave_type     # sine, triangle, sawtooth, or square. the wave_type you will be adding when methods are called. Default is sine.

        __init__(self, title, volume=50)

        __del__(self)
        Destructor that calls render()

        add_wave(self, wave_type, frequency, length, location='END')
        Adds a wave with a given frequency, length (in seconds) at a given location (in seconds)

        add_note(self, note, length, wave_type='square', location='END')
        Same as add_wave, but instead of frequency, the user provides a string representing a note (ie 'C5')
        Also try add_quarter_note, add_half_note, add_whole_note, add_eighth_note, add_sixteenth_note instead of specifying a length

        iterate(self, start, pattern)
        Generates an array of notes given a starting note and a pattern of gaps between notes. This is better explained below

        add_melody(self, melody, length, wave_from [DEFAULT 'square'])
        Adds given notes in a melody to the wave data, each having the given length

        add_rest(self, length)
        Adds a rest (nothing) for a given time (in seconds)
        Also add_whole_rest, add_quarter_rest, etc. (instead of specifying a length)

        render(self)
        Renders the wave form to a wav file


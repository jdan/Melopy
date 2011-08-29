# Melopy (melo-pee)

#### A python library for playing with sound. 
#### by Jordan Scales (http://jordanscales.com) and friends
#### on Github: http://github.com/prezjordan/Melopy

For an example: check out canon.py 

    $ python examples/canon.py

To install:

    $ git clone git://github.com/prezjordan/Melopy
    $ cd Melopy
    $ sudo python setup.py install

To run the tests: (we've got some errors to work out)

    $ python setup.py test

or:

    $ pip install -r requirements.txt
    $ nosetests


## Library methods
    >>> # Returns the frequency of the note (key) keys from A0
    >>> melopy.frequency_from_key(49)
    440

    >>> # Returns the frequency of a note represented by a string
    >>> melopy.frequency_from_note('A4')
    440

    >>> # Returns the key number (keys from A0) from a note represented by a string
    >>> melopy.key_from_note('A4')
    49

    >>> # Returns a string representing a note which is (key) keys from A0
    >>> melopy.note_from_key(49)
    'A4'

    >>> # Calls iterate() with the starting note and the pattern [2,2,1,2,2,2]
    >>> melopy.generate_major_scale('D4')
    ['D4','E4','F#4','G4','A4','B4','C#5']

    >>> # Calls iterate with the starting note and the pattern [2,1,2,2,1,2]
    >>> melopy.generate_minor_scale('C4')
    ['C4','D4','E4','F4','G4','A4','A#4']

    >>> # Calls iterate with the starting note and the pattern [4, 3]
    >>> melopy.generate_major_triad('A4')
    ['A4', 'C#5', 'E5']

    >>> # Calls iterate with the starting note and the pattern [3, 4]
    >>> melopy.generate_minor_triad('C5')
    ['C5', 'D#5', 'G5']

All methods that return lists support choosing return types. The default return type is a list. example:

    >>> generate_minor_scale("A4","tuple")
    ('A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5')
    >>> generate_minor_scale("A4","dict")
    {0: 'A4', 1: 'B4', 2: 'C5', 3: 'D5', 4: 'E5', 5: 'F5', 6: 'G5'}



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

        # Destructor that calls render()
        __del__(self)

        # Adds a wave with a given frequency, length (in seconds) at a given location (in seconds)
        add_wave(self, wave_type, frequency, length, location='END')

        # Same as add_wave, but instead of frequency, the user provides a string representing a note (ie 'C5')
        # Also try add_quarter_note, add_half_note, add_whole_note, add_eighth_note, add_sixteenth_note instead of specifying a length
        add_note(self, note, length, wave_type='square', location='END')

        # Generates an array of notes given a starting note and a pattern of gaps between notes. This is better explained below
        iterate(self, start, pattern)

        # Adds given notes in a melody to the wave data, each having the given length
        add_melody(self, melody, length, wave_from [DEFAULT 'square'])

        # Adds a rest (nothing) for a given time (in seconds)
        # Also add_whole_rest, add_quarter_rest, etc. (instead of specifying a length)
        add_rest(self, length)

        # Renders the wave form to a wav file
        render(self)

## TODO
* Implement custom wave-types
* Create project page
* Add music reader
* Add types of scales?
* Fix scales to work properly (`d731ad5`)
* Write to wav file bitwise? Rather than having an overhead
# Melopy (melo-pee)

#### A python library for playing with sound. 
#### by Jordan Scales (http://jordanscales.com) and friends
#### on Github: http://github.com/prezjordan/Melopy

For an example: check out canon.py 

    $ python examples/canon.py

To install:

    $ git clone git://github.com/prezjordan/Melopy

To run the tests: (we've got some errors to work out)

    $ python setup.py test

or:

    $ pip install -r requirements.txt
    $ nosetests

## Organization

Melopy is broken down into 3 subcategories - `melopy`, `scales`, and `utility`.

* `melopy.py` contains the Melopy class 
    * this is used for creating a Melopy and adding notes to it, rendering, etc
* `scales.py` contains methods for generating scales
    * for instance, if you want to store the C major scale in an array
* `utility.py` contains methods for finding frequencies of notes, etc

## melopy.py

```
>>> from melopy import Melopy
>>> m = Melopy('mysong')
>>> m.add_quarter_note('A4')
>>> m.add_quarter_note('C#5')
>>> m.add_quarter_note('E5')
>>> m.render()
[==================================================] 100%
Done
```

## scales.py

* chromatic_scale    
* harmonic_minor_scale    
* major_pentatonic_scale    
* major_scale
* minor_scale
* major_triad
* minor_triad    
* melodic_minor_scale    
* minor_pentatonic_scale     

```
>>> from melopy.scales import *
>>> major_scale('C4')
['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
>>> major_scale('C4','dict')
{0: 'C4', 1: 'D4', 2: 'E4', 3: 'F4', 4: 'G4', 5: 'A4', 6: 'B4'}
>>> major_scale('C4','tuple')
('C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4')
>>> minor_scale('D#5')  # has some bugs
['D#5', 'F5', 'F#5', 'G#5', 'A#5', 'B5', 'C#6']
>>> major_triad('A4')
['A4', 'C#5', 'E5']
>>> major_triad('A4', 'tuple')
('A4', 'C#5', 'E5')
```

## utility.py

* frequency_from_key    
* frequency_from_note    
* key_from_note    
* note_from_key

```
>>> from melopy.utility import *
>>> frequency_from_key(49)
440.0
>>> frequency_from_note('A4')
440.0
>>> frequency_from_note('C5')
523.2511306011972
>>> key_from_note('Bb5')
62
>>> note_from_key(65)
'C#6'
>>> note_from_key(304) # even something stupid
'C26'
```

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
        add_wave(self, frequency, length, location='END')

        # Same as add_wave, but instead of frequency, the user provides a string representing a note (ie 'C5')
        #     If the octave is ignored, it is defaulted to 4. This can be changed by edited `self.octave`
        # Also try add_quarter_note, add_half_note, add_whole_note, add_eighth_note, add_sixteenth_note instead of specifying a length
        add_note(self, note, length, wave_type='square', location='END')
        # You can also replace `note` with an array of notes, i.e. (['C', 'E', 'G'] or ['A4', 'C#5', 'E5']) to add chords.

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
* Add option to listen to files before rendering out (Render into RAM, play and then dump?)
## Melopy

http://jdan.github.io/Melopy

A python library for playing with sound.<br />
*by [Jordan Scales](http://jordanscales.com) and friends*

### Install it

You may need to use `sudo` for this to work.

    $ pip install melopy

### Load it

```python
$ python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import melopy
>>> melopy.major_scale('C5')
['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']
>>>
```

### Development

To install locally:

    $ git clone git://github.com/jdan/Melopy
    $ cd Melopy
    $ python setup.py install

For examples, check out the `examples` directory:

    $ python examples/canon.py
    $ python examples/parser.py entertainer < examples/scores/entertainer.mlp

To run the tests:

    $ python tests/melopy_tests.py

### Organization

Melopy is broken down into 3 subcategories - `melopy`, `scales`, and `utility`.

* `melopy.py` contains the Melopy class
    * this is used for creating a Melopy and adding notes to it, rendering, etc
* `scales.py` contains methods for generating scales
    * for instance, if you want to store the C major scale in an array
* `utility.py` contains methods for finding frequencies of notes, etc

### melopy.py

```python
>>> from melopy import Melopy
>>> m = Melopy('mysong')
>>> m.add_quarter_note('A4')
>>> m.add_quarter_note('C#5')
>>> m.add_quarter_note('E5')
>>> m.render()
[==================================================] 100%
Done
```

### scales.py

* chromatic_scale
* harmonic_minor_scale
* major_pentatonic_scale
* major_scale
* minor_scale
* major_triad
* minor_triad
* melodic_minor_scale
* minor_pentatonic_scale

```python
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

### utility.py

* key_to_frequency
* key_to_note
* note_to_frequency
* note_to_key
* frequency_to_key
* frequency_to_note

```python
>>> from melopy.utility import *
>>> key_to_frequency(49)
440.0
>>> note_to_frequency('A4')
440.0
>>> note_to_frequency('C5')
523.2511306011972
>>> note_to_key('Bb5')
62
>>> key_to_note(65)
'C#6'
>>> key_to_note(304) # even something stupid
'C26'
>>> frequency_to_key(660)
56
>>> frequency_to_note(660)
'E5'
```

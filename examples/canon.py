#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys; sys.path.append(sys.path[0] + '/../')

from melopy import *

if __name__ == "__main__":
    m = Melopy('canon', 50)
    melody = []

    m.wave_type = 'sawtooth'

    for start in ['d4', 'a3', 'b3m', 'f#3m', 'g3', 'd3', 'g3', 'a3']:
        if start.endswith('m'):
            scale = DiatonicScale(start[:-1], DiatonicScale.Minor).scale
        else:
            scale = DiatonicScale(start, DiatonicScale.Major).scale

        scale.insert(0, scale[0][:-1] + str(int(scale[0][-1]) - 1))

        [melody.append(note) for note in scale]

    m.add_melody(melody, 0.2)
    m.add_rest(0.4)
    m.add_note('d4', 0.4)
    m.add_rest(0.1)
    m.add_note(['d4', 'a4', 'd5'], 0.8)

    m.render()

# Licensed under The MIT License (MIT)
# See LICENSE file for more


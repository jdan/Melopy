#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys; sys.path.append('../melopy/')

from melopy.melopy import Melopy

if __name__ == "__main__"
    song = Melopy('twinkle')

    song.tempo = 160
    song.wave_type = 'square'

    part1notes = ['C', 'G', 'A', 'G', 'F', 'E', 'D', 'C']
    part2notes = ['G', 'F', 'E', 'D']

    def twinkle(notes):
        for i in range(len(notes)):
            if i % 4 == 3:
                song.add_quarter_note(notes[i])
                song.add_quarter_rest()
            else:
                song.add_quarter_note(notes[i])
                song.add_quarter_note(notes[i])

    twinkle(part1notes)
    twinkle(part2notes)
    twinkle(part2notes)
    twinkle(part1notes)

    song.render()



#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utility import note_to_key, key_to_note, iterate
from exceptions import MelopyGenericError

SCALE_STEPS = {
    "major":[2,2,1,2,2,2,1],
    "melodic_minor":[2,1,2,2,2,2,1],
    "harmonic_minor":[2,1,2,2,2,1,2],
    "chromatic":[1,1,1,1,1,1,1,1,1,1,1],
    "major_pentatonic":[2,2,3,2],
    "minor_pentatonic":[3,2,2,3]
}

def _get_mode(steps, mode):
    """ Gets the correct mode step list by rotating the list """
    mode = mode - 1
    res = steps[mode:] + steps[:mode]
    return res

def generateScale(scale, note, mode=1, rType="list", octaves=True): #scale, start, type
    """
    Generate a scale
    scale (string): major,  melodic_minor, harmonic_minor, chromatic, major_pentatonic
    note: start note
    """
    if scale in SCALE_STEPS:
        steps = _get_mode(SCALE_STEPS[scale], mode)
        return iterate(note, steps, rType, octaves)
    else:
        raise MelopyGenericError("Unknown scale type:" + str(scale))

# Licensed under The MIT License (MIT)
# See LICENSE file for more

#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MelopyGenericError(Exception): pass
class MelopyValueError(ValueError): pass

from utility import note_to_key, key_to_note

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
            return ''.join(output)
        elif Type.lower() == "stringspace":
            return ' '.join(output)
        elif Type.lower() == "delemiter":
            return ','.join(output)
        else:
            raise MelopyGenericError("Unknown type: " + Type)
    else:
        raise MelopyGenericError("Input to bReturn is not a list! Input: " + str(output))

def iterate(start, pattern, rType="list", octaves=True):
    """Iterates over a pattern starting at a given note"""
    start_key = note_to_key(start)
    ret = [start_key]
    for step in pattern:
        ret.append(ret[-1] + step)

    for i, item in enumerate(ret):
        ret[i] = key_to_note(ret[i], octaves)

    return bReturn(ret, rType)

def major_scale(start, rType="list", octaves=True):
    """Generates a major scale using the pattern [2,2,1,2,2,2] (Returns: List)"""
    major_steps = [2,2,1,2,2,2]
    return iterate(start, major_steps, rType, octaves)

def minor_scale(start, rType="list", octaves=True): #Natural minor
    """Generates a minor scale using the pattern [2,1,2,2,1,2] (Returns: List)"""
    minor_steps = [2,1,2,2,1,2]
    return iterate(start, minor_steps, rType, octaves)
    #To be added: Harmonic and Melodic minor scales. Patterns: [2,1,2,2,2,1,2] | [2,1,2,2,2,2,1]

def melodic_minor_scale(start, rType="list", octaves=True):
    """Generates a melodic minor scale using the pattern [2,1,2,2,2,2,1]"""
    mminor_steps = [2,1,2,2,2,2,1]
    return iterate(start, mminor_steps, rType, octaves)

def harmonic_minor_scale(start, rType="list", octaves=True):
    """Generates a harmonic minor scale using the patter [2,1,2,2,2,1,2]"""
    hminor_steps = [2,1,2,2,2,1,2]
    return iterate(start, hminor_steps, rType, octaves)

def chromatic_scale(start, rType="list", octaves=True):
    """Generates a chromatic scale using the pattern [1,1,1,1,1,1,1,1,1,1,1] (Returns: List)"""
    chromatic_steps = [1,1,1,1,1,1,1,1,1,1,1]
    return iterate(start, chromatic_steps, rType, octaves)

def major_pentatonic_scale(start, rType="list", octaves=True):
    """Generates a major pentatonic scale using the pattern [2,2,3,2] (Returns: List)"""
    major_pentatonic_steps = [2,2,3,2]
    return iterate(start, major_pentatonic_steps, rType, octaves)

def minor_pentatonic_scale(start, rType="list", octaves=True):
    """Generates a minor pentatonic scale using the pattern [3,2,2,3] (Returns: List)"""
    minor_pentatonic_steps = [3,2,2,3]
    return iterate(start, minor_pentatonic_steps, rType, octaves)

def major_triad(start, rType="list", octaves=True):
    """Generates a major triad using the pattern [4,3] (Returns: List)"""
    major_triad = [4, 3]
    return iterate(start, major_triad, rType, octaves)

def minor_triad(start, rType="list", octaves=True):
    """Generates a minor triad using the pattern [3,4] (Returns: List)"""
    minor_triad = [3, 4]
    return iterate(start, minor_triad, rType, octaves)

def generateScale(scale, note, rType="list"): #scale, start, type
    """
    Generate a scale
    scale (string): major, minor, melodic_minor, harmonic_minor, chromatic, major_pentatonic
    note: start note
    """
    scales = {
        "major":major_scale,
        "minor":minor_scale,
        "melodic_minor":melodic_minor_scale,
        "harmonic_minor":harmonic_minor_scale,
        "chromatic":chromatic_scale,
        "major_pentatonic":major_pentatonic_scale,
        "minor_pentatonic":minor_pentatonic_scale
    }

    if scale in scales:
        return scales[scale](note, rType) #Places each individual argument into function call
    else:
        raise MelopyGenericError("Unknown scale type:"+str(scale))

# Licensed under The MIT License (MIT)
# See LICENSE file for more

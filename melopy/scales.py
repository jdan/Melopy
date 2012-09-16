class MelopyGenericError(Exception): pass
class MelopyValueError(ValueError): pass

from utility import key_to_note, note_to_key
from patternConstructor import *

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

def iterate(start, pattern, rType="list"):
    """Iterates over a pattern starting at a given note"""
    start_key = key_from_note(start)
    ret = [start_key]
    for step in pattern:
        ret.append(ret[-1] + step)
    ret = map(note_from_key, ret)
    return bReturn(ret, rType)
    
def major_scale(start):
    """generates a major scale in any key using correct spelling - build major scale pattern"""
    major_pattern = [0,2,2,1,2,2,2]
    
    """start by generating a scale of all natural notes starting at our start note"""
    natural_scale = get_base_pattern(start, [0,1,2,3,4,5,6])

    """use pattern builder to assign the correct sharps and flats based on the step pattern and note pattern"""
    return build_pattern(start, natural_scale, major_pattern)

def minor_scale(start, rType="list"): #Natural minor
    """Generates a minor scale in any key using correct spelling - build minor scale pattern"""
    minor_pattern = [0,2,1,2,2,1,2]

    """start by generating a scale of all natual notes starting at our start note"""
    natural_scale = get_base_pattern(start, [0,1,2,3,4,5,6])

    """use pattern builder to assign the correct sharps and flats based on the step pattern and note pattern"""
    return build_pattern(start, natural_scale, minor_pattern)

def melodic_minor_scale(start, rType="list"):
    """Generates a melodic minor scale in any key with correct spelling"""
    melodic_pattern = [0,2,1,2,2,2,2]

    """start by generating a scale of all natural notes starting at our start note"""
    natural_scale = get_base_pattern(start, [0,1,2,3,4,5,6])

    """use pattern builder to assign the correct sharps and flats based on step pattern and note pattern"""
    return build_pattern(start, natural_scale, melodic_pattern)


def harmonic_minor_scale(start, rType="list"):
    """Generates a harmonic minor scale in any key with correct spelling"""
    harmonic_pattern = [0,2,1,2,2,1,3]

    """start by generating a scale of all natural notes starting at our start note"""
    natural_scale = get_base_pattern(start, [0,1,2,3,4,5,6])

    """use pattern builder to assign the correct sharps and flats based on step pattern and note pattern"""
    return build_pattern(start, natural_scale, harmonic_pattern)

def chromatic_scale(start, rType="list"):
    """Generates a chromatic scale using the pattern [1,1,1,1,1,1,1,1,1,1,1] (Returns: List)"""
    chromatic_steps = [1,1,1,1,1,1,1,1,1,1,1]
    return iterate(start, chromatic_steps, rType)

def major_pentatonic_scale(start):
    """Generates a major pentatonic scale in any key with correct spelling"""
    pent_pattern = [0,2,2,3,2]

    """start by generating a scale of all natural notes starting at our start note"""
    natural_scale = get_base_pattern(start, [0,1,2,4,5])

    """use pattern builder to assign the correct sharps and flats based on th step pattern and note pattern"""
    return build_pattern(start, natural_scale, pent_pattern)

def minor_pentatonic_scale(start):
    """Generates a minor pentatonic scale in any key with correct spelling"""
    pent_pattern = [0,3,2,2,3]

    """start by generating a scale of all natural notes starting at our start note"""
    natural_scale = get_base_pattern(start, [0,2,3,4,6])

    """use pattern builder to assign the correct sharps and flats based on the step pattern and note pattern"""
    return build_pattern(start, natural_scale, pent_pattern)

def major_triad(start):
    """generates a major triad in any key using correct spelling"""
    major_pattern = [0,4,3]

    """start by generating a triad of natural notes from our starting note"""
    natural_triad = get_base_pattern(start, [0,2,4])

    """use pattern builder to assign the correct sharps and flats based on the step pattern and note pattern"""
    return build_pattern(start, natural_triad, major_pattern)

def minor_triad(start):
    """generates a minor triad in any key with correct spelling"""
    minor_pattern = [0,3,4]

    """start by generating a triad of natural notes from our start note"""
    natural_triad = get_base_pattern(start, [0,2,4])

    """use pattern builder to assign the correct sharps and flats based on the step pattern and note pattern"""
    return build_pattern(start, natural_triad, minor_pattern)

def diminished_triad(start):
    """generates a diminished triad in any key with correct spelling"""
    diminished_pattern = [0,3,3]

    """start by generating a triad of natural notes from our start note"""
    natural_triad = get_base_pattern(start, [0,2,4])

    """use pattern builder to assign the correct sharps and flats based on the step pattern and note pattern"""
    return build_pattern(start, natural_triad, diminished_pattern)

def augmented_triad(start):
    """generates an augmented triad in any key with correct spelling"""
    augmented_pattern = [0,4,4]

    """start by generating a triad of natural notes from our start note"""
    natural_triad = get_base_pattern(start, [0,2,4])

    """use pattern builder to assign the correct sharps and flats based on the step pattern and note pattern"""
    return build_pattern(start, natural_triad, augmented_pattern)

def get_diatonic_interval(note, note_set, basic_interval):
    i = 0

    if len(note) == 1: note += '5'
    
    for pitch in note_set:
        if pitch[0:len(pitch)-1] == note[0:len(note)-1]:
            if i + basic_interval -1 < 8:
                return note_set[i + basic_interval - 1]
            else:
                return note_set[i + basic_interval - 8]
        i = i + 1

def genScale(scale, note, rType="list"): #scale, start, type
    """Example of better way to do scale generation @NOTE: Please don't use this in production! It might be taken out at a later time..."""
    scales = {
        "major":major_scale,
        "minor":minor_scale,
        "melodic_minor":melodic_minor_scale,
        "harmonic_minor":harmonic_minor_scale,
        "chromatic":chromatic_scale,
        "major_pentatonic":major_pentatonic_scale
    }

    if scale in scales:
        return scales[scale](note, rType) #Places each individual argument into function call
    else:
        raise MelopyGenericError("Unknown scale type:"+str(scale))

# Licensed under The MIT License (MIT)
# See LICENSE file for more

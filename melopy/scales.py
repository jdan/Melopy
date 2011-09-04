class MelopyGenericError(Exception): pass
class MelopyValueError(ValueError): pass

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
    
def generate_major_scale(start, rType="list"):
    """Generates a major scale using the pattern [2,2,1,2,2,2] (Returns: List)"""
    major_steps = [2,2,1,2,2,2]
    return iterate(start, major_steps, rType)

def generate_minor_scale(start, rType="list"): #Natural minor
    """Generates a minor scale using the pattern [2,1,2,2,1,2] (Returns: List)"""
    minor_steps = [2,1,2,2,1,2]
    return iterate(start, minor_steps, rType)
    #To be added: Harmonic and Melodic minor scales. Patterns: [2,1,2,2,2,1,2] | [2,1,2,2,2,2,1]

def generate_melodic_minor_scale(start, rType="list"):
    """Generates a melodic minor scale using the pattern [2,1,2,2,2,2,1]"""
    mminor_steps = [2,1,2,2,2,2,1]
    return iterate(start, mminor_steps, rType)

def generate_harmonic_minor_scale(start, rType="list"):
    """Generates a harmonic minor scale using the patter [2,1,2,2,2,1,2]"""
    hminor_steps = [2,1,2,2,2,1,2]
    return iterate(start, hminor_steps, rType)

def generate_chromatic_scale(start, rType="list"):
    """Generates a chromatic scale using the pattern [1,1,1,1,1,1,1,1,1,1,1] (Returns: List)"""
    chromatic_steps = [1,1,1,1,1,1,1,1,1,1,1]
    return iterate(start, chromatic_steps, rType)

def generate_major_pentatonic_scale(start, rType="list"):
    """Generates a major pentatonic scale using the pattern [2,2,3,2] (Returns: List)"""
    major_pentatonic_steps = [2,2,3,2]
    return iterate(start, major_pentatonic_steps, rType)

def generate_minor_pentatonic_scale(start, rType="list"):
    """Generates a minor pentatonic scale using the pattern [3,2,2,3] (Returns: List)"""
    minor_pentatonic_steps = [3,2,2,3]
    return iterate(start, minor_pentatonic_steps, rType)

def generate_major_triad(start,rType="list"):
    """Generates a major triad using the pattern [4,3] (Returns: List)"""
    major_triad = [4, 3]
    return iterate(start, major_triad, rType)

def generate_minor_triad(start,rType="list"):
    """Generates a minor triad using the pattern [3,4] (Returns: List)"""
    minor_triad = [3, 4]
    return iterate(start, minor_triad, rType)

def genScale(scale, note, rType="list"): #scale, start, type
    """Example of better way to do scale generation @NOTE: Please don't use this in production! It might be taken out at a later time..."""
    scales = {
        "major":generate_major_scale,
        "minor":generate_minor_scale,
        "melodic_minor":generate_melodic_minor_scale,
        "harmonic_minor":generate_harmonic_minor_scale,
        "chromatic":generate_chromatic_scale,
        "major_pentatonic":generate_major_pentatonic_scale
    }
    if scale in scales:
        return scales[scale](note, rType) #Places each individual argument into function call
    else:
        raise MelopyGenericError("Unknown scale type:"+str(scale))
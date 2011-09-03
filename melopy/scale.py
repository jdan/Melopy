"""
Scale Class.
"""
from __future__ import absolute_import

from melopy.utility import iterate
from melopy.utility import key_from_note

# TODO move Exceptions into a file 'melopy.exception'
class UnknownScale(Exception):
    """
    Exception class for unknown scales
    """
    def __init__(self, unknownScale, scaleClass) :
        """
        Constructor.

        @param unknownScale: Name of unknown scale
        @type unknownScale: str
        """
        self.err = 'Given scale "{}" is unknown. Known scales are:\n{}\n'.format(
                    unknownScale, 
                    ' '.join(scaleClass.ScaleIntervals.keys()))

    def __str__(self):
        return self.err


class UnknownTriad(Exception):
    """
    Exception class for unknown triads
    """
    def __init__(self, unknownTriad) :
        """
        Constructor.

        @param unknownTriad: Name of unknown scale
        @type unknownTriad: str
        """
        self.err = 'Given triad "{}" is unknown. Known triads are:\n{}\n'.format(
                    unknownTriad, 
                    ' '.join(DiatonicScale.Triad.Roots.keys()))

    def __str__(self):
        return self.err



class Scale(object):
    """
    Scale will be used to obtain information about those scale... e. g.:
        
        - provide special information for different scales
        - get triad as iterable or chord (tonic, subdominant, dominant) [only in diatonic]
        - get parallel moll
        - iterate over scale (__iter__)
    """

    def __init__(self, root, scaleIntervals):
        """
        Constructor.

        @param root: root note of scale
        @param scaleIntervals: list contains intervals to build scale from given root note.
        """
        #: List representation of scale
        self.scale = iterate(root, scaleIntervals, "list")
        #: Octave of root ==> octave of scale
        self.octave = int(self.scale[0][-1])

#       self.root = root
#       self.rootKey = key_from_note(root)
#       self.scaleIntervals = ScaleIntervals[scale]

    def __str__(self):
        return '-'.join(self.scale)

    def __iter__(self):
        self.scale

#   @property
#   def scale(self):
#       """
#       @return: Scale over one octave
#       @rtype: list
#       """
#       return [self.root] + [note_from_key(rootKey + interval) for interval in self.scaleIntervals]

    def get_note(self, noteIndex):
        """
        Returns note at given index in scale.

        e.g.::
            diatonic c4 major:

            ... a3 b3 c4 d4 e4 f4 g4 a4 b4 c5 d5 e5 ...
                -2 -1 |0  1  2  3  4  5  6| 7  8  9
                        

        @return: Note in Scale
        @rtype: str
        """
        octave = self.octave + noteIndex / len(self.scale)
        
        # TODO Exception class?
        assert octave >= 0, 'This note does not exist!'

        #           repersenting note in scale        'F#5' -> 'F#'
        #      .----------------+--------------------..-+-.      
        note = self.scale[noteIndex % len(self.scale)][:-1] + str(octave)

        return note

    def get_chord(self, noteIndices):
        """
        Returns chord.

        e.g.::
            get chord Cmaj 1-3-5:
                c4maj.get_chord([0, 2, 4]) --> ['C4', 'E4', 'G4']
        """
        chordRootNoteIndex = noteIndices[0]
        chordRootNote = self.get_note(chordRootNoteIndex)
        chord = [chordRootNote] + [self.get_note(chordRootNoteIndex + i) for i in noteIndices[1:]]

        return chord
       

class DiatonicScale(Scale):
    """
    DiatonicScale.
    """

    #: Diatonic scale types
    Minor = 'minor'
    Major = 'major'
    
    #: Scale intervals
    ScaleIntervals = {
        Major       : (2,2,1,2,2,2)     ,   
        Minor       : (2,1,2,2,1,2)     ,
    }

    class Triad(object):
        """
        Defines Triad for this class.
        """
        #: Diatonic triads 
        Tonic          = 'tonic'
        Supertonic     = 'supertonic'
        Mediant        = 'mediant'
        Subdominant    = 'subdominant'
        Dominant       = 'dominant'
        Submediant     = 'submediant'
        Subtonic       = 'subtonic'

        #: Triads root note
        Roots = {
            Tonic          : 0 ,
            Supertonic     : 1 ,
            Mediant        : 2 ,
            Subdominant    : 3 ,
            Dominant       : 4 ,
            Submediant     : 5 ,
            Subtonic       : 6 ,
        }


    def __init__(self, root, scale):
        """
        Constructor.

        @param root: Root note.
        @param scale: Type of Diatonic scale
        """
        if self.ScaleIntervals.has_key(scale):
            Scale.__init__(self, root, self.ScaleIntervals[scale])
        else:
            raise UnknownScale(scale, self)

    def get_triad(self, triad, rType="list"):
        """
        Getter for scales triads.

        @param triad: Name of triad
        @type type: str

        @param rType: Name of iterable type
        @type rType: str

        @return: Sequence of requested triad of current scale
        @rtype: depends on rType
        """
        
        if not self.Triad.Roots.has_key(triad):
            raise UnknownTriad(triad)

        return self.get_chord((self.Triad.Roots[triad], 2, 4))


class OctatonicScale(Scale):
    """
    Octatonic
    """

    Half   = 'half'
    Whole  = 'whole'
    
    ScaleIntervals = {
        Half   : (1,2,1,2,1,2,1,2) ,
        Whole  : (2,1,2,1,2,1,2,1)
    }

    def __init__(self, root, scale):
        """
        Constructor.
        """
        if self.ScaleIntervals.has_key(scale):
            Scale.__init__(self, root, self.ScaleIntervals[scale])
        else:
            raise UnknownScale(scale, self)

class MelodicScale(Scale):
    """
    Melodic.
    """

    Major = 'major'
    Minor = 'minor'
    
    ScaleIntervals = {
        Major   : (2,2,1,2,1,2) ,
        Minor   : (2,1,2,2,2,2)
    }
    
    def __init__(self, root, scale):
        """
        Constructor.
        """
        if self.ScaleIntervals.has_key(scale):
            Scale.__init__(self, root, self.ScaleIntervals[scale])
        else:
            raise UnknownScale(scale, self)



class HarmonicScale(Scale):
    """
    Harmonic.
    """

    Major   = 'major'
    Minor   = 'minor'

    ScaleIntervals = {
        Major   : (2,2,1,2,1,3) ,
        Minor   : (2,1,2,2,1,3)
    }
    
    def __init__(self, root, scale):
        """
        Constructor.
        """
        if self.ScaleIntervals.has_key(scale):
            Scale.__init__(self, root, self.ScaleIntervals[scale])
        else:
            raise UnknownScale(scale, self)


class PentatonicScale(Scale):
    """
    Pentatonic.
    """
    Major = 'major'
    Minor = 'minor'


#: Dictionary, which contains intervals for previously defined scale names.
#: Building scales by using this intervals.
    ScaleIntervals = {
        Major : (2,2,3,2)         ,
        Minor : (3,2,2,3)         ,
    }

    def __init__(self, root, scale):
        """
        Constructor.
        """
        if self.ScaleIntervals.has_key(scale):
            Scale.__init__(self, root, self.ScaleIntervals[scale])
        else:
            raise UnknownScale(scale, self)


class ChromaticScale(Scale):
    """
    Chromatic.
    """

    def __init__(self, root):
        """
        Constructor.
        """
        Scale.__init__(self, root, (1,1,1,1,1,1,1,1,1,1,1)) 

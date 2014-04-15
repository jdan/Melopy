#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utility import note_to_key, key_to_note, iterate

# Interval lists for the chords, choosing to add the interval to get to the
# upper tonic for easier inversion of chords
CHORD_INTERVALS = {
  'maj': [4,3,5],
  'min': [3,4,5],
  'aug' : [4,4,4],
  'dim' : [3,3,6],
  '7': [4,3,3,2],
  'maj7': [4,3,4,1],
  'min7': [3,4,3,2],
  'minmaj7': [3,4,4,1],
  'dim7': [3,3,3,3,3]
}

def _get_inversion(chord, inversion):
  return chord[inversion:] + chord[:inversion]

def generateChord(name, tonic, inversion=0, rType='list', octaves=True):
  if name in CHORD_INTERVALS:
      steps = _get_inversion(CHORD_INTERVALS[name],inversion)
      return iterate(tonic, steps, rType, octaves)
  else:
     raise MelopyGenericError("Unknown Chord:"+str(name))


# Licensed under The MIT License (MIT)
# See LICENSE file for more

#!/usr/bin/env
# -*- coding: utf-8 -*-

from unittest import TestCase

from nose.tools import *

from melopy.utility import *
from melopy.scales import *

class LibraryFunctionsTests(TestCase):
    def test_frequency_from_key(self):
        key = 49
        self.assertEqual(frequency_from_key(key), 440)

    def test_frequency_from_note(self):
        note = 'A4'
        self.assertEqual(frequency_from_note(note), 440)

    def test_key_from_note(self):
        note = 'A4'
        self.assertEqual(key_from_note(note), 49)

    def test_note_from_key(self):
        key = 49
        self.assertEqual(note_from_key(key), 'A4')

    def test_iterate(self):
        start = 'D4'
        pattern = [2, 2, 1, 2, 2, 2]
        should_be = ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5']
        self.assertEqual(iterate(start, pattern), should_be)

    def test_DiatonicScale(self):
        diatonicCMaj = DiatonicScale('C', DiatonicScale.Major)
        shouldBeDiatonicCMaj = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
        self.assertEqual(diatonicCMaj.scale, shouldBeDiatonicCMaj)

        diatonicCMin = DiatonicScale('C', DiatonicScale.Minor)
        # TODO Better notation would be...
        # TODO ['C4', 'D4', 'Eb4', 'F4', 'G4', 'Ab4', 'B4b']
        shouldBeDiatonicCMin = ['C4', 'D4', 'D#4', 'F4', 'G4', 'G#4', 'A#4']
        self.assertEqual(diatonicCMin.scale, shouldBeDiatonicCMin)

    def test_MelodicScale(self):
        melodicCMaj = MelodicScale('C', MelodicScale.Major)
        shouldBeMelodicCMaj = ['C4', 'D4', 'E4', 'F4', 'G4', 'G#4', 'A#4']
        self.assertEqual(melodicCMaj.scale, shouldBeMelodicCMaj)

        melodicCMin = MelodicScale('C', MelodicScale.Minor)
        shouldBeMelodicCMin = ['C4', 'D4', 'D#4', 'F4', 'G4', 'A4', 'B4']
        self.assertEqual(melodicCMin.scale, shouldBeMelodicCMin)

    def test_HarmonicScale(self):
        harmonicCMaj = HarmonicScale('C', HarmonicScale.Major)
        shouldBeHarmonicCMaj = ['C4', 'D4', 'E4', 'F4', 'G4', 'G#4', 'B4']
        self.assertEqual(harmonicCMaj.scale, shouldBeHarmonicCMaj)
       
        harmonicCMin = HarmonicScale('C', HarmonicScale.Minor)
        shouldBeHarmonicCMin = ['C4', 'D4', 'D#4', 'F4', 'G4', 'G#4', 'B4']
        self.assertEqual(harmonicCMin.scale, shouldBeHarmonicCMin)

    def test_PentatonicScale(self):
        pentatonicCMaj = PentatonicScale('C', PentatonicScale.Major)
        shouldBePentatonicCMaj = ['C4', 'D4', 'E4', 'G4', 'A4']
        self.assertEqual(pentatonicCMaj.scale, shouldBePentatonicCMaj)
    
        pentatonicCMin = PentatonicScale('C', PentatonicScale.Minor)
        shouldBePentatonicCMin = ['C4', 'D#4', 'F4', 'G4', 'A#4']
        self.assertEqual(pentatonicCMin.scale, shouldBePentatonicCMin)

    def test_ChromaticScale(self):
        chromaticC = ChromaticScale('C')
        shouldBeChromaticC = ['C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4']
        self.assertEqual(chromaticC.scale, shouldBeChromaticC)

    def test_DiatonicTriad(self):
        diatonicCMaj = DiatonicScale('C', DiatonicScale.Major)

        triadTonic = diatonicCMaj.get_triad(DiatonicScale.Triad.Tonic)
        triadSupertonic = diatonicCMaj.get_triad(DiatonicScale.Triad.Supertonic)
        triadMediant = diatonicCMaj.get_triad(DiatonicScale.Triad.Mediant)     
        triadSubdominant = diatonicCMaj.get_triad(DiatonicScale.Triad.Subdominant)
        triadDominant = diatonicCMaj.get_triad(DiatonicScale.Triad.Dominant)   
        triadSubmediant = diatonicCMaj.get_triad(DiatonicScale.Triad.Submediant)  
        triadSubtonic = diatonicCMaj.get_triad(DiatonicScale.Triad.Subtonic)  

        shouldBeTonic = ['C4', 'E4', 'G4']
        shouldBeSupertonic = ['D4', 'F4', 'A4']
        shouldBeMediant = ['E4', 'G4', 'B4']
        shouldBeSubdominant = ['F4', 'A4', 'C5']
        shouldBeDominant = ['G4', 'B4', 'D5']
        shouldBeSubmediant = ['A4', 'C5', 'E5']
        shouldBeSubtonic = ['B4', 'D5', 'F5']

        self.assertEqual(triadTonic, shouldBeTonic)
        self.assertEqual(triadSupertonic, shouldBeSupertonic)
        self.assertEqual(triadMediant, shouldBeMediant)
        self.assertEqual(triadSubdominant, shouldBeSubdominant)
        self.assertEqual(triadDominant, shouldBeDominant)
        self.assertEqual(triadSubmediant, shouldBeSubmediant)
        self.assertEqual(triadSubtonic, shouldBeSubtonic)


class MelopyTests(TestCase):
    def test_dummy(self):
        assert True

# Licensed under The MIT License (MIT)
# See LICENSE file for more

def get_base_pattern(startNote, pattern):
	"""takes a starting note and a pattern and generates a scale of all natural notes"""
	"""used in conjunction with build_pattern to create scales and chords with correct spellings"""
	"""every scale/chord can be constructed in a two-phase manner:  first create the list of notes"""
	"""without accidentals so that spelling can be done correctly, then add correct flats/sharps"""
	"""to match the half/whole step pattern of the chord/scale you are trying to build"""
	natural_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
	retPattern = []
	
	for i in range(0, len(natural_notes)):
		if natural_notes[i] == startNote[0]:
			start = i

	for degree in pattern:
		if start + degree > 6: degree = degree - 7
		retPattern.append(natural_notes[start + degree])

	return retPattern

def build_pattern(startNote, base_pattern, step_pattern):
	"""this function is the key to building all scales and chords.  It will take a starting note, a pattern of natural notes"""
	"""and a pattern of half steps and combine them together to build the chord or scale with correct spelling - """
	"""aka use of sharps/flats/double sharps/double flats"""

	"""running list of notes added to this scale/chord"""
	retScale = []

	"""set octave to 4 by default"""
	octave = 4

	"""if the input included the octave to use then lets use that instead"""
	"""once we have the octave set we can trim that bit off of our startNote, we don't need it anymore"""
	if startNote[-1] in '01234567':
		octave = int(startNote[-1])
		startNote = startNote[0:len(startNote)-1]

	"""build a list of all chromatic tones and their possible enharmonic equivalents"""
	"""using * to represent double sharp (##) and % to represent double flat (bb) so each only takes on character"""
	fullscale = [
			['G*', 'A', 'B%'],
			['A#', 'Bb', 'C%'],
			['A*', 'B', 'Cb'],
			['B#', 'C', 'D%'],
			['B*', 'C#', 'Db'],
			['C*', 'D', 'E%'],
			['D#', 'Eb', 'F%'],
			['D*', 'E', 'Fb'],
			['E#', 'F', 'G%'],
			['E*', 'F#', 'Gb'],
			['F*', 'G', 'A%'],
			['G#', 'Ab'] ]

	"""lets see what index of fullscale we are going to start on"""
	for i in range(0, len(fullscale)):
		for note in fullscale[i]:
			if note == startNote.replace('bb', '%').replace('##', '*'):
				currentPosition = i

	"""lets go through each step in the pattern we recieved"""
	for x in range(0, len(step_pattern)):
		"""if we go past the last element of the list, jump down an octave and continue counting"""
		if currentPosition + step_pattern[x] > 11: currentPosition = currentPosition - 12

		"""we have the correct enharmonic slot we need based on the number of half-steps, but we need"""
		"""to know which version of that pitch to use - we want the one that start with our base_note"""
		for note in fullscale[currentPosition + step_pattern[x]]:
			if note[0] == base_pattern[x]:
				if base_pattern[x] == 'C' and x > 0: octave+= 1
				retScale.append(note.replace('%', 'bb').replace('*', '##') + str(octave))

		""" adjust our current position to reflect the most recent note processed"""
		currentPosition += step_pattern[x]

	return retScale

		

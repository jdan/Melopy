from melopy import *

m = Melopy('canon', 50)
melody = []

for start in ['d4', 'a3', 'b3m', 'f#3m', 'g3', 'd3', 'g3', 'a3']:
	if start.endswith('m'):
		scale = m.generate_minor_triad(start[:-1])
	else:
		scale = m.generate_major_triad(start)
	
	for note in scale:
		melody.append(note)

m.add_melody(melody, 0.2)
m.add_note('e4', 0.2)
m.render()
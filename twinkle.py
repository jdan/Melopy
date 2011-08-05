from melopy import *

song = Melopy('twinkle')
t = 0.25

part1notes = ['C', 'G', 'A', 'G', 'F', 'E', 'D', 'C']
part2notes = ['G', 'F', 'E', 'D']

def twinkle(notes):
	for i in range(len(notes)):
		if i % 4 == 3:
			song.add_note(notes[i], t*2)
		else:
			song.add_note(notes[i], t)
			song.add_note(notes[i], t)
			
twinkle(part1notes)
twinkle(part2notes)
twinkle(part2notes)
twinkle(part1notes)

song.render()
		



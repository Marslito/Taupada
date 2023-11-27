from music21 import *

# Create a stream to represent the musical notation
s = stream.Stream()

# Create a time signature of 2/4
ts = meter.TimeSignature('2/4')
s.append(ts)

# Create two measures, each with a whole note in 2/4 time signature
for _ in range(2):
    m = stream.Measure()
    m.append(note.Whole())
    s.append(m)

# Create a staff and add the music to it
staff = stream.Part()
staff.append(s)
score = stream.Score()
score.append(staff)

# Show the music notation in a pentagram
score.show()
from turing_machine import TuringMachine


machine = TuringMachine(
    {
        ('q0', '#'): ('saw_#', '#', 'R'),
        ('saw_#', '#'): ('saw_##', '#', 'R'),
        ('saw_##', ''): ('qa', '', 'R'),
    }
)

w = "##" #try some strings here to find out what the machine accepts and rejects
print("Input:",w)
print("Accepted?", machine.accepts(w))

'''
starts
at      state q0     reads a     '#'     shifts state to saw_#      writes a '#'    moves to right
at      state saw_#  reads a     '#'     shifts state to saw_##     writes a '#'    moves to right (i.e. now has read two hashes writes)
at      state saw_## reads a     ''      shifts state to qa         writes a ''     HALT
ends
'''
"""
Just reads two #'s
"""

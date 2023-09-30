# A tuple consists of a number of values separated by commas, for instance:

t = 12345, 54321, 'hello!'
t[0]
# output 12345
t
# output (12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
# output ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
t[0] = 88888

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
# output ([1, 2, 3], [3, 2, 1])

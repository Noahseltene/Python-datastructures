fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)  # Find next banana starting at position 4
fruits.reverse()
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()

# List comprehensions
squares = []
for x in range(10):
    squares.append(x**2)

squares
# output [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# OR 
squares = list(map(lambda x: x**2, range(10)))

# OR equivalently 
squares = [x**2 for x in range(10)]


# using the del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]

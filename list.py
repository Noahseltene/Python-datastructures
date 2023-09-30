fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting at position 4
fruits.reverse()
print(fruits)
# output ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
print(fruits)
# output ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)
# output ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
print(fruits.pop())
print(fruits)

# List comprehensions
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
# output [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# OR 
squares = list(map(lambda x: x**2, range(10)))

# OR equivalently 
squares = [x**2 for x in range(10)]
print(squares)


# using the del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

#  A set is an unordered collection with no duplicate elements.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
#  output {'orange', 'banana', 'pear', 'apple'}
print('orange' in basket)              # fast membership testing
# output True
print('crabgrass' in basket)
# output False

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)     
print(b)                         # unique letters in a
# output {'a', 'r', 'b', 'c', 'd'}
print(a - b)                              # letters in a but not in b
# output {'r', 'd', 'b'}
print(a | b)                            # letters in a or b or both
# output {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)                           # letters in both a and b
# output {'a', 'c'}
print(a ^ b)                           # letters in a or b but not both
# output {'r', 'd', 'b', 'm', 'z', 'l'}
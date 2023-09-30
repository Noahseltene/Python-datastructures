#  A set is an unordered collection with no duplicate elements.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
#  output {'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 # fast membership testing
# output True
'crabgrass' in basket
# output False

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
# output {'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
# output {'r', 'd', 'b'}
a | b                              # letters in a or b or both
# output {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b
# output {'a', 'c'}
a ^ b                              # letters in a or b but not both
# output {'r', 'd', 'b', 'm', 'z', 'l'}
##

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
## output {'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
## output 4098
del tel['sape']
tel['irv'] = 4127
tel
## output {'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
['jack', 'guido', 'irv']
sorted(tel)
##output ['guido', 'irv', 'jack']
'guido' in tel
##output True
'jack' not in tel
##output False


## Dict comprehensions
{x: x**2 for x in (2, 4, 6)}
##output {2: 4, 4: 16, 6: 36}


## Looping techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

## output gallahad the pure
## output robin the brave


#using enumerate method
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
"""
--output--
0 tic
1 tac
2 toe

"""


## using the zip method

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
"""
Output

What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

"""
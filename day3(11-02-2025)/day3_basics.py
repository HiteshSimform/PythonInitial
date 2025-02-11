'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = 'global x'

def test():
    y = 'local y'
    print(y)

test()

import keyword
print(keyword.kwlist)


# Reduce Redundecy and Reuse the code


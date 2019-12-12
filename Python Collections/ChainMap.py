import collections as c
""" 1 ) ChainMap() function"""

d1={1:"a",2:"b"}
d2={3:"c",4:"d"}
print(c.ChainMap(d1,d2))

# Output : ChainMap({1: 'a', 2: 'b'}, {3: 'c', 4: 'd'})

""" 2 ) ChainMap() function with maps(returns result as list)"""

d1={1:"a",2:"b"}
d2={3:"c",4:"d"}
print(c.ChainMap(d1,d2).maps)

# Output : [{1: 'a', 2: 'b'}, {3: 'c', 4: 'd'}]

""" 3 ) ChainMap() function with maps(returns result as list) => Accessing a specific key or value in chainmap list"""

d1={1:"a",2:"b"}
d2={3:"c",4:"d"}
print(c.ChainMap(d1,d2).maps[1][4])

# Output :  d

""" 4 ) ChainMap() function with maps(returns result as list) =>
 Accessing a specific key or value in chainmap list Alternate method using get method"""

d1={1:"a",2:"b"}
d2={3:"c",4:"d"}
print(c.ChainMap(d1,d2).get(4))

# Output :  d

""" 5 ) ChainMap() function accessing keys and values of two dictionaries """

d1={1:"a",2:"b"}
d2={3:"c",4:"d"}
print(list(c.ChainMap(d1,d2).keys()))
print(list(c.ChainMap(d1,d2).values()))

# Output : [3, 4, 1, 2]
#          ['c', 'd', 'a', 'b']

""" new_child() function Adding new dictionary to chain map """

d1={1:"a",2:"b"}
d2={3:"c",4:"d"}
d3 = {5:"e"}
print(c.ChainMap(d1,d2).new_child(d3))

# Output : 
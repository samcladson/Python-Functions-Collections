import collections as c
"""Counter counts the frequency of element and elemrnts() function 
prints the element upto that frequency"""

test_input = "sam cladson"
print(list(c.Counter(test_input).elements()))

# Output : ['s', 's', 'a', 'a', 'm', ' ', 'c', 'l', 'd', 'o', 'n']

test_input = "sam cladson"
print(sorted(list(c.Counter(test_input).elements())))
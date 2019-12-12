import collections as c

""" 1) Ordered dictionary ( maintains the structure of the dictionary )"""

a = c.Counter({"pen":2,"pencil":4,"scale":6})
b = c.Counter({"pen":1,"pencil":1,"scale":4})
a.subtract(b)
print(c.OrderedDict(a))


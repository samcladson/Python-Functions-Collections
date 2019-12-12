import collections as c
a = c.Counter({"pen":2,"pencil":4,"scale":6})
b = c.Counter({"pen":1,"pencil":1,"scale":4})
a.subtract(b)
print(a)
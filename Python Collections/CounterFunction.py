import collections as c

# Reduce function example

# from functools import reduce as r
# list_1 =  [1,2,3,4]
# result = r((lambda x,y: x*y),list_1)
# print(result)

""" Counter Function"""

l = [1,2,1,2,3,4,2,1]
print(c.Counter(l))

#Output : Counter({1: 3, 2: 3, 3: 1, 4: 1})

"""Counter Most_common() function"""

l = [1,2,1,2,3,4,2,1]
print(c.Counter(l).most_common())

#Output : [(1, 3), (2, 3), (3, 1), (4, 1)]

"""Counter Most_common() function with parameter"""
l = [1,2,1,2,3,4,2,1]
print(c.Counter(l).most_common(3))

# Output : [(1, 3), (2, 3), (3, 1)]

"""Counter Most_common() function with parameter accessing required element"""
l = [1,2,1,2,3,4,2,1]
print(c.Counter(l).most_common(2)[0][0])

# Output : 1
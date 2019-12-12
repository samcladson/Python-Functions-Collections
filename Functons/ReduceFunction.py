# Reduce function example

from functools import reduce as r
list_1 =  [1,2,3,4]
result = r((lambda x,y: x*y),list_1)
print(result)

# Output : 24
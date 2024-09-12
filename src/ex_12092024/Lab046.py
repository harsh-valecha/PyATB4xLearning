# collections
# deque - double ended queue , same as list but contains endpoints

from collections import deque , OrderedDict
#create a deque
d1 = deque()
d2 = deque([1,2,3])
# print(d2)

# adding elements
d1.append(23)
# print(d1)

d2.extend([2,3])
print(d2)
d2.pop()# pops from right
print(d2)
d2.popleft() # pops from left

# OrderedDict same as dict but remembers the order
d = OrderedDict({
    "name":"Kamlesh",
    "kaam":"Jaktu"
})
print(d)
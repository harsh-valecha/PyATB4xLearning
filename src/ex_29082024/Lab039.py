lst= [1,2,2,3,3,4,5,6,6,6,6]

# set - unordered collection of unique elements
# represented using {}
# removing

print(set(lst))
for i in set(lst):
    print(i)


set1 = {1,2,3}
set2= {3,4,5}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.issubset(set1))

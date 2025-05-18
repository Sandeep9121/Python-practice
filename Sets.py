set_1 = {"a", "b", "c", "c"}
print(set(set_1))


set_range = set(range(1,20,2))
print(set_range)

print(10 in  set_range)

#set useful to remove the duplicates but it is unordered

# Set Methods
# add()

my_set = {1, 2, 3, 4, 5,55,62}

my_set.add(6)
print(my_set)
my_set.remove(3)
my_set.discard(9) #Removes an element if it exists. No error if the element is not found.
print(my_set)

my_set.update([7, 8, 9])
print(my_set)

#pop Removes and returns a random element from the set.

my_set.pop()
print(my_set)

# union
a = {1, 2}
b = {2, 3}
result = a.union(b)

print(result)

#intersaction
a1 = {1, 2, 3}
b1 = {2, 3, 4}
result1= a1.intersection(b1)
print(result1)


# difference
a2 = {1, 2, 3}
b2= {2, 3}
result3 = a2.difference(b2)
print(result3)

# set comprehensions

comp1 ={even+2 for even in range(2,11,2)}
print(comp1)



comp2 ={ch.lower() for ch in "SANDEEPKUMARRayala"}    # here it removes duplicate make it lower case too
print(comp2)
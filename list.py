#List

print(list("sandeep"))    #convert String into list

# in and not in operator can check cantains

listt= [1,2,3,5]
print(8 in listt)   # just like contain in the java it operates

print(6 not in listt)

# indexes and list slicing

index_lst=[[1,3,5],[3,56,0]]
index_lst2=["Deloitte","Sandeep"]
print(index_lst[0][2])
print(index_lst2[0][2])

# accessing the backward index by using the negative indexes

print(listt[-1]) # reverse negative

mixed = [False ,365,4.23,"this is the String"]

# slicing a list is similar to slicing a String

sliced =[1,3,4,5,6,7,7,2]
print(sliced[:4])
print(sliced[4:])
print(sliced[3:6])

#update the list
sliced[3]=22
print(sliced)


# del the index elements

del sliced[0]
print(sliced)


planets =["pluto","earth","mars","jupiter","jupiter"]
planets.remove("jupiter") # only first instance is removed
print(planets)

# delete index method .   remove based on the item

# append list

# planets.append("Sandeep")
# print(planets)


# insert
# planets.insert(0,"Sun")
planets.sort(reverse=False)
print(planets)

# AsciiBetical order
asciibetical =["Andy","Sandy","Apple","Brain"]

#asciibetical.sort(key= str.lower())            # not working please

print(asciibetical)

# .index()
print(asciibetical.index("Brain"))

# pop   pop method will removed the last item and assing to new variable
new_pop=asciibetical.pop()   # you can use the pop with index
print(asciibetical)
print(new_pop)













#create a dictionary

mapDic ={"name": "sandeep", "amazon": "alexa", "sony": "playstation"}

print(mapDic)

# reading values using key
print(mapDic["name"])

print(mapDic.keys())

# key exists in the dictionary

print("name" in mapDic)  # in and not in

print(mapDic.values())  # iterate to get the values


# items

print(mapDic.items())   #

for k,v in mapDic.items():
    print("k:"+k," v:"+v)


# .get()
print(mapDic.get("names","not found"))

# .fromkeys() it returns the dictionary using the two values

xmap = {}.fromkeys(["address",],"1422 kalyan nagar bangalore")
print(xmap)  # output : xmap = {}.fromkeys(["address",],"1422 kalyan nagar bangalore")

# if you use a  string in the itereable each unique char becomes a key  values repeat

xmap2 = {}.fromkeys("add","1422 kalyan nagar bangalore")
print(xmap2)

mapDic.pop("sony")
print(mapDic)


# pop item check popitem it doesn't take the names

sample_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "email": "alice@example.com",
    "is_employee": True,
    "department": "Engineering",
    "experience": 5,
    "skills": ["Python", "JavaScript", "SQL"],
    "manager": "Bob",
    "salary": 85000
}

print(sample_dict)  #{}

# copy method used to create a new copy dictionary
# clear
# update create a key value pair and update  if same key is there it override /
# if key name is new then the new key value pair will get appended

h ={"salary":197000}
sample_dict.update(h)
print(sample_dict)

# SetDefault method

person_info = {
    "full_name": "Alice Johnson",
    "years_old": 30,
    "location": "New York City"
}
# if "lastname" not in person_info:
#     person_info["lastname"] ="Rayala" #if last name is not present the adding
#
# print(person_info);


# set defualt method
person_info.setdefault("lastname","Rayala")
print(person_info)


# .dic() create a dic in python

empty = dict()  # empty dictionary

dict_with_value = dict(a=1, b_=2 ,c3=3)   # {'a': 1, 'b': 2, 'c': 3}
print(dict_with_value)


# tuples



# other way of coouple converts
tuple5 = tuple([3,33,6])
print(tuple5)  # it changed directly into the tuple (3, 33, 6)

tuple6 = tuple("Sandeep")
print(tuple6)  #('S', 'a', 'n', 'd', 'e', 'e', 'p')

# if you use dictionary inside the tuple only key converts as a tuple

tuple1 =tuple({"a":1,"b":2})
print(tuple1)   #('a', 'b')

numbers = (1, 2, 3, 4, 5)
print(numbers[0])  # accessing 1  index base
# slicing of tuples
print(numbers[:3])
print(numbers[1:4])
print(numbers[1:])
# numbers[0]=44; 'tuple' object does not support item assignment
# tuples are immutable data type

# tuples are less space in mememory immutable
print(numbers.__sizeof__())

# tuples looping and step

colors = ("red", "green", "blue")

count =0

while count< len(colors):
    print(colors[count])
    count+=1

# step in the tuples
ints  = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print(ints[::3])   # stride jumps 3
print(ints[1::2])   # even
print(ints[14::-1])   # backward from
print(ints[14::-2])    # backward even


# nested tuples
coordinates = ((10.0, 20.0), (30.0, 40.0))
print(coordinates[1][0])

# .index in tuples  it give the value index simple





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

numbers = (1, 2, 3, 4, 5)

# other way of
tuple5 = tuple([3,33,6])
print(tuple5)  # it changed directly into the tuple (3, 33, 6)

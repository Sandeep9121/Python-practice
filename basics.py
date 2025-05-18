import random

#Functions

def abcd():
    print("sandeep")
    print("is a good")
    print("salary 2Lpa")
    print(" nice time to have")

# calling the function
# abcd()
# abcd()
# abcd()

# 5 parts in the function    def functionname parantheis : and the code body



#function with parameters

def add_two_numbers(a,b):
    print(a+b)

add_two_numbers(2,4)


#deafults values in the functions
def def_value(a=1,b=0):
    print(a-b)


# def_value()             # used default
def_value(122-99)       #used customised


# using the return function
def def_value_return(a=1,b=0):
    return a-b

print(def_value_return())


# function exercise create a function and take the parameter 1 and print read a userinput name
#
# name =input(" Please enter your name \n")
# def printer_name(s):
#     return "Hello good afternoon :"+s
# # print(printer_name(name))


# write a fuction volume of retancular cube lbh using the user input l b h
#
# l =int(input("please enter the length of the cube \n l:"))
# b =int(input("please enter the breath of the cube \n b:"))
# h =int( input("please enter the height of the cube \n h:"))
#
# def volume_of_cube(k,q,c):
#     return k*q*c
#
# print("volume of the cube is :",volume_of_cube(l,b,h))

# module import , custom import and Universal import
print(random.randint(1,100))

# variable scope
# the variable created with the functions

def localscope():
    example="hi"
    return example

# print(example) # cannot be accessible because it is local only via function  destroyed when programs end

# local cannot used in global scope
# one local scope cannot be shared between the other function
# global scope can we used any where no matter what
# global scope variable can be accessed by multiple functions and used by others


# how to change a global variable using the function

fruit ="Apple "

def global_and_local():
    global fruit    # this stament changed brough the global variable  inside the function and modified it
   # fruit ="mango"
    return fruit

print(global_and_local())
print(fruit)

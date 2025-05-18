from basics import add_two_numbers
from random import randint;
from random import * # universal import
print("Sandeep is the developer")

var=5
print(var)
abc=3.003
high="Sandeep"
flag= True
print(type(high))
print(flag)

# Comments and Math operation

addition =4+5
substraction =9-1
division =7/2
multiplication =3*8
exponentiation =4**4
floor_division=16//5   # 3.2 but 0.2 is ignored
modulo = 7%3

# assign operation

ass=2
ass +=6
print(ass)


# order of operation
# () ** % / // and * + and -   just like a bodmass rule

expression = (9-7)*2**3+10%6//-1*2-1
print(expression)


print(11%3)

# floats
print(1.23+2.80) # approximate error 4.029999999999999  it is build on C

# how to fix below  -> use the round function

ex2 =(123+280)/100
print("fix",ex2)  #fix 4.03

print(round(1.23+2.80,2))  # round to the 2 decimal places

# a customer of grocery store purchase 6 items the name of the items as follows
# 1.penne 16 oz pack of 12 $16.68
# 2.pasta 24oz 6.98
# 3.cloves 16.78
# 4. 15.26



print( round(16.68+6.98+16.78+15.26,3))



#String

string ="sandeep ajnanaina"
string1 = 'sandeep is good '

print(string[0])  #accessing the index
print("sandeep"[5])

#stirng slicing

print("sandeep"[:3])   # starting
print(string1[2:5])   # start from 2nd index and end by 5
print(string1[5:])     # last 5  remove first 5
print(string[2:55])     # there is no out of bond exception

# string concatenation
concatenation = "Sandeep"+"-"+"kumar"
print(concatenation)
print(concatenation[1:44])   #not matter it is end is larger or not

s="Just do it!"
print(s[10:])   # 10:11 or 10:  exclude ! ->:10

# type or str function

print(type(s))
var =1
#print(str(var)+" snanioa")  # without str function ->unsupported operand type(s) for +: 'int' and 'str'


# escape character
# print("There\tis\ta\tlot\tof\tspace")
# # \n new line
# # put quotes in the String  \"
# print("sandeep\'s work \"")
# print("*******\n *****\n  ***\n   *")

# read the input from the usee

# name =input("please enter  your name \n")
# print(type(name))    # always treats as a String
# print("welcome "+name)

#casting for float & Int
x=123.55
# print(x)
# print(int(x))

c="135"
# c="124a"  # error -> ValueError: invalid literal for int() with base 10: '135a'
print(int(c))
#similar with float

f ="123.55890088884888"  # String doesn't give garbage value like before
print(float(f))

# function is being imported using -> from basic import add_two_number
add_two_numbers(22,9999)
add_two_numbers(22,randint(1,700))
# import inside one more random import used that functon for pass the second variable














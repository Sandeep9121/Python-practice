all_low= "sandeep is GGG good boy"
# print(all_low.upper())
# print(all_low.lower().islower())

# isUpper or islower is to check the return the boolean value

# multiple string methods

# isaphla , isalnum , isdecimal , isspace()  istitle()

# .startswith() .endswith()

c="sandeep"
# join
print("".join([all_low,c]))  # single join  why  separator.join([string1,String2])

#Split method

#print("Eggs, Milk , Walffles ".split())  # ['Eggs,', 'Milk', ',', 'Walffles']

# print("Eggs,Milk,Walffles".split(","))   # comma are removed here , acts as separator




# String method 2

# .rjust() and .Ijust
# -> adjust any with the given string length if less add spaces to it ,
# you can fill that spaces using other character by providing the space

print("sandeep".rjust(24))
print("sandeep".ljust(12,"*"))  #sandeep*****

#.center()

print("India".center(12,"*")) #***India****

# .strip() .rstrip()  and .lstrip() and replace()

# Strip removes all of the spaces and whitespace from both sides of the string
# rStrip remove rightside spaces
#lstrip removes leftside of a string

print("i am good".strip("d"))
print("i am good".strip("d").replace(" ","")) # replace the string

print(len("sandeep"))

# reverse the string
# st= "i am sandeep kumar rayala"
# counter=len(st)
# result =""
# while counter>0:
#     result+=st[counter-1]
#     counter=counter-1
#
# print(result)

# using for and range reverse the string

# inputString = input("please enter the String \n")
# reversed = ""
# for i in range(len(inputString)-1,-1,-1) :
#        reversed +=inputString[i]
#
# print(reversed) # normal reverse

# word counter

st= "i am sandeep kumar rayala"
counter=len(st.split())
print("the counter is",counter)
arrayString =st.split()
rev2 = ""
for i in  range(0,len(arrayString)):
    subString=arrayString[i]
    for j in range(len(subString)-1,-1,-1):
        rev2+=subString[j]
    rev2+=" "
print(rev2)  # i ma peednas ramuk alayar     -> reverse the each word


#.format()  to run the print statement

s1="sandeep"
s2="technical"
s3="java developer"

print("what is name{} department {} role {}".format(s1,s2,s3))







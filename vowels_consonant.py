import string
x=input()
x=x.lower()
v=('a','e','i','o','o')
if (x not in string.ascii_lowercase):
    print("invalid")
elif(x in v):
    print("Vowel")
else:
    print("Consonant")

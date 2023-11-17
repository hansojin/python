#!/usr/bin/env python

word= input()
word=word.replace(":-)",'$').replace(":-(","#")
a=word.count("$")
b=word.count("#")
if a>b:
    print("happy")
elif a<b:
    print("sad")
elif a==b==0:
    print("none")
else:
    print("unsure")



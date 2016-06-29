'''
Created on 29.06.2016

@author: Zmote
'''
x = 2
print x == 2
print x == 3
print x < 3

name = "John";
age = 23
if name == "John" and age == 23:
    print "Your name is John, and you are also 23 years old";
if name == "John" or name == "Rick":
    print "Your name is either John or Rick.";

if name in ["John", "Rick"]:
    print "Your name is either John or Rick";
    
# if, elif, else, like if, else if und else in anderen Sprachen

x = 23
if x == 2:
    print "x equals two!";
else:
    print "x does not equal to two";
    
x = [1,2,3]
y = [1,2,3]

print x == y # variables check
print x is y # no match of variables, but instances

print not False
print (not False) == (False)
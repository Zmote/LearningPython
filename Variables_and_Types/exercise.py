'''
Created on 28.06.2016

@author: Zmote
'''

'''
basic types
'''
myint = 7;
myfloat1 = 7.0;
myfloat2 = float(7);
mystring1 = 'hello';
mystring2 = "hello";
mystring3 = "Don't worry about appostrophes lal";

print "All: " + str(myint) + " " + str(myfloat1) + " " + str(myfloat2) + " " + mystring1 + " " + mystring2 + " " + mystring3;


'''
Lists
'''

mylist = [];
mylist.append(1);
mylist.append(2);
mylist.append(3);

print(mylist[0]); # prints 1
print(mylist[1]); # prints 2
print(mylist[2]); # prints 3

for x in mylist:
    print x,;
print;
mylist2 = [1,2,3,4,5,6,7];

for y in mylist2:
    print y,;
    
'''
Basic operators
'''
    
number = 1 + 2 * 3 / 4.0;

print;

print number;

remainder = 11 % 3;

print remainder;

squared = 7 ** 2;
cubed = 3 ** 4;

print squared;
print cubed;

helloworld = "hello" + " " + "world";
print helloworld;

lotsofhellos = "hello" * 10;
print lotsofhellos;

'''
List operators
'''
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7] # interesting, no semicolon needed apparently if on separate line
all_numbers = odd_numbers + even_numbers;
print all_numbers;

print [1,2,3] * 3;




















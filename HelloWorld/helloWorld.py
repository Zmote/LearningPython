'''
Created on 28.06.2016

@author: Zmote
'''
print "Hello World";
x = 1;
y = 2;
z = x + y;

'direct concatenation not possible'
print "x: " + str(x) + " and y: " + str(y) + " equals: z: " + str(z);

if z == 1:
    print "I entered conditional subtree";
elif z == 3:
    print "Elif has taken up the cause!";
else:
    print "Zafer is awesome, else subtree entered";
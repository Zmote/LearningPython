'''
Created on 29.06.2016

@author: Zmote
'''

primes = [2,3,5,7]

for prime in primes:
    print prime,;
print;

for x in xrange(5):
    print x,;
print;

for x in xrange(3,6):
    print x,;
print;

for x in xrange(3,8,2):
    print x,;
print;

count = 0
while count < 5:
    print count,;
    count += 1;
print;

countme = 0;

while True:
    print countme,
    countme += 1
    if countme >= 5:
        break
print
for x in xrange(10):
    if x % 2 == 0:
        continue
    print x,
print

me = 0
while me < 5:
    print me,
    me += 1
else:
    print
    print "Count value reached %d" %(me)
    
def my_function():
    print "Hello from my Function!";
    
my_function();

def add(first,second):
    result = first + second
    print str(result)

add(1,4);

def multiplication(first,second):
    return first * second

print multiplication(3, 5);





























'''
Created on 29.06.2016

@author: Zmote
'''
def do_stuff_with_number(n):
    print n
    
the_list = (1,2,3,4,5)

for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError:
        do_stuff_with_number(0)
        
'''
Sets
'''

print set("my name is Zafer and Zafer is my name".split())

a = set(["Jake", "John", "Eric"])
b = set(["John","Jill"])

A = set(a)
B = set(b)
C = A.union(B)

print A.difference(B)
print C

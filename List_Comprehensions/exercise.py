'''
Created on 29.06.2016

@author: Zmote
'''
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []

for word in words:
    if word != "the":
        word_lengths.append(len(word));

print words
print word_lengths

def myfunction(first,second,third, *therest):
    print "First: %s" % first
    print "Second: %s" % second
    print "Third: %s" % third
    print "And all the rest... %s" % list(therest)

myfunction("Zafer", "Niyazai", "Nazair", "Mario", "Luigi")

def bar(first,second,third,**options):
    if options.get("action") == "sum":
        print "The sum is: %d" % (first + second + third)
    
    if options.get("number") == "first":
        return first
result = bar(1,2,3, action = "sum", number = "first")
print "Result: %d" % result
'''
Created on 29.06.2016

@author: Zmote
'''
class MyClass:
    variable = "blah"
    
    def function(self):
        print "This is a message inside the class"

myobject = MyClass();
myobject.function()

print myobject.variable

phonebook = {}
phonebook["Zafer"] = 786069811
phonebook["Niyazi"] = 769992211

print phonebook["Zafer"]

phonebook1 = {
     "Ayse" : 555,
     "Ayfer" : 222,
     "Lol" : 234
}

print phonebook1["Ayse"]

for name, number in phonebook1.iteritems():
    print "Phone number of %s is %d" % (name,number)
    
del phonebook["Zafer"]
phonebook.pop("Niyazi")




















'''
Created on 30.06.2016

@author: Zmote
'''
import json
import cPickle

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json) # like JSON.parse
    salaries[name] = salary

    return json.dumps(salaries) # like JSON.stringify

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print decoded_salaries["Alfred"]
print decoded_salaries["Jane"]
print decoded_salaries["Me"]

phonebook = '{"Zafer" : 786069811, "Niyazi": 772883243}'
decoded_phonebook = json.loads(phonebook)

print decoded_phonebook["Zafer"]

pickled_string = cPickle.dumps([1,2,3,"a","b","c"])
print cPickle.loads(pickled_string)
# Intro to dictionaries

course = {} #Empty Dictionary

courses = {'key':'value'} # All Keys must be unique. If not, then data is overwritten

courses = {'CSI-160':'Intro To Python','CSI-260':'adv.Python', 'CSI-300':'Integer data'}

print(courses)
print(courses.keys())
print(courses.values())

# Using a loop to extract keys
for keys in courses.keys():
    print(keys)

# Using a loop to extract values
for values in courses.values():
    print(values)

for key,value in courses.items():
    print("The key is", key, "and the value is", value)

# A valid dictionary structure that includes a list
grades = {'course':'CIS-160-01: Intro to Python','Students':['John','Mary'],'x':3}

for i in courses: # The default behavior of the interpreter is to search for keys
    if i == 'CSI-300':
        print("The course exists.", i)
    else:
        print("The key does not exist")


for j in courses.values(): # Have to specify
    if j == 'Integer data':
        print("The course exists.", j)
    else:
        print("The value does not exist")


def addToDictionary():
    for keys,values in courses.items():
        k = input("Key: ")
        v = input("Value: ")
        if k == 'CSI-160' and v == 'Intro to Python':
            print("The course exists.", k, v)
        else:
            print("The course does not exist")

# working with courses = {'CSI-160':'Intro To Python','CSI-260':'adv.Python', 'CSI-300':'Integer data'}

print(courses)
courses.update({'CSI-400':'A great course'}) #adds a dictionary item to the dictionary
print(courses)
courses.update({'CSI-400':'Software Engineering'}) # This updates the value of a key
print(courses)
courses['CSI-420'] = 'More Engineering' # adds the key and its value into a dictionary
print(courses)
courses['CSI-260'] = 'Advanced Python'
print(courses)
# Adding and is easy, but making a mistake can lead to this and screwing up the list
courses['CSI-2600'] = 'Advanced Python'
print(courses)

del courses['CSI-2600'] # Deletes the entire item (keys and values) - It's gone FOREVER
print(courses)
key = input("Enter the key do delete: ") # To get the key instead of the value
item = courses.pop(key) # This will let you store a value, not a key, in a variable
print(item)
print(courses)
print(key)
print(item)

# Restoring deleted data, provided you have already properly saved it
courses[key] = item
print(courses)

print(dict(sorted(courses.items()))) # sorts the dictionary by key

print(dict(sorted(courses.items(), key=lambda item: item[1]))) # sorts the dictionary by values
addToDictionary()

def addToDiction():
    for keys,values in courses.items():
        k = input("Key: ")
        v = input("Value: ")
        if k == 'CSI-160' and v == 'Intro to Python':
            print("The course exists.", k, v)
        else:
            print("The course does not exist")
            
addToDiction()

from os.path import exists

file = 'myfile.txt'
data = input("Enter your data here: ")
file_exists = exists(file) # Returns a True if exists, False if it doesn't
# print(file_exists)

if file_exists == False:
    with open(file, 'w') as f: # if it's not there, write it
        print("The file does not exist, but it will be created now")
        f.write('\n' + data)
else:
    with open(file, 'a') as f: #if it is there, append it
        print("The data has been appended to the file")
        f.write('\n' + data)

with open(file, 'r') as f:
    content = f.read()
    print(content)







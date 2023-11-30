# Permanent saving of any data

"""
Three key functions to manage I/O (input/output):

Write - writes data to a file (CAN EASILY OVERWRITE DATA IN A FILE)
Read - reads the data in a file
Append - updates data in a file (Prevents data from being overwritten)

If the file does not exist, using "write" will automatically create the file

Programmers need to work with the file handlers to open, close and process data with files
"""
'''
f = open('test.txt', 'w') # creates a new file, an open file, on the server
print(f.name)
print(f.mode)
f.close()
'''
'''
# Context Manager - it will automatically close the file at the end of the process
with open('test.txt', 'w') as f: #the 'f' is a file handler - holds the file name and action
    content = input("Enter data for the file: ")
    f.write(content)
'''
'''
with open('test.txt', 'a') as f: # a as append
    content = input("Enter new data: ")
    f.write('\n' + content)
'''
'''
with open('test.txt', 'r') as f:
    content = f.read()
    print(content)

with open('test.txt', 'r') as f:
    content = f.read(5) # This method takes a parameter to limit the output (num of characters)
    print(content)
'''
'''
with open('test.txt', 'r') as f:
    max = 10 # limits the number of characters to output from the file
    f.seek(0) # sets the cursor at the beginning og the file
    contents = f.read(max)
    while len(contents) > 0: # grab the data, 10 characters, output those characters, stop then reset and grab ten again
        print(contents, end='*')
        t =f.tell() # Identify the current position of the cursor
        print(t)
        contents = f.read(max) # this sets the loop to run the next 10 characters
'''
'''
f.tell() - identifies the position of the cursor in the file
f.seek() - this sets the position of the cursor in a file 
'''

with open('test.txt', 'r') as fp: # fp as file handler (file process) can be anything though
    contents = fp.readlines() # readlines is the more functional way to get the data out
    # print(contents[1:3][0]) # [0] gets rid of the list brackets
    contents_final = contents[1:3]
    for i in contents_final:
        print(i)

# Working with Lab 5, some tips about lab 5
# Worked on this in class
"""
The section below goes into the if, else procedure to find the correct slice of the URL if find is not working
"""
url = "http://www.champlain.edu/course"
def domain_name_extractor(url):
    # Assumption: the protocol is http://
    protocol = url[0:7]
    if(protocol == "https:/"):
        domain = url[8:]
        pos = domain.index("/")
        print(domain[0:pos])
    elif(protocol == "http://"):
        domain = url[7:]
        pos = domain.index("/")
        print(domain[0:pos])
"""
This section bellow goes into the find procedure to find the correct slice of the URL 
"""
y = url.find('w')
domain = url[y:]  # www.champlain.edu/course
z = domain.find('/')  # Find the '/'
                        # Finds the '/' and passes it to the variables 'z'

print(domain[0:z])  # The 'domain' variable holds: www.champlain.edu/course.
                        # Start the slice at zero. The end of the slice is up to but **Do Not Include** the '/'
                        # Its index position is held in the varible 'z'

pass

print()
domain_name_extractor(url)





def hello():
    print('hello')
    print('howdy')

hello()
hello()

def hello2(name):
    print("The name is " + name + " and has " + str(len(name)) + 'letters')
    # the str is for string concantination(can't + to string without str)

#trick for print
print('Hello', end='')# dosen't add the endline for the print
print('World') 

print('stuff', 'stuff', 'stuff')
print('stuff', 'stuff', 'stuff', sep='ABC')#instead of spaces, it is ABC
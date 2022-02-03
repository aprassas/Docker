import project


print ("running test")

var = project.my_function2(True)
assert(var == True)

var = project.my_function2(False)
assert(var == False)
print('passed the test')


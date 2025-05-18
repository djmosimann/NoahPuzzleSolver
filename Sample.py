# Lines starting with a '#' symbol are comments

# This is a variable we can use in the program
name = "Noah"

# This is a function we can call. It takes 1 argument, the name
def doSomething(n):
    print("Hello " + n + "!")


# Any statements here will be executed when the program is run
# We're just going to call the doSomething() function a couple of times
doSomething(name)
doSomething("David")
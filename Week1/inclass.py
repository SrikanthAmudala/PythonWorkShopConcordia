# append, extend, return multi values from a function

# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))

# nested for loop
for i in range(1, 5):
    for j in range(i):
        print(i)
    print()

# Prints all letters except 'e' and 's'
for letter in 'concordia':
    if letter == 'c' or letter == 'i':
        continue
    print('Current Letter :', letter)

for letter in 'concordia':

    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'c' or letter == 'i':
        break

print('Current Letter :', letter)

# An empty loop
for letter in 'concordia':
    pass
print('Last Letter :', letter)

"""
Generator-Function : A generator-function is defined like a normal function, 
but whenever it needs to generate a value, 
it does so with the yield keyword rather than return. 

If the body of a def contains yield, the function automatically becomes a generator function.
"""
# defining fuctions

# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


# Example
def nextSquare():
    i = 1;

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point


# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)

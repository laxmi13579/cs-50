# default print function syntax
# print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)


# objects, can take any number of objects as input. 
#  sep=' ', [seprator] . we can add any number of arguments it apply one single blank
#  end='\n',  it will close with paraethesis and start with new line.


# he program with user input and variables


name = input("what is your name? ")

# override end of print function
print("hello", end=" ")
print(name)

print("hello", end="--")
print(name)

# override sep of print function
print('Hello', name, sep="**")

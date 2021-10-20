# Python Functions


def function_name(parameters):
	"""docstring"""
	statement(s)





    def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")




    # How to call a function in python?
#     def greet(name):
#     # """
#     # This function greets to
#     # the person passed in as
#     # a parameter
#     # """
#     print("Hello, " + name + ". Good morning!")

# greet('Paul')


# How to call a function in python?
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))



# Scope and Lifetime of variables
def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)





# Types of Functions
# Basically, we can divide functions into the following two types:

# Built-in functions - Functions that are built into Python.
# User-defined functions - Functions defined by the users themselves.
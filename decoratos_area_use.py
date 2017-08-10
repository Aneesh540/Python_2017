""" Area where decorators shine
We have seen in decorators.py that function.__name__ becomes wrapTheFunction
This could change docstring of function but python has a easy way to overcome this
"""

from functools import wraps


def newDecorator(function):

    @wraps(function)
    def wrapTheFunction():
        print("Xecute b4 function == {}".format(function.__name__))
        function()
        print("Xecute after function == {}".format(function.__name__))

    return wrapTheFunction

@newDecorator
def myFunctionForTestingWraps():
    print("TESTING @wraps")
    print("name == {}".format(myFunctionForTestingWraps.__name__))

myFunctionForTestingWraps()

# BUG BUG BUG BUG BUG BUG BUG BUG BUG
def logit(function):

    # @wraps
    def withLogging(*args, **kwargs):
        print(function.__name__ + "was called")
        return function(*args, **kwargs)

    return withLogging

@logit
def addition(x):
    return x + x

print(addition(3,4,5))

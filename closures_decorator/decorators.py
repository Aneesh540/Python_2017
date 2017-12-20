""" DECOORATORS """

# WRITING FIRST DECORATOR

def newDecorator(function):

    def wrapTheFunction():
        print("I'am xecuting b4 function=={}".format(function.__name__))

        function()

        print("xecuting after function=={}".format(function.__name__))

    return wrapTheFunction

def functionRequiredForDecoration():
    print("PLEASE DECORATE MEEE!!!")


@newDecorator
def alsoDecorateMe():
    print("Decorate me, and remove my foul smell!!")

if __name__ == "__main__":

    functionRequiredForDecoration = newDecorator(functionRequiredForDecoration)
    print(functionRequiredForDecoration)
    functionRequiredForDecoration()

    print("\n\n")
    alsoDecorateMe()
    print("WTF:: name of alsoDecorateMe == {}".format(alsoDecorateMe.__name__))
    
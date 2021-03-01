# Chapter # 13
#13.6.1 - 13.6.3
def getIntFromUser(message, errormessage):
    userinput = None
    while userinput == None:
        userinput = input(message)
        
        try:
            userinput = int(userinput)
        except ValueError:
            print(errormessage)
            userinput = None
        else:
            return userinput

def userDivideNum():
    while True:
        try:
            answer = int(input("Enter numerator: "))/int(input("Enter denominator: "))
        except ValueError:
            print("Please enter numbers")
        except ZeroDivisionError:
            print("Error: div by zero")
        finally:
            print(answer)
            return ()
    
#13.6.5
def openafile(filename, readorwrite):
    try:
        file = open(filename, readorwrite)
    except FileNotFoundError:
        print("Error, file does not exist")
        return
    return file


#test code ------------------

#Call code 13.6.1-13.6.3
# integer = getIntFromUser("Enter an int: ", "Try Again")
# print(integer)

# userDivideNum()

#Call code 13.6.5
# file = openafile("doesntexist.txt", "r")

# file = openafile("doesexist.txt", "r")
# print(file)
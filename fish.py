def main():
    #This line of code is where I call try
    try:
        print(input(": "))
    except KeyboardInterrupt:
        print("So long, and thanks for all the fish")


def maths(a, b): 
    divs = a / b
    return print("THIS IS THE NEW VALUE ", int(divs))


maths(8,2)



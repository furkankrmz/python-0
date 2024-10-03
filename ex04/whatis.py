import sys

count = len(sys.argv)
#print("number of arguments: ", count)
if  count == 2:
    if sys.argv[1].lstrip("-+").isdigit():
        tmp = int(sys.argv[1])
        if tmp % 2 == 0 :
            print("I'm Even.")

        else:
            print("I'm Odd.")
    else:
        print("AssertionError: argument is not an integer")

else:
    if(count == 1):
        print("")
    else:
        print("AssertionError: more than one argument is provided")


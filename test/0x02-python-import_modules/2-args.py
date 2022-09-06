#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number_of_arguments = len(argv)

    if number_of_arguments == 1:
        print("{} arguments.".format(0))
    elif number_of_arguments == 2:
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(number_of_arguments - 1))

    if number_of_arguments > 1:
        for i in range(1, number_of_arguments):
            print("{}: {}".format(i, argv[i]))

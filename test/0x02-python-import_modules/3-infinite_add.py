#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum_of_argument = 0
    number_of_arguments = len(argv)

    for i in range(1, number_of_arguments):
        sum_of_argument += int(argv[i])

    print(sum_of_argument)

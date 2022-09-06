# :book: 0x03. Python - Data Structures: Lists, Tuples

# :computer: Tasks
## [0-print_list_integer.py](0-print_list_integer.py)
Write a function that prints all integers of a list.
 - Prototype: def print_list_integer(my_list=[]):
 - Format: one integer per line. See example
 - You are not allowed to import any module
 - You can assume that the list only contains integers
 - You are not allowed to cast integers into strings
 - You have to use str.format() to print integers

```
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$
```

> pycodestyle 0-main.py; chmod +x 0-main.py; ./0-main.py


## [1-element_at.py](1-element_at.py)
Write a function that retrieves an element from a list like in C.
 - Prototype: def element_at(my_list, idx):
 - If idx is negative, the function should return None
 - If idx is out of range (> of number of element in my_list), the function should return None
 - You are not allowed to import any module
 - You are not allowed to use try/except

```
guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$ 
```

> pycodestyle 1-main.py; chmod +x 1-main.py; ./1-main.py

## [2-replace_in_list.py](2-replace_in_list.py)
Write a function that replaces an element of a list at a specific position (like in C).
 - Prototype: def replace_in_list(my_list, idx, element):
 - If idx is negative, the function should not modify anything, and returns the original list
 - If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
 - You are not allowed to import any module
 - You are not allowed to use try/except

> pycodestyle 2-replace_in_list.py; chmod +x 2-main.py; ./2-main.py

## [3-print_reversed_list_integer.py](3-print_reversed_list_integer.py)
Write a function that prints all integers of a list, in reverse order.
 - Prototype: def print_reversed_list_integer(my_list=[]):
 - Format: one integer per line. See example
 - You are not allowed to import any module
 - You can assume that the list only contains integers
 - You are not allowed to cast integers into strings
 - You have to use str.format() to print integers

```
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$
```
> pycodestyle 3-print_reversed_list_integer.py; chmod +x 3-main.py; ./3-main.py

## [4-new_in_list.py](4-new_in_list.py)
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
 - Prototype: def new_in_list(my_list, idx, element):
 - If idx is negative, the function should return a copy of the original list
 - If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
 - You are not allowed to import any module
 - You are not allowed to use try/except

```
guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 
```

> pycodestyle 4-new_in_list.py; chmod +x 4-main.py; ./4-main.py


## [5-no_c.py](5-no_c.py)
Write a function that removes all characters c and C from a string.
 - Prototype: def no_c(my_string):
 - The function should return the new string
 - You are not allowed to import any module
 - You are not allowed to use str.replace()

```
guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$ 
```

> pycodestyle 5-no_c.py; chmod +x 5-main.py; ./5-main.py

## [6-print_matrix_integer.py](6-print_matrix_integer.py)
Write a function that prints a matrix of integers.
 - Prototype: def print_matrix_integer(matrix=[[]]):
 - Format: see example
 - You are not allowed to import any module
 - You can assume that the list only contains integers
 - You are not allowed to cast integers into strings
 - You have to use str.format() to print integers

```
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
```
> pycodestyle 6-print_matrix_integer.py; chmod +x 6-main.py; ./6-main.py

## [7-add_tuple.py](7-add_tuple.py)
Write a function that adds 2 tuples.
 - Prototype: def add_tuple(tuple_a=(), tuple_b=()):
 - Returns a tuple with 2 integers:
     - The first element should be the addition of the first element of each argument
     - The second element should be the addition of the second element of each argument
 - You are not allowed to import any module
 - You can assume that the two tuples will only contain integers
 - If a tuple is smaller than 2, use the value 0 for each missing integer
 - If a tuple is bigger than 2, use only the first 2 integers
```
guillaume@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$ 
```

> pycodestyle 7-add_tuple.py; chmod +x 7-main.py; ./7-main.py

[8-multiple_returns.py](8-multiple_returns.py)
Write a function that returns a tuple with the length of a string and its first character.
 - Prototype: def multiple_returns(sentence):
 - If the sentence is empty, the first character should be equal to None
 - You are not allowed to import any module

```
guillaume@ubuntu:~/0x03$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/0x03$ 

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x03-python-data_structures
    File: 8-multiple_returns.py
```

> pycodestyle 8-multiple_returns.py; chmod +x 8-main.py; ./8-main.py

## References
 1. [https://docs.python.org/3/tutorial/introduction.html#strings](An Informal Introduction to Python)
 2. [https://docs.python.org/3/tutorial/modules.html](Modules)
 3. [https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments](Command Line Arguments)


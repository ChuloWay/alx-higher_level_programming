# doctest_simple.py

## Check format style using pycodestyle
pycodestyle doctest_simple.py; 

## Provide executable permission to file
chmod +x doctest_simple.py;

## Run file
./doctest_simple.py

or 

python3 doctest_simple.py

pycodestyle doctest_simple.py; chmod +x doctest_simple.py; ./doctest_simple.py

## internal Tests
### Run internal tests
python3 -m doctest -v doctest_simple.py

## External tests
Write test in tex file

### Run tests using th command
python3 -m doctest -v doctest_simple_external_test.txt

## doctest_testmod_mod.py
Running run doctest against the source

### Check python script, provide permissions and run
pycodestyle doctest_testmod_mod.py; chmod +x doctest_testmod_mod.py; ./doctest_testmod_mod.py

### Run tests
python3 doctest_testmod_mod.py -v

## Running tests from within modules using testmod() and testfile()
## Run test in this module
```
if __name__ == '__main__':
    import doctest
    doctest.testmod()

```

### Run tests in another module
```
#import doctest_simple

if __name__ == '__main__':
    import doctest
    doctest.testmod(doctest_simple)

```

### Runf from file
```
#doctest_testfile.py

import doctest

if __name__ == '__main__':
    doctest.testfile('doctest_in_help.txt')

```
# Test
we can test our code using three functions in order to check our program. The tests can be found in the folder named ```tests/test_csv/```, we use this module to test the correct creation of csv file. You can repeat the tests running the code: ```python3 -m unittest -v -b tests/test_csv.py```. The output you receive is the following: 
```
$ python3 -m unittest -v -b tests/test_csv.py
test_empty_datafile (tests.test_csv.TestMain)
Check the presence of data inside the csv file. ... ok
test_no_datafile (tests.test_csv.TestMain)
Check if there is a csv file. ... ok
test_valid_extension (tests.test_csv.TestMain)
Check the extension of the file. ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

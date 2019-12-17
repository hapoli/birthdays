# Find famous people birthdays!

In our repository the first file you find is called ```main.py``` which returns the birthdays of several well-known people given a valid input. 
To be able to run the code, you need to insert your credentials (username and password). In the following steps we will show how to do it!

## How to:
Insert the name/s of the famous person you want to know the birthday of and your right credentials. This is the outcome you will receive:

```
$ python3 main.py 'Albert Einstein' 'Alan Turing' -c username -p password -vv
User is present, password is valid
Albert Einstein was born the  03/14/1879
Sorry, Alan Turing is not in the list, 
We know the birthdays of these people:
Donald Trump
Rowan Atkinson
Albert Einstein
Ada Lovelace
Benjamin Franklin
```

In the case of incorrect credentials, the program will return that either the password or the username is invalid.

## How to populate the database:
If you want to only access the database, because you are already registered, you can run the ```main.py``` only. Instead, if you are registering for the first time you have to use the ```dbmanager.py``` in which you can find some useful instructions.

## Add a new user:
To add a new user into the database, these are the arguments you need to insert in ```dbmanager.py``` file:
* -h, --help: tells you the possible arguments you can insert
* -a: username
* -p: password

```
$ python dbmanager.py -a username -p password
Username username successfully added
```

## Check the validity:
To check if your credentials are valid, please insert in ```dbmanager.py```:
* -h, --help: tells you the possible arguments you can insert
* -c: username
* -p: password

```
$ python dbmanager.py -c username -p password
User is present, password is valid
```

## Let’s now use the application!
Now that you have completed your registration or access process, you can find out the birthdays of famous people present in the ```birth.csv``` file contained in ```birth_package```.
The database contains this information:

|Name and Surname | Birthday |
|-----------------|----------|
|Albert Einstein  |03/14/1879|
Benjamin Franklin |01/17/1706|
Rowan Atkinson    |01/06/1955|
Ada Lovelace      |12/10/1815|
Donald Trump      |06/14/1946|

If you insert a name that is not found in the database, the program returns the following statement:

```
$ python main.py 'Alan Turing' -c username -p password
User is present, password is valid
Sorry, Alan Turing is not in the list, 
We know the birthdays of these people:
Rowan Atkinson
Ada Lovelace
Benjamin Franklin
Albert Einstein
Donald Trump
```

### Verbosity:
You can view your output in three different ways according to the number of **-v** you put:
* *-v*: shows only the name and the birthday.
```Albert Einstein : 03/14/1879```
* *-vv* or more: returns a complete sentence.
```Albert Einstein was born the 03/14/1879``` 

> **Note:** If you don't put any *-v*, you will get only the date of the birthday. ```03/14/1879```

## PEP-8 and PEP-257:
All the python modules used the standard rules of PEP-8 and PEP-257 for codes and dostrings to make the code documentable and consistent.

## Test:
We can test our code using three functions in order to check our program. The tests can be found in the folder named ```tests/test_csv/```, we use this module to test the correct creation of csv file. You can repeat the tests running the code: ```python3 -m unittest -v -b tests/test_csv.py```. The output you receive is the following: 

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

## Authors:
We are the GAS GAS group:

* Basaglia Giulia 
* Benetti Sofia
* Poli Anna

## License:
GNU GENERAL PUBLIC LICENSE


## Credits:
Code is taken from the nice [practice Python](https://www.practicepython.org/) website from Michele Pratusevich and is released with a [CC-BY](https://www.practicepython.org/about/) license.

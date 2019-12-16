# Find famous people birthdays!

In our repository the first file you find is called “main.py” which returns the birthdays of several well-known people given a valid input. To do so, you need to insert your credentials (username and password) and the “dbmanager” file, contained in folder “scripts”, will check their validity. 

More in depth:
If you insert the name of the famous person you want to know the birthday of and your right credentials, this is the outcome you should receive:

```
$ python main.py 'Albert Einstein' -c username -p password
User is present, password is valid
03/14/1879
```

In the case of incorrect credentials, the program will return that either the password or the username is invalid.

## How to populate the database
If you want to only access the database, because you are already registered, you can run the “main.py” only. Instead, if you are registering for the first time you have to use the “dbmanager.py” in which you can find some useful instructions.

## Add a new user:
To add a new user into the database, these are the arguments you need to insert in “dbmanager” file:
-a: username
-p: password

## Check the validity:
To check if your credentials are valid, please insert in “main.py”:
-c: username
-p: password

## Let’s now use the application!
Now that you have completed your registration or access process, you can find out the birthdays of famous people present in the “birth.csv” file contained in “birth_package”.
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
$ python main.py "prova" -c username -p password
User is present, password is valid
Sorry, prova is not in the list, 
We know the birthdays of these people:
Rowan Atkinson
Ada Lovelace
Benjamin Franklin
Albert Einstein
Donald Trump
```

## PEP-8

All the python modules used the standard rules of PEP-8 and PEP-257 for codes and dostrings to make the code documentable and consistent.

## Database

|Name and Surname | Birthday |
|-----------------|----------|
|Albert Einstein  |03/14/1879|
Benjamin Franklin |01/17/1706|
Rowan Atkinson    |01/06/1955|
Ada Lovelace      |12/10/1815|
Donald Trump      |06/14/1946|
## Authors

We are the GAS GAS group:

* Basaglia Giulia 
* Benetti Sofia
* Poli Anna

## License

GNU GENERAL PUBLIC LICENSE


## Credits:

Code is taken from the nice [practice Python](https://www.practicepython.org/) website from Michele Pratusevich and is released with a [CC-BY](https://www.practicepython.org/about/) license.

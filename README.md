# Permuter

Permuter is a tool written in python that allows you to create a passwords lists based on personal data about a person, like the name, born date, id, pet name, any data that can be used to create a password permuting these data to generate a password list. This, like any password maker for BruteForce, may fail. So be smart and patient :).

### How to use?

To use this tool you only need to have data about a person, and then follow the next steps.

### Install

```
$ git clone https://github.com/Grillet0xEB/permuter.git
$ cd permuter
$ pip install -r requirements.txt
```
### Usage
```
Usage: pyhton permuter.py [data 1] [data 2] [data 3] [data 4]... [data n]

 ______                                           
(_____ \                          _               
 _____) )____  ____ ____  _   _ _| |_ _____  ____ 
|  ____/ ___ |/ ___)    \| | | (_   _) ___ |/ ___)
| |    | ____| |   | | | | |_| | | |_| ____| |    
|_|    |_____)_|   |_|_|_|____/   \__)_____)_|    
                                                  

		Carlos Grillet
		Version 0.1


[?]Add special chars[ - _ . ! ][y/n]:
[?]Generate only passwords greater than 8 chars?[y/n]:

[+]Num of items to be permuted: n
[+]Num of possible permutations: p

[!]Creating file of passwords
[!]File locate in: ~/permuter/passw.txt
[!]Writing...

[!]File save successfully
```

### Example:
```
pyhton permuter.py Carlos Grillet C G 07 1996 Ren       The order doesn't matter
pyhton permuter.py --help                               Show the help banner 
```

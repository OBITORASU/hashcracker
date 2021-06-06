# hashcracker is a hash cracking script made in Python

`hashcracker` is a terminal based python script which uses a dictionary attack on supported hashing algorithms to crack the provided hashes. Currently `hashcracker` supports some of the most common algorithms a penetration tester might encounter during a pentest, namely `sha1, sha224, sha256, sha384, sha512 and md5`. ```hashcracker``` is implemented using ```hashlib``` in Python.

## Prerequisites:
- `python 3`
- `a good wordlist`

## Installation:
Step 1:
```
git clone https://github.com/OBITORASU/hashcracker.git
```
Step 2:
```
cd hashcracker
```
Step 3:
```
python3 hascracker.py -H hash -t hash_type -w path_to_wordlist
```

## Usage:
```
usage: hashcracker.py [-h] -H  -t  -w

Hashcracker is a quick script that cracks common hashes using Python.

optional arguments:
  -h, --help        show this help message and exit
  -H , --hash       Your hash
  -t , --type       Type of your hash supported hashes [sha1, sha224, sha256, sha384, sha512, md5]
  -w , --wordlist   Path to your wordlist
```

Use the script with `-h` or `--help` flag to see it's usage.

---
**NOTE**

I have not provided any wordlist with my code so you will have to find a good wordlist yourself to get cracking.

---

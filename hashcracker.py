import hashlib
import sys
import os
import argparse

# Set colours for better visuals
red = "\033[91m"
green = "\033[92m"    
reset = "\033[0m"

parser = argparse.ArgumentParser(description="Hashcracker is a quick script that cracks common hashes using Python.")
parser.add_argument("-H", "--hash", type=str, metavar="", required=True, help="Your hash")
parser.add_argument("-t", "--type", type=str, metavar="", required=True, help="Type of your hash supported hashes [sha1, sha224, sha256, sha384, sha512, md5]")
parser.add_argument("-w", "--wordlist", type=str, metavar="", required=True, help="Path to your wordlist")
args = parser.parse_args()

# Define banner
banner = """%s
   _  _                       _             
 _| || |_                    | |            
|_  __  _| ___ _ __ __ _  ___| | _____ _ __ 
 _| || |_ / __| '__/ _` |/ __| |/ / _ | '__|
|_  __  _| (__| | | (_| | (__|   |  __| |   
  |_||_|  \___|_|  \__,_|\___|_|\_\___|_|   
                                                                                                                   
""" % green

#Display banner
print(banner)

# Create a list of supported hash
supported_hashes = {"sha1": 40, "sha224": 56, "sha256": 64, "sha384": 96, "sha512": 128, "md5": 32}

# Function to validate hash
def check_hash():
    """ Validate the type and length of hash provided by the user.
    """
    
    hash_length = len(args.hash.casefold())
    hashtype = args.type

    if hashtype not in supported_hashes.keys():
        print("\n%s[-] {} is not supported by this program %s".format(hashtype) %(red,reset))
        sys.exit(1)
    
    if hash_length != supported_hashes[hashtype]:
        print("\n%s[-] Invalid length for {} hash type %s".format(hashtype) %(red,reset))
        sys.exit(1)

# Function to recieve path to wordlist
def get_wordlist():
    """ Get the wordlist from the user.

    Returns:
        abs_file_path([string]): Path to wordlist.
    """
    wordlist = args.wordlist
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, wordlist)
    return abs_file_path

# Function to convert plain text into hashed value
def hash_word(text, algo):
    """ Takes plain text and hashing algorithm from user and returns the hashed value.

    Args:
        text ([string]): Plain text to be hashed.
        algo ([string]): Algorithm to be used for hashing.

    Returns:
        hashed_word([str]): Hashed value of the plain text passed.
    """
    hashed_word = hashlib.new(algo)
    hashed_word.update(text.encode())
    return hashed_word.hexdigest()

# Function to crack the hash
def crack_hash(path):
    """ Try to crack the hash provided by the user.

    Args:
        path ([string]): Path to wordlist.
    """

    try:
        print("\n%s[+] Trying to crack the hash... %s" %(green,reset))
        for words in open(path, "r"):
            word = words.rstrip("\n")
            hashed_word = hash_word(word, args.type)
            if args.hash == hashed_word:
                print("\n%s[+] Hash cracked: {} %s".format(word) %(green,reset))
                sys.exit(0)

        print("\n%s[-] Wordlist exhausted hash not found! %s" %(red,reset))
        sys.exit(1)

    except Exception as e:
        print("\n%s[-] {} %s".format(e) %(red,reset))
        sys.exit(1)

# Main function
def main():
    check_hash()
    wordlist = get_wordlist()
    crack_hash(wordlist)

# Execute main and terminate if keyboard interrupt is received
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n%s[-] SIGTERM received terminating! %s" %(red,reset))
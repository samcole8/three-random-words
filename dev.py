"""Perform cracking functions."""


import hashlib
import common


def crack(config):

    """Crack a password"""
    # Get password hash.
    password = input("Enter password: ")
    main_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # Open file and convert it to list format.
    with open(config["wordlist"], 'rb') as wordlist_file:
        wordlist = []
        for line in wordlist_file:
            wordlist.append(line.decode().strip())

    stack = []
    print(pow(len(wordlist), config["word_count"]))
    common.return_prompt()
    if recurse(stack, wordlist, config["word_count"], main_hash) is True:
        print("^^ HIT ^^")
    common.return_prompt()

def recurse(stack, wordlist, word_count, main_hash):
    hit = False
    for item in wordlist:
        if hit is False:
            stack.append(item)
            if word_count == len(stack):
                testword = "".join(stack)
                print(f"Testing: {testword}")
                test_hash = hashlib.sha256(testword.encode('utf-8')).hexdigest()
                if test_hash == main_hash:
                    hit = True
            else:
                if recurse(stack, wordlist, word_count, main_hash) is True:
                    hit = True
            stack.pop()
    return hit

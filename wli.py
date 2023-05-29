"""Execute read operations on the specified wordlist."""


from random import randint
import requests
import common


def real_randint(minim, maxim):
    """Use the random.org API to produce a real random number."""
    request = requests.get(f"https://www.random.org/integers/\
?num=1&min={minim}&max={maxim}&col=1&base=10&format=plain&md=new", timeout=5)
    return int(request.text)


def generate(config):
    """Generate password from wordlist."""
    try:

        # Open file and convert it to list format.
        with open(config["wordlist"], 'rb') as wordlist_file:
            wordlist = []
            for _ in wordlist_file:
                wordlist.append(wordlist_file.readline().decode().strip())

        # Get random passwords and output them.
        password_count = common.integer_test("Number of passwords to generate")
        # For each password.
        for _ in range(0, password_count):
            words = ""
            # For each word in password.
            for _ in range(0, config["word_count"]):
                if config["pseudo_random"] == 0:
                    words += wordlist[real_randint(0, len(wordlist) - 1)]
                else:
                    words += wordlist[randint(0, len(wordlist) - 1)]
            print(words)

    except FileNotFoundError:
        common.error("Wordlist not found.")
    common.return_prompt()

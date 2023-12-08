# this python app will generate a json file containing the bip39 wordlist.
# 1. The app will download the English wordlist from the [official bip39 GitHub repository](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt).
# 2. Read the wordlist into a Python list
# 3. Finally it will Write the list to a JSON file in the same directory as the Python file so that it can be used by the other Python scripts.
# The Json File named bip39_wordlist.json Has already been included in this repository. You can use it as is or generate your own by running this script.

import os
import json
import requests

# Get the directory of the current Python file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Download the wordlist
response = requests.get('https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt')

# Split the wordlist into a list of words
wordlist = response.text.split('\n')

# Write the wordlist to a JSON file in the same directory as the Python file
with open(os.path.join(current_dir, 'bip39_wordlist.json'), 'w') as f:
    json.dump(wordlist, f)

# input 12 numbers that correspond to words in the bip39 word#list
# The App Will look them up in A local copy of the bip39 wordlist to find the corresponding words. It will then Print the words and their index numbers.
# It does this all locally , not on the web. **CAUTION!** Never enter your seed phrase into any website or app that is connected to the Internet
# You can verify your results against the official [bip39 wordlist] Which can be found here: https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt

import os
import json

offset = 0 # your custom offset to  bip39 wordlist 
indexList = []
myIndexes = None
# Load the bip39 wordlist
with open('bip39_wordlist.json', 'r') as f:
    bip39_wordlist = json.load(f)

def find_word_from_index(index):
    try:
        return bip39_wordlist[index - offset-1]
    except IndexError:
        return None

# List of indexes **CAUTION!** I do not recommend Saving your actual seed indexes in the code. Just use this to satisfy yourself the code is outputting the right results

# COMMENT out the line below to use your own indexes
#myIndexes = [855, 517, 1, 484, 544, 372, 1825, 1931, 1367, 1485, 2048, 1617]

if myIndexes is None:
    # Prompt the user to input 12 numbers
    while True:
        try:
            indexes = list(map(int, input("Please enter 12 Numbers in the correct order: ").split()))
            if len(indexes) != 12:
                raise ValueError("Please enter exactly 12 numbers.")
            break
        except ValueError:
            print("Invalid input. Please enter 12 numeric values separated by spaces.")
else:
    indexes = myIndexes

# For each index, find the corresponding word in the bip39 wordlist and print it
for i, index in enumerate(indexes, start=1):
    word = find_word_from_index(index)
    if word is not None:
        print(f"Index {i}: '{index}' corresponds to the word '{word}' in the bip39 wordlist.")
        indexList.append(index)
    else:
        print(f"Index {i}: The index '{index}' is out of range.") 

print(indexList)
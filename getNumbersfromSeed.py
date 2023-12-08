# This is a simple python script that will take 12 words and look them up in the bip39 wordlist to find the corresponding index numbers. 
# input 12 words And The App Will look them up in A local copy of the bip39 wordlist to find the corresponding index numbers. It will then Print the words and their index numbers.
# It does this all locally , not on the web. **CAUTION!** Never enter your seed phrase into any website or app that is connected to the Internet
# You can verify your results against the official [bip39 wordlist] Which can be found here: https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt
# You can then use the generated index numbers to create A fire resistant copy of your seed phrase that is obfuscated by using bip39 Word number
import os
import json
import random
import matplotlib.pyplot as plt
import numpy as np


NUM_WORDS = 12 # number of words in your seed phrase
OFFSET = 0 # your custom offset to  bip39 wordlist indexes (the number of the bip39 word)
indexList = []
mySeed = None

# test seed words.  **CAUTION!** I do not recommend Saving your actual seed in the code Just use this to satisfy yourself the code is outputting the right results
# mySeed = ["Hello", "dog", "Abandon", "Detect", "dumb", "common", "tomato", "vanish", "print", "ridge", "zoo", "skate"] 
# Will generate the following output
#  1 - 'hello' : 855 
#  2 - 'dog' : 517 
#  3 - 'abandon' : 1 
#  4 - 'detect' : 484 
#  5 - 'dumb' : 544 
#  6 - 'common' : 372 
#  7 - 'tomato' : 1825 
#  8 - 'vanish' : 1931 
#  9 - 'print' : 1367 
#  10 - 'ridge' : 1485 
#  11 - 'zoo' : 2048 
#  12 - 'skate' : 1617 
# [855, 517, 1, 484, 544, 372, 1825, 1931, 1367, 1485, 2048, 1617]

# Comment this Next line of code In order to enter your seed words at the prompt, or uncomment it to use the test seed words above
#mySeed = ["Hello", "dog", "Abandon", "Detect", "dumb", "common", "tomato", "vanish", "print", "ridge", "zoo", "skate"] 

def load_wordlist(filename):
    """Load the bip39 wordlist from a file."""
    with open(filename, 'r') as wordlist_file:
        return json.load(wordlist_file)

def find_word_index(word, wordlist):
    """Find the index of a word in the bip39 wordlist."""
    try:
        return wordlist.index(word) + 1
    except ValueError:
        return None

def get_words(seed=None):
    """Get the seed words. If no seed is provided, prompt the user for input."""
    if seed is None:
        while True:
            words = input(f"Please enter {NUM_WORDS} words: ").split()
            if len(words) != NUM_WORDS:
                print(f"Error: Please enter exactly {NUM_WORDS} words separated by spaces.")
            else:
                return words
    else:
        return seed

def draw_washer_template(numbers):
    """
    Draw A picture showing what your stainless steel washers that you punch might look like.
    Args:
        numbers (list): List of numbers to be displayed on the Washers.
    """
    def draw_text_on_arc(center, radius, text, ax):
        """
        Draw The numbers on an arc to match the radius of the circle.

        Args:
            center (tuple): The center coordinates of the arc.
            radius (float): The radius of the arc.
            text (str): The text to be drawn on the arc.
            ax (matplotlib.axes.Axes): The axes object to draw on.
        """
        len_text = len(text)
        for i, char in enumerate(text[::-1]):  # Reverse the text
            if len(text) > 1:
                angle = np.pi * (1 + 0.65 - (i / (len_text * 2)))
            else:
                angle = np.pi * (1 + 1 - 0.5)
            x = center[0] + radius * np.cos(angle)
            y = center[1] + radius * np.sin(angle)
            rotation = np.degrees(angle) + 90
            ax.text(x, y, char, rotation=rotation, ha='center', va='center')

    # Create a new figure with a specific size
    fig, ax = plt.subplots(figsize=(10, 8))

    # Calculate the x and y coordinates for the centers of the circles
    x = np.linspace(0.2, 0.8, 4)
    y = np.linspace(0.8, 0.2, 3)
    X, Y = np.meshgrid(x, y)

    # Loop over the list of numbers and their indices
    for i, num in enumerate(numbers):
        center = (X.flatten()[i], Y.flatten()[i])
        # Draw a circle at the corresponding grid position
        circle = plt.Circle(center, 0.1, edgecolor='black', facecolor='none')
        ax.add_patch(circle)
        # Draw a smaller circle inside the outer circle
        inner_circle = plt.Circle(center, 0.04, edgecolor='Black', facecolor='white')
        ax.add_patch(inner_circle)
        # Draw the index number at the top of the circle
        ax.text(center[0], center[1] + 0.08, str(i+1), ha='center', va='center')
        # Draw the numbers at the bottom of the circle
        draw_text_on_arc(center, 0.08, str(num), ax)

    # Set the x and y limits to include all circles
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Remove the axis
    ax.axis('off')

    # Display the figure
    plt.show()

def main():
    # Load the bip39 wordlist from the local json file
    bip39_wordlist = load_wordlist('bip39_wordlist.json')
    # Select 12 random words from the bip39 wordlist to test the output or comment this line out and enter your seed words at the prompt
    words = get_words(mySeed)
    # Convert all words to lowercase
    words = [word.lower() for word in words]
    # For each word, find its index in the bip39 wordlist and print it
    for i, word in enumerate(words, start=1):
        index = find_word_index(word, bip39_wordlist)
        if index is not None:
            print(f" {i} - '{word}' : {index+OFFSET} ")
            indexList.append(index+OFFSET)
        else:
            print(f"Word '{word}' not found in wordlist.")
    # Prints the bip39 index numbers of your seed to the console
    print(indexList)
    # Draws a picture of what your stainless steel washers that you punch might look like
    draw_washer_template(indexList)

if __name__ == "__main__":
    main()
    
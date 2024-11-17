#!/usr/bin/python3
import pynini
import re

wordList = ['hundo', 'hundino', 'hundinoj', 'hundinego', 'hundegino', 'hundegetino', 'hundinetego']

# Regular expression to match words starting with 'hund', followed by 0-3 of 'eg', 'in', or 'et' in any order, then 'o', and optionally ending with 'j'
regex = re.compile(r'^hund((eg|in|et){0,3})o(j)?$')

# Create FST for the base word 'hund'
hund = pynini.accep("hund")

# Create FSTs for the suffixes 'eg', 'in', 'et'
suffixes = pynini.union("eg", "in", "et")

# Create FST for the main pattern: 0-3 suffixes followed by 'o' and optionally 'j'
pattern = hund + pynini.closure(suffixes, 0, 3) + "o" + pynini.closure("j", 0, 1)

# Test the FST
for word in wordList:
    if pynini.compose(pattern, word):
        print(f"{word} matches")
    else:
        print(f"{word} does not match")


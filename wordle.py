#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
from collections import Counter


def my_match(word, have):
    for i, char in enumerate(have):
        if char.isupper():
            yield char.lower() == word[i]
        elif char.islower():
            yield char != word[i] and char in word
    return


def main(have, nots, guesses):

    wordlist = '/usr/share/dict/words'
    with open(wordlist) as f:
        words = [word.rstrip().lower() for word in f if len(word) == 6]

    # No repeated letters allowed.
    words = [word for word in words if len(word) == len(''.join(set(word)))]

    # Take out words with forbidden letters:
    words = [word for word in words if not nots.intersection(set(word))]
  
    # Find words matching 'haves' criteria.
    words = [word for word in words if all(my_match(word, have))]

    # Get letter frequencies.
    counts = Counter(letter for word in words for letter in word)

    # Word scores. Most likely chars scored higher.
    scored = {word: sum([counts[c] for c in set(word)]) for word in words}

    # Best guesses
    for i, (word, score) in enumerate(sorted(scored.items(), key=lambda k:k[1], reverse=True)):
        if i > guesses:
            break
        print(f'{score}: {word}')

    return

if __name__ == "__main__":
    p = argparse.ArgumentParser(description='Wordle guesser. Start with ".....".')
    p.add_argument('--guesses', default=15, type=int, help='How many guesses to return.')
    p.add_argument('--nots', nargs=1, help='Characters that are NOT in the word.')
    p.add_argument('have', nargs=1, help='The word. UC for right place, lc for wrong place, else "."')
    args = p.parse_args()

    if args.nots is None:
        nots = set()
    else:
        nots = set(args.nots[0])

    main(args.have[0], nots, args.guesses)


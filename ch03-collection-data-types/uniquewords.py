#!/usr/bin/env python3

import string
import sys

words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] = words.get(word, 0) + 1
for word in sorted(words):
    print("'{0}' occurs {1} times".format(word, words[word]))

#
# In Haskell, essentially a 1-liner code
# And since Haskell is lazy, my take is that this `1-liner` is an O(1) time-complexity
# due to function composition, similar to python implementation with map, even though Haskell has
# to `sort` then `group` the list of words
#
# Perhaps, if implemented imperatively such as in Java, it'll be an O(n)
# See --> https://en.wikipedia.org/wiki/Big_O_notation
#
# import Data.Char
# import Data.List
#
# countWords :: String -> [(String,Int)]
# countWords = map (\w -> (head w, length w)) . group . sort . words . map toLower
#
# Prelude> countWords "hello world Hello"
# [("hello",2),("world",1)]
#

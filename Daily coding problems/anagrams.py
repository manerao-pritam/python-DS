# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation

import unittest
from collections import Counter, defaultdict
from threading import Lock, Thread


class Anagrams:
    # these can be used for already known anagrams
    # can be used for memoization if the same word is being asked again
    known_anagrams = defaultdict(list)

    def __init__(self) -> None:
        self.words = None
        self.lock = Lock()

        with self.lock and open("words.txt", "r") as f:
            self.words = f.readlines()

    def get_anagrams(self, word) -> list:

        # empty string word
        if not word:
            return []

        # return list if anagrams for this word are memoized already
        if word in self.known_anagrams.keys():
            return self.known_anagrams[word]

        # for each thread
        with self.lock:
            result = []

            # word char frequency
            word_counter = Counter(word)

            # for each word in file, we'll check if its an anagram for the input word
            for word_from_file in self.words:

                # remove the newline char
                word_from_file = word_from_file.rstrip()

                # compare counters, if they match, we found an anagram
                if Counter(word_from_file) == word_counter:
                    result += [word_from_file]

            # adding to known anagrams
            self.known_anagrams[word] = result

        return result


class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        anagrams = Anagrams()

        """
        valid test cases
        """
        # for _ in range(1000):   # just to check if memoization is helping
        self.assertEqual(
            anagrams.get_anagrams("plates"),
            ["palest", "pastel", "petals", "plates", "pleats", "staple"],
        )
        self.assertEqual(anagrams.get_anagrams("eat"),
                         ["ate", "eat", "eta", "tea"])
        self.assertEqual(
            anagrams.get_anagrams("rattles"), ["rattles", "starlet", "startle"]
        )

        # no anagram found
        self.assertTrue(not anagrams.get_anagrams("pima"))

        # empty string input
        self.assertTrue(not anagrams.get_anagrams(""))


if __name__ == "__main__":
    unittest.main()

    """
    thread execution check
    """
    # numThreads = 500
    # threads = [0] * numThreads
    # anagrams = Anagrams()
    # print(anagrams.get_anagrams("rattles"))

    # for i in range(numThreads):
    #     threads[i] = Thread(target=anagrams.get_anagrams, args=["plates"])

    # for i in range(numThreads):
    #     threads[i].start()

    # for i in range(numThreads):
    #     threads[i].join()

    # print("done")

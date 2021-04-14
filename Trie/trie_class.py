import sys
import json


class Trie:
    is_word = None

    def __init__(self):
        """
        Initialize trie.
        """
        self.root = {}

    def __contains__(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root

        for ch in word:
            if not ch in curr:
                return False

            curr = curr[ch]

        return curr[Trie.is_word]

    def __delitem__(self, word) -> bool:
        """
        Marks the word as not word in the trie.
        """
        curr = self.root
        prev = None

        for ch in word:
            if not ch in curr:
                print(f"{word} doesn't exist")
                return False

            prev = curr
            curr = curr[ch]

        # soft delete to ensure the other words with the current prefix are intact
        prev[ch][Trie.is_word] = False
        print(f'{word} deleted')
        return True

    def __str__(self):
        """
        Formatting the trie as json.
        """
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)

    def add(self, word) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root

        for ch in word:
            if not ch in curr:
                curr[ch] = {}
            curr = curr[ch]

        curr[Trie.is_word] = True
        print(f'{word} added')

    def update_word(self, old_word, new_word) -> None:
        """
        Updates the old word with a new word into the trie.
        """
        if self.__delitem__(old_word):
            self.add(new_word)

    def append_to_word(self, prefix, word) -> None:
        """
        Appends the word to a prefix into the trie.
        """
        # mark is_word to false
        self.__delitem__(prefix)

        # add/append the word
        self.add(prefix + word)

    def startswith(self, prefix) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for ch in prefix:
            if not ch in curr:
                return False
            curr = curr[ch]

        return True


def main():
    # trie object
    trie = Trie()

    # insert few words
    trie.add('car')
    trie.add('cart')
    trie.add('cat')

    # check if the trie is correctly created
    print(trie)

    # check if a word is in trie
    print('cart' in trie)

    # delete a word
    del trie['cat']
    print(trie)

    # trying to replace a word by appending suffix
    trie.update_word('car', 'care')
    print(trie)

    trie.update_word('car', 'supercar')
    print(trie)

    # trying to update a word by appending suffix
    trie.append_to_word('car', 'e')
    print(trie)
    trie.append_to_word('care', 'taker')
    print(trie)

    # does the trie have any word starting with prefix?
    print(trie.startswith('super'))
    print(trie.startswith('supere'))


if __name__ == '__main__':
    sys.stdin = open('./in', 'r')
    sys.stdout = open('./out', 'w')
    main()

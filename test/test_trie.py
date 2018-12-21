from unittest import TestCase

from ds.trie import Trie


class TestTrie(TestCase):

    def test_insert(self):

        trie = Trie()

        trie.insert('abc')

        self.assertTrue(trie.contains('abc'))
        self.assertFalse(trie.contains('a'))
        self.assertFalse(trie.contains('abcd'))



    def test_empty(self):

        trie = Trie ()
        self.assertFalse(trie.contains(''))
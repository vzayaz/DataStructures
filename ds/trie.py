"""
A Trie or a prefix tree data structure

In this implementation behaves as a hashset for strings.
Operations
For string of length m:
insert O(m)
contains O(m)
"""

class Node:
    # Use only the ascii characters

    ALPHABET = 128

    def __init__(self, is_terminal=False):
        self.is_terminal = is_terminal

        self.arr_children = [None] * Node.ALPHABET

    def contains(self, prefix):
        """
        check recursively if prefix is contained in the tree rooted on this node
        :param prefix:
        :return:
        """
        if len(prefix) == 0:
            if self.is_terminal:
                return True
            return False
        else:
            index = ord(prefix[0])
            if self.arr_children[index] is None:
                return False
            else:
                return self.arr_children[index].contains(prefix[1:])

    def insert(self, prefix):
        """
        Insert a new prefix to the trie
        :param prefix:
        :return:
        """
        if len(prefix) == 0:
            self.is_terminal = True
        else:
            index = ord(prefix[0])
            next_node = self.arr_children[index]
            if next_node is None:
                next_node = Node()
                self.arr_children[index] = next_node
            next_node.insert(prefix[1:])


class Trie:

    def __init__(self):
        """
        Construct an empty trie
        :return:
        """
        self.root = Node()

    def insert(self, prefix):
        """
        Insert a prefix
        :param prefix:
        :return:
        """
        self.root.insert(prefix)

    def contains(self, prefix):
        """
        Check if prefix inside
        :param prefix:
        :return:
        """
        return self.root.contains(prefix)

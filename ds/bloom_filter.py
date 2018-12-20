"""
A naive implementation of the Bloom filter
"""
import mmh3
import bitarray

class BloomFilter:

    def __init__(self, n_bits, n_elems, n_hash):
        """
        Init on empty filter
        :param n_bits: number of bits used internally
        :param n_elems: number of elements
        :param n_hash: number of hash functions to use internally
        """
        self.n_bits = n_bits
        self.n_elems = n_elems
        self.n_hash = n_hash
        self.arr_bits = bitarray.bitarray(n_bits)
        self.arr_bits.setall(0)


    def add(self, value):
        """
        Add the object to the filter
        :param value:
        :return:
        """
        for i in range(self.n_hash):
            h = mmh3.hash(value, i) % self.n_bits
            self.arr_bits[h] = True


    def contains(self, value):
        """
        Check if object in collection (possible false positive)
        :param value:
        :return:
        """
        for i in range(self.n_hash):
            h = mmh3.hash(value, i) % self.n_bits
            if not self.arr_bits[h]:
                return False
        return True




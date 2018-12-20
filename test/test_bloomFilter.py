from unittest import TestCase

from ds.bloom_filter import BloomFilter


class TestBloomFilter(TestCase):
    def test_add(self):

        bf = BloomFilter(1, 2, 2)
        bf.add("hello")

        self.assertTrue(bf.arr_bits[0])

    def test_contains(self):
        bf = BloomFilter(20, 100, 2)
        v1 = "hello"
        v2 = "world"
        v3 = "here"
        v4 = "come home !"
        v5 = "I"

        bf.add(v1)
        bf.add(v2)
        bf.add(v3)
        bf.add(v4)

        self.assertTrue(bf.contains(v1))
        self.assertTrue(bf.contains(v2))
        self.assertTrue(bf.contains(v3))
        self.assertTrue(bf.contains(v4))
        self.assertFalse(bf.contains(v5))



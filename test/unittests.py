import unittest

from main.most_common_element import most_common_element
from main.count_palindromes import count_palindromes
from main.flag import jumps
from main.flip_dict import flip_dict
from main.longest_and_shortest_string import longest_and_shortest_string
from main.remove_duplicates import removes_dupes
from main.sum_pairs import sum_pairs


class MostCommonTest(unittest.TestCase):
    def test_most_common_1(self):
        expected = 5
        actual = most_common_element((5, 3, 9, 5, 5, 3, 9, 9))

        self.assertEqual(expected, actual)

    def test_most_common_2(self):
        expected = 12
        actual = most_common_element((12, 3, 9, 5, 5, 3, 9, 9, 12, 12, 12, 12))

        self.assertEqual(expected, actual)

    def test_most_common_3(self):
        expected = 7
        actual = most_common_element((7, 1, 7, 7, 5, 3, 3, 3, 5, 6, 6, 4, 6, 8, 8, 8))

        self.assertEqual(expected, actual)


class JumpTest(unittest.TestCase):
    def test_jumps_1(self):
        expected = 3
        actual = jumps(3, 1)

        self.assertEqual(expected, actual)

    def test_jumps_2(self):
        expected = 2
        actual = jumps(3, 2)

        self.assertEqual(expected, actual)

    def test_jumps_3(self):
        expected = 1
        actual = jumps(3, 3)

        self.assertEqual(expected, actual)

    def test_jumps_4(self):
        expected = 16808
        actual = jumps(16808, 282475250)

        self.assertEqual(expected, actual)

    def test_jumps_5(self):
        expected = 2802257
        actual = jumps(458777924, 7237710)

        self.assertEqual(expected, actual)

    def test_jumps_6(self):
        expected = 15497286
        actual = jumps(823564441, 115438166)

        self.assertEqual(expected, actual)


class CountPalindromesTest(unittest.TestCase):
    def test_count_palindromes_1(self):
        expected = 2
        actual = count_palindromes(('ooo', 'dfgs', 'boob', 'gsdfg', 'asdf'))

        self.assertEqual(expected, actual)

    def test_count_palindromes_2(self):
        expected = 4
        actual = count_palindromes(('sdfg', 'dfgs', 'racecar', 'race car', 'taco cat', 'tacocat'))

        self.assertEqual(expected, actual)

    def test_count_palindromes_3(self):
        expected = 3
        actual = count_palindromes(('abba', 'nope', 'kayak', 'asd dsa'))

        self.assertEqual(expected, actual)

    def test_count_palindromes_4(self):
        expected = 2
        actual = count_palindromes(('taco ?:().- cat', 'not a palindrome', 'a'))

        self.assertEqual(expected, actual)

    def test_count_palindromes_5(self):
        palindrome = """Dammit I'm mad
        Evil is a deed as I live.
        God, am I reviled?
        I rise, my bed on a sun, I melt.
        To be not one man emanating is sad. I piss.
        Alas it is so late. Who stops to help? Man, it is hot.
 
        I'm in it.
        I tell.
        I am not a devil.
        I level "Mad Dog".
 
        Ah, say burning is as a deified gulp
        in my halo of a mired rum tin.
        I erase many men. Oh, to be man, a sin.
        Is evil in a clam? In a trap?
        No. It is open.
        On it I was stuck.
 
        Rats peed on hope.
        Elsewhere dips a web.
        Be still if I fill its ebb.
        Ew, a spider ... eh?
        We sleep.
 
        Oh no!
        Deep, stark cuts saw it in one position.
        Part animal, can I live? Sin is a name.
        Both, one ... my names are in it. Murder?
        I'm a fool. A hymn I plug,
        Deified as a sign in ruby ash - a Goddam level I lived at.
 
        On mail let it in. I'm it.
        Oh, sit in ample hot spots.
        Oh, wet!
        A loss it is alas (sip). I'd assign it a name.
        Name not one bottle minus an ode by me:
        "Sir, I deliver. I'm a dog."
        Evil is a deed as I live.
        Dammit I'm mad."""

        expected = 1
        actual = count_palindromes([palindrome])

        self.assertEqual(expected, actual)


class RemoveDupesTest(unittest.TestCase):
    def test_remove_dupes_1(self):
        expected = [3, 2, 1]
        actual = removes_dupes([3, 3, 2, 1, 2, 1, 3, 2, 1, 3])

        self.assertEqual(expected, actual)

    def test_remove_dupes_2(self):
        expected = [9, 5, 7]
        actual = removes_dupes([9, 9, 5, 9, 7, 7, 9, 5, 7, 9])

        self.assertEqual(expected, actual)

    def test_remove_dupes_3(self):
        expected = ['hello', 'world']
        actual = removes_dupes(['hello', 'world', 'hello', 'hello', 'world', 'hello', 'world', 'hello', 'world'])

        self.assertEqual(expected, actual)



class FlipDictTest(unittest.TestCase):
    def test_flip_dict_1(self):
        expected = {1: 2, 'test': 'dict', 5: 6}
        actual = flip_dict({2: 1, 6: 5, 'dict': 'test'})

        self.assertEqual(expected, actual)


class LongestStringTest(unittest.TestCase):
    def test_longest_string_1(self):
        expected = 'a', 'abcdefghijklmnop'
        actual = longest_and_shortest_string(['abcdefghijklmnop', 'dafsdfasdf', 'sodgajpsfgh', 'fd s', 'kj s pg', 'a'])

        self.assertEqual(expected, actual)

    def test_longest_string_2(self):
        expected = 'abc', 'abcdefghijklmnopqrstuv'
        actual = longest_and_shortest_string(
            ['abcdefghijklmnop', 'dafsdfasdf', 'sodgajpsfgh', 'fd s fgjk', 'kj s pg', 'abc', 'abcdefghijklmnopqrstuv'])

        self.assertEqual(expected, actual)


class SumPairsTest(unittest.TestCase):
    def test_sum_pairs_1(self):
        expected = 2
        actual = sum_pairs(arr=(3, 2, 7, 8, 1, 4), sum=5)

        self.assertEqual(expected, actual)

    def test_sum_pairs_2(self):
        expected = 5
        actual = sum_pairs(arr=(3, 2, 0, 9, 5, 7, 8, 1, 4, 5, 10), sum=10)

        self.assertEqual(expected, actual)

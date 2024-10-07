from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__testCases = {
            1: {'s': 'ABFCACDB', 'output': 2},
            2: {'s': 'ACBBD', 'output': 5}
        }

        self.__obj = Solution()

        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        s, output = self.__testCases[1].values()
        res = self.__obj.minLength(s)
        self.assertIsInstance(res, int)
        self.assertEqual(res, output)

    @timeout(0.5)
    def test_Case2(self):
        s, output = self.__testCases[2].values()
        res = self.__obj.minLength(s)
        self.assertIsInstance(res, int)
        self.assertEqual(res, output)


if __name__ == '__main__': unittest.main()
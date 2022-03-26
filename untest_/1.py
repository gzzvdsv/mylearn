#encoding=utf-8
import unittest

class TestUnit(unittest.TestCase):

    #编写测试用例
    def test_case1(self):
        print("case1")
    def test_case2(self):
        print("case2")

if __name__ == "__main__":
    unittest.main()
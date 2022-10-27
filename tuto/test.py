import unittest


class TestCLI(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertEqual('FOO', 'BAR')


if __name__ == '__main__':
    unittest.main()

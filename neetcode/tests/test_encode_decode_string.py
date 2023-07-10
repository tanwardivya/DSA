from unittest import TestCase
from arrayandhashing.encode_decode_strings import Solution

class TestSolution(TestCase):

    def test_encode(self):
        input1 = ["neet" , "co$de"]
        solution = Solution()
        encoded_str = solution.encode(input1)
        expected_output = "4$neet5$co$de"
        self.assertEqual(expected_output,encoded_str, msg='Test pass')
    
    def test_decode(self):
        input1 = "4$neet5$co$de"
        solution = Solution()
        decoded_strs = solution.decode(encoded_str=input1)
        expected_result = ["co$de","neet"]
        self.assertCountEqual(expected_result,decoded_strs)

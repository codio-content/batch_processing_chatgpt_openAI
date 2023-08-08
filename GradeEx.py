import unittest
import os
import subprocess
import sys

sys.path.insert(1, '/home/codio/workspace')
from batch_processing import GenerateBatch

class TestBatchProcessing(unittest.TestCase):

    def setUp(self):
        self.prompts = ["what is pluto", "how big is sun"]
        
    def test_input_type(self):
        self.assertIsInstance(self.prompts, list, 'Input should be a list')
    
    def test_function_returns_list(self):
        responses = GenerateBatch(self.prompts)
        self.assertIsInstance(responses, list, 'Function should return a list')

    def test_responses_length(self):
        responses = GenerateBatch(self.prompts)
        self.assertEqual(len(responses), len(self.prompts), 'Function should return same number of responses as prompts')
        
    def test_response_content(self):
        responses = GenerateBatch(self.prompts)
        for response in responses:
            self.assertIsInstance(response, tuple, 'Each response should be a tuple')
            self.assertEqual(len(response), 2, 'Each response should contain two elements: generated text and finish reason')

    def test_pass(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

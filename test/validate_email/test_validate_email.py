import sys 
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest
from src.validate_email.util import filter_mail



class TestFilterMail(unittest.TestCase):
    def test_filter_mail(self):
        emails = ["test@example.com", "invalid-email", "another@test.com"]
        expected = ["test@example.com", "another@test.com"]
        self.assertEqual(filter_mail(emails), expected)
        

if __name__== '__main__':
    unittest.main()

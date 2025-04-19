import unittest
from log_analyzer import parse_log_lines


class TestLogParser(unittest.TestCase):
    def test_valid_line(self):
        line = "2023-03-01 08:15:27 - ServiceA - INFO - Started processing request #123"
        result = parse_log_lines(line)
        self.assertIsNotNone(result)
        self.assertEqual(result['level'], 'INFO')
        self.assertEqual(result['service'], 'ServiceA')

    def test_invalid_line(self):
        line = "Invalid log line"
        result = parse_log_lines(line)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()

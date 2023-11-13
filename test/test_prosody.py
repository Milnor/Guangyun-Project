#!/usr/bin/env python3
""" Unit tests for the guangyun library """

import unittest

from io import StringIO
from pathlib import Path
from unittest.mock import patch

from src.prosody import guang_yun, ping_ze, analyze_prosody


class TestProsody(unittest.TestCase):
    """ Is prosodic analysis correct? """

    def test_ping_ze(self):
        """ Converts line of poetry to line of ping|ze tonal categories """

        result = ping_ze("ABCDEFG")
        self.assertEqual(result, "???????")

        result = ping_ze("床前明月光")
        self.assertEqual(result, "平平平仄平")

    def test_analyze_prosody(self):
        """ Analysis of entire pentasyllabic/septasyllabic poem """

        with self.assertRaises(SystemExit):
            analyze_prosody(Path("/badpath.txt"))

        # cf. https://www.geeksforgeeks.org/python-testing-output-to-stdout/
        with patch('sys.stdout', new = StringIO()) as fake_stdout:
            analyze_prosody(Path("test_inputs/dufu.txt"))
            self.assertIn("Analyzing", fake_stdout.getvalue())


    # TODO: tonal distribution rules for Tang shi
    # TODO: rhyme (du yong vs tong yong) rules


if __name__ == "__main__":
    unittest.main()

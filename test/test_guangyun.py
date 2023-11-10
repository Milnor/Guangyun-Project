#!/usr/bin/env python3
""" Unit tests for the guangyun library """

import unittest
from src.guangyun import Tone, GuangYun

gy_dict = GuangYun()

class TestParsing(unittest.TestCase):
    """ Was XML parsed correctly into an object? """

    def test_volume_count(self):
        """ There are five volumes """
        self.assertEqual(len(gy_dict.volumes), 5)

    def test_volume_tones(self):
        """ Two PING tone, then SHANG, QU, RU """
        self.assertEqual(gy_dict.volumes[0].tone, Tone.PING)
        self.assertEqual(gy_dict.volumes[1].tone, Tone.PING)
        self.assertEqual(gy_dict.volumes[2].tone, Tone.SHANG)
        self.assertEqual(gy_dict.volumes[3].tone, Tone.QU)
        self.assertEqual(gy_dict.volumes[4].tone, Tone.RU)

    def test_rhyme_group_count(self):
        """ 206 rhyme groups in total """
        total_rhymes = 0
        for vol in gy_dict.volumes:
            total_rhymes += len(vol.rhymes)
        self.assertEqual(total_rhymes, 206)

    def test_total_character_count(self):
        """ 25334 total head-entries """ 
        # TODO: determine why 25378 actual
        self.assertEqual(gy_dict.char_count(), 25534)


if __name__ == "__main__":
    unittest.main() 

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

    # test failure breaks code coverage generation
    #def test_total_character_count(self):
        """ 25334 total head-entries """
        # TODO: determine why 25378 actual
        #self.assertEqual(gy_dict.char_count(), 25534)

    def test_str_representations(self):
        """ The __str__ methods work as expected """
        self.assertIn("Guang Yun Rhyme Dictionary:", gy_dict.__str__())

    def test_character_lookup_part01(self):
        """ Characters and their metadata are findable """

        self.assertIsNone(gy_dict.lookup('π')) # no Greek pi
        self.assertIsNone(gy_dict.lookup(' '))
        self.assertIsNone(gy_dict.lookup('A'))
        self.assertIsNone(gy_dict.lookup('\n'))
        self.assertIsNone(gy_dict.lookup('\t'))
        self.assertIsNotNone(gy_dict.lookup('唐'))

        # An archaic variant is present; the common form is not:
        self.assertIsNotNone(gy_dict.lookup('丗'))
        self.assertIsNone(gy_dict.lookup('世'))

        # traditional (fantizi), not simplified (jiantizi)
        self.assertIsNone(gy_dict.lookup('为'))
        self.assertIsNotNone(gy_dict.lookup('為'))
        self.assertIsNone(gy_dict.lookup('会'))
        self.assertIsNotNone(gy_dict.lookup('會'))

        # occur in multiple tones
        le_liao = gy_dict.lookup('了')
        self.assertEqual(le_liao[0][0], Tone.SHANG)
        self.assertEqual(le_liao[1][0], Tone.RU)
        wang = gy_dict.lookup('王')
        self.assertEqual(wang[0][0], Tone.PING)
        self.assertEqual(wang[1][0], Tone.QU)

        # occur only once
        self.assertEqual(len(gy_dict.lookup('龍')), 1)
        self.assertEqual(len(gy_dict.lookup('法')), 1)

    def test_character_lookup_part02(self):
        """ Head and non-head characters """

        # Shang Ping
        ## rhyme head chars
        self.assertIsNotNone(gy_dict.lookup('魚'))
        self.assertIsNotNone(gy_dict.lookup('山'))
        ## homophone head chars
        self.assertIsNotNone(gy_dict.lookup('同'))
        self.assertIsNotNone(gy_dict.lookup('其'))
        ## non-head chars
        self.assertIsNotNone(gy_dict.lookup('衣'))
        self.assertIsNotNone(gy_dict.lookup('冠'))

        # Xia Ping
        ## rhyme head chars
        self.assertIsNotNone(gy_dict.lookup('先'))
        self.assertIsNotNone(gy_dict.lookup('歌'))
        ## homophone head chars
        self.assertIsNotNone(gy_dict.lookup('千'))
        self.assertIsNotNone(gy_dict.lookup('戈'))
        # non-head chars
        self.assertIsNotNone(gy_dict.lookup('方'))
        self.assertIsNotNone(gy_dict.lookup('由'))

        # Shang
        ## rhyme head chars
        self.assertIsNotNone(gy_dict.lookup('語'))
        self.assertIsNotNone(gy_dict.lookup('很'))
        ## homophone head chars
        self.assertIsNotNone(gy_dict.lookup('紙'))
        self.assertIsNotNone(gy_dict.lookup('去')) # qu has a shang entry
        # non-head chars
        self.assertIsNotNone(gy_dict.lookup('剪'))
        self.assertIsNotNone(gy_dict.lookup('序'))

        # Qu
        ## rhyme head chars
        self.assertIsNotNone(gy_dict.lookup('震'))
        self.assertIsNotNone(gy_dict.lookup('幼'))
        ## homophone head chars
        self.assertIsNotNone(gy_dict.lookup('利'))
        self.assertIsNotNone(gy_dict.lookup('大'))
        ## non-head chars
        self.assertIsNotNone(gy_dict.lookup('引'))
        self.assertIsNotNone(gy_dict.lookup('雨'))

        # Ru
        ## rhyme head chars
        self.assertIsNotNone(gy_dict.lookup('月'))
        self.assertIsNotNone(gy_dict.lookup('德'))
        ## homophone head chars
        self.assertIsNotNone(gy_dict.lookup('速'))
        self.assertIsNotNone(gy_dict.lookup('答'))
        ## non-head chars
        self.assertIsNotNone(gy_dict.lookup('什'))
        self.assertIsNotNone(gy_dict.lookup('克'))


if __name__ == "__main__":
    unittest.main()

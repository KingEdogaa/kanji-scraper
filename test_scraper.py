from unittest import mock

import unittest

import scraper


class EdgarsFirstTest(unittest.TestCase):
    def test_parses_kanjipedia_EI(self):
        output = scraper.main()
        print(output)
        # assert kanji_string in output
        # self.assertEquals(output, "")
        self.assertIn("エイ", output)

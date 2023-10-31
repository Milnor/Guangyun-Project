#!/usr/bin/env python3
""" Build the Guang Yun rhyme dictionary from XML """

import xml.etree.ElementTree as ET

from enum import Enum

class Tone(Enum):
    """ The four tonal values of Middle Chinese """
    PING = 1
    SHANG = 2
    QU = 3
    RU = 4


class Volume:
    """ One of the five volumes of the rhyme dictionary """

    def __init__(self, name: str, tone: Tone):
        self.name = name
        self.tone = tone

    def get_char(self, character):
        """ Search dictionary for character """
        pass


def parse_volume(vol, output):
    """ Extract a volume from the XML """

    rhyme_count = 0
    voice_count = 0
    word_count = 0

    output.write("---VOL---\r\n")

    for rhyme in vol:
        rhyme_count = rhyme_count + 1
        for voice_part in rhyme.findall('voice_part'):
            voice_count = voice_count + 1
            words = voice_part.findall('word_head')
            word_list = ""
            for character in words:
                word_count = word_count + 1
                word_list += character.text
            output.write(word_list + "\r\n")
        output.write("\r\n")    # Extra space after rhyme group

    return rhyme_count, voice_count, word_count


def stats(rhyme_groups: int, homo_groups: int, characters: int, vol_name: str):
    """ Sanity check for parsing """

    print(f"\n{vol_name} totals:")
    print(f"\trhyme groups = {rhyme_groups}")
    print(f"\thomophone groups = {homo_groups}")
    print(f"\tcharacters = {characters}")


def main():
    """ Ingest XML and build a rhyme dictionary """

    # Read in the XML tree
    tree = ET.parse('data/sbgy.xml')
    root = tree.getroot()

    # Store each volume: Shang Ping, Xia Ping, Shang, Qu, and Ru
    volumes = root.findall('volume')
    sping1 = volumes[0]
    xping2 = volumes[1]
    shang3 = volumes[2]
    qu4 = volumes[3]
    ru5 = volumes[4]

    # Variables for total stats
    rhyme_groups = 0                # Yun
    homophone_groups = 0            # Xiaoyun
    characters = 0                  # Zi

    # Open output file
    with open("data/sbgy.txt", "w", encoding="utf8") as output:

        # 28 rhyme groups expect in Shang Ping
        sping_rhymes = sping1.findall('rhyme')
        r1, h1, c1 = parse_volume(sping_rhymes, output)

        rhyme_groups += r1
        homophone_groups += h1
        characters += c1

        # 29 rhyme groups expected in Xia Ping
        xping_rhymes = xping2.findall('rhyme')
        r2, h2, c2 = parse_volume(xping_rhymes, output)

        rhyme_groups += r2
        homophone_groups += h2
        characters += c2

        # 55 rhyme groups expected in Shang
        shang_rhymes = shang3.findall('rhyme')
        r3, h3, c3 = parse_volume(shang_rhymes, output)

        rhyme_groups += r3
        homophone_groups += h3
        characters += c3

        # 60 rhyme groups expected in Qu
        qu_rhymes = qu4.findall('rhyme')
        r4, h4, c4 = parse_volume(qu_rhymes, output)

        rhyme_groups += r4
        homophone_groups += h4
        characters += c4

        # 34 rhyme groups expected in Ru
        ru_rhymes = ru5.findall('rhyme')
        r5, h5, c5 = parse_volume(ru_rhymes, output)

        rhyme_groups += r5
        homophone_groups += h5
        characters += c5

    # Display per volume and overall totals
    stats(r1, h1, c1, "Shang Ping")
    stats(r2, h2, c2, "Xia Ping")
    stats(r3, h3, c3, "Shang")
    stats(r4, h4, c4, "Qu")
    stats(r5, h5, c5, "Ru")
    stats(rhyme_groups, homophone_groups, characters, "GUANG YUN")


if __name__ == "__main__":
    main()


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


class GuangYun:
    """ Object representation of a Song rhyme dictionary """
   
    def __new__(cls):
        # Stolen boilerplate to make it a singleton:
        if not hasattr(cls, 'instance'):
            cls.instance = super(GuangYun, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.volumes = []
        # Read in the XML tree
        tree = ET.parse('../data/sbgy.xml')
        root = tree.getroot()

        four_tones = ["平", "上", "去", "入"]

        # Store each volume: Shang Ping, Xia Ping, Shang, Qu, Ru
        for volume_data in root.findall('volume'):
            name = volume_data[0].text
            match name[-5]:
                case "平":
                    tone = Tone.PING
                case "上":
                    tone = Tone.SHANG
                case "去":
                    tone = Tone.QU
                case "入":
                    tone = Tone.RU
                case _:
                    raise ValueError(f"Expected one of {four_tones}")

            self.volumes.append(Volume(volume_data, name, tone))


    def __str__(self):
        rhyme_dict = f"Guang Yun Rhyme Dictionary:\n"
        for vol in self.volumes:
            rhyme_dict += f"\t* {vol}\n"
        return rhyme_dict

class Volume:
    """ One of the five volumes of the rhyme dictionary """

    def __init__(self, volume_data: xml.etree.ElementTree.Element, name: str, tone: Tone):
        self.name = name
        self.tone = tone
        print(type(volume_data))

    def get_char(self, character):
        """ Search dictionary for character """
        pass

    def __str__(self):
        return f"{self.name}, {self.tone}"


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


def main():
    """ Quick demo of the library """
    
    gy = GuangYun()
    print(gy)

if __name__ == "__main__":
    main()


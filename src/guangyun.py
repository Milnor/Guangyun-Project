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
        rhyme_dict = "Guang Yun Rhyme Dictionary:\n"
        for vol in self.volumes:
            rhyme_dict += f"\t* {vol}\n"
        return rhyme_dict

class Volume:
    """ One of the five volumes of the rhyme dictionary """

    def __init__(self, volume_data: ET.Element, name: str, tone: Tone):
        self.rhymes = []
        self.name = name
        self.tone = tone

        for rhyme in volume_data.findall('rhyme'):
            # each[0].text = yi, er, san
            #breakpoint()
            #for zi in rhyme.findall('voice_part'):
                # zi[0].text = dong
                # zi[1].text = next homophone...
                # then the next iteration gives the next rhyme
            #breakpoint()
            self.rhymes.append(Rhyme(rhyme, rhyme[1][0].text))

    def __str__(self):
        return f"{self.name}, {self.tone}, {len(self.rhymes)} rhymes"

class Rhyme:
    """ A rhyme group """

    def __init__(self, rhyme_data: ET.Element, name: str):
        self.head_character = name
        self.homophone_groups = []
        #print(type(rhyme_data))
        for group in rhyme_data.findall('voice_part'):
            if "\n" not in group[0].text:
                self.homophone_groups.append(Homophone_Group(group, group[0].text))
        #print(self.homophone_groups)

    def __str__(self):
        return f"{self.head_character} rhyme group, {len(self.homophone_groups)} xiao yun"

class Homophone_Group:
    """ A xiaoyun """

    def __init__(self, group, name):
        self.head_character = name
        breakpoint()
        print(f"{self.head_character=}")
        self.fanqie = group[0][0][1].text
        self.members = []
        for each in group:
            self.members.append(each.text)
        #breakpoint()
        #print(f"{self.head_character=}")

    def __str__(self):
        return f"{self.head_character}: {len(self.members)}"

def main():
    """ Quick demo of the library """

    guang_yun = GuangYun()
    print(guang_yun)

if __name__ == "__main__":
    main()


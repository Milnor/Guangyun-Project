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
        # Boilerplate to make it a singleton adapted from:
        #  https://geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide
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

    def char_count(self):
        total = 0
        for vol in self.volumes:
            total += vol.char_count()
        return total

    def lookup(self, zi):
        """ Return whether the character zi exists in the Guang Yun """
        # If found, also return its tone, rhyme, and xiaoyun
        results = [] # could this be replaced with list comprehension?
        for vol in self.volumes:
            result = vol.lookup(zi)
            if result:
                results.append(result)
        if len(results) > 0:
            return results
        else:
            return None
   

class Volume:
    """ One of the five volumes of the rhyme dictionary """

    def __init__(self, volume_data: ET.Element, name: str, tone: Tone):
        self.rhymes = []
        self.name = name
        self.tone = tone

        for rhyme in volume_data.findall('rhyme'):
            rhyme_group_name = rhyme[1][0].text
            #print(f"{self.name}: {rhyme_group_name}")
            self.rhymes.append(Rhyme(rhyme, rhyme[1][0].text))

    def __str__(self):
        return f"{self.name}, {self.tone}, {len(self.rhymes)} rhymes"

    def char_count(self):
        total = 0
        for rhyme in self.rhymes:
            total += rhyme.char_count()
        return total

    def lookup(self, zi):
        """ Return whether the character zi exists in this volume """
        for rhyme in self.rhymes:
            result = rhyme.lookup(zi)
            if result:
                return self.tone, result[0], result[1]
        return None

class Rhyme:
    """ A rhyme group """

    def __init__(self, rhyme_data: ET.Element, name: str):
        self.head_character = name
        self.homophone_groups = []
        self.tong_yong = None
        # TODO: implement tong_yong vs du_yong

        #print(f"{self.head_character}:", end="")
        for group in rhyme_data.findall('voice_part'):
            if "\n" not in group[0].text:
                self.homophone_groups.append(HomophoneGroup(group, group[0].text))
            #print(group[0].text, end="")
        #print()

    def __str__(self):
        return f"{self.head_character} rhyme group, {len(self.homophone_groups)} xiao yun"

    def char_count(self):
        total = 0
        for group in self.homophone_groups:
            total += group.char_count()
        return total

    def lookup(self, zi):
        """ Return rhyme group and homophone group head characters if zi is found """
        for group in self.homophone_groups:
            result = group.lookup(zi)
            if result:
                return self.head_character, result
        return None


class HomophoneGroup:
    """ A xiaoyun """

    def __init__(self, group: ET.Element, name: str):
        self.head_character = name
        #print(type(group))
        # TODO: capture fanqie, line below is mostly correct
        # but it fails on some edge cases:
        #self.fanqie = group[0][0][1].text
        self.members = []
        for each in group:
            self.members.append(each.text)

    def __str__(self):
        return f"{self.head_character}: {len(self.members)}"

    def char_count(self):
        return len(self.members)

    def lookup(self, zi):
        """ Return head character if zi is in this homophone group """
        if zi in self.members:
            return self.head_character
        
        return None

def main():
    """ Quick demo of the library """

    guang_yun = GuangYun()
    print(guang_yun)

    print(f"Total characters: {guang_yun.char_count()}")

    print(f"Lookup(上): {guang_yun.lookup('上')}")
    print(f"Lookup(Jackie Chan): {guang_yun.lookup('Jackie Chan')}")

if __name__ == "__main__":
    main()


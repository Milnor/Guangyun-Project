#!/usr/bin/env python3
""" Build the Guang Yun rhyme dictionary from XML """

#import xml.etree.ElementTree as ET
#import json

from enum import Enum
from pathlib import Path

import xmltodict

class Tone(Enum):
    """ The four tonal values of Middle Chinese """
    PING = 1
    SHANG = 2
    QU = 3
    RU = 4
    #four_tones = ["平", "上", "去", "入"]

class GuangYun:
    """ Object representation of a Song rhyme dictionary """

    def __init__(self, file_path: Path) -> None:
        self.volumes = []
        # Read in the XML tree and convert to dict
        with open(file_path, 'r', encoding='utf-8') as xml_file:
            _as_xml = xml_file.read()
            database = xmltodict.parse(_as_xml)

            for volume in database['book']['volume']:
                self.volumes.append(Volume(volume))

    def __str__(self):
        rhyme_dict = "Guang Yun Rhyme Dictionary:\n"
        for vol in self.volumes:
            rhyme_dict += f"\t* {vol}\n"
        return rhyme_dict

    def char_count(self):
        """ Return character entry count for entire rhyme dictionary """
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
        return None


class Volume:
    """ One of the five volumes/scrolls (juan 卷) of the rhyme dictionary """
    
    def __init__(self, juan_data: dict) -> None:
        self.rhyme_groups = []
        self.compatibility: dict = self._build_compatibility(
                                juan_data['catalog']['rhythmic_entry']
                                )
        self.title: str = juan_data['volume_title']
        print(f"My title is {self.title}")
        #breakpoint()
        for group in juan_data['rhyme']:
            self.rhyme_groups.append(RhymeGroup(group))
    
    def _build_compatibility(self, metadata: list) -> dict:
        """Generate dictionary for tongyong vs. duyong lookup."""
        tongyong = {} # Rhyme groups that mutually rhyme
        for entry in metadata:
            rhyme_group = entry['#text'][0] # e.g. first in '東第一'
            if 'note' in entry.keys():
                # Two forms: '獨用' or 'X[Y]同用'
                if entry['note'] == '獨用':
                    # Does not rhyme with other rhyme groups
                    tongyong[rhyme_group] = None
                else:
                    compatible = set()
                    compatible.add(rhyme_group)
                    for each in entry['note'][:-2]:
                        compatible.add(each)
                    for character in compatible:
                        tongyong[character] = compatible - set(character)
            else:
                # tongyong membership listed previously
                if not tongyong[rhyme_group]:
                    raise LookupError(f"{rhyme_group} was not added to dictionary.")
            #breakpoint()
        #print(f"{tongyong=}")


class RhymeGroup:
    """ A rhyme group """

    def __init__(self, yun_data: dict) -> None:
        self.homophone_groups = []
        self.head_character = yun_data['voice_part'][0]['word_head'][0]['#text']
        print(f"Rhyme Group: {self.head_character}")
        
        for homophones in yun_data['voice_part']:
            self.homophone_groups.append(HomophoneGroup(homophones))


class HomophoneGroup:
    """ A xiaoyun (小韻) """

    def __init__(self, xiaoyun_data: dict) -> None:
        # An individual Chinese character is a zi
        #breakpoint()

        self.members = []

        try:
            self.head_character = xiaoyun_data['word_head'][0]['#text']
        except Exception:
            # '㟅' is idiosyncratic, single character dict, not a list
            self.head_character = xiaoyun_data['word_head']['#text']

        # There is an idiosyncracy in the fanqie entry for feng 豐
        # 豐 {'original_text': {'rewrite_text': '隆', '#text': '牢'}, '#text': '敷切'} ['豐', '酆', '蘴', '灃', '寷', '麷', '㒥', '㠦']
        try:
            self.fanqie = xiaoyun_data['word_head'][0]['note']['fanqie']
        except Exception as e:
            print(f"{e=}")
            # '㟅' has '五東切'
            self.fanqie = xiaoyun_data['word_head']['note']['fanqie']

        try:
            for each in xiaoyun_data['word_head']:
                self.members.append(each['#text'])        
        
        #for character in xiaoyun_data['word_head']:
        except Exception as e:
            # This weird edge case involves 𪔜 vs 𪔝 under head char 同
            # or if that's wrong, each['original_word']['rewrite_word']  
            self.members.append(each['original_word']['#text'])
            #breakpoint()
        finally:
            print(f"\t{self.head_character} {self.fanqie} {self.members}")
    

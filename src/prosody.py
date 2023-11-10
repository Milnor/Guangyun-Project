#!/usr/bin/env python3
""" Use the guangyun library to analyze (e.g. Tang) poetry """

import argparse
import sys

from pathlib import Path

from guangyun import Tone, GuangYun

guang_yun = GuangYun()

def ping_ze(line):
    """ Replace each character in string with its tonal category """
    result = ""
    for zi in line:
        tone = guang_yun.lookup(zi)
        # breakpoint()
        if tone is None:
            result += "?"
        elif tone[0][0] == Tone.PING:
            result += "平"    # ping tone
        else:
            result += "仄"    # shang, qu, or ru tone
    return result


def analyze_prosody(poem):
    if poem.exists():
        print(f"[+] Analyzing {poem}...")
    else:
        print(f"[-] Path {poem} does not exist.")
        sys.exit(1)

    with open(poem, "rt") as data:
        lines = data.readlines()
        for count, line in enumerate(lines, start=1):
            tone_map = ping_ze(line.strip())
            print(f"{count}\t{line.strip()}\t{tone_map}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('poem', type=Path, help='file path')
    args = parser.parse_args()
    
    analyze_prosody(args.poem)


if __name__ == "__main__":
    main()

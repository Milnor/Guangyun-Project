![GuangYun](https://user-images.githubusercontent.com/7789866/115130190-60ffa700-9fbb-11eb-92ac-fd2dd0d2b5e6.png)

# Guangyun-Project
automate textual analysis using the Guangyun rhyme dictionary

## What is the Guangyun?

The **Guangyun** (廣韻) is a Song dynasty rhyme dictionary compiled ca. 1000 CE. It was based on an earlier work, the **Qieyun** (切韻, ca. 600 CE). Though originally a tool for literati poets, rhyme dictionaries are useful for modern linguists in reconstructing the sound system of Middle Chinese. See also 
(Guangyun) [https://en.wikipedia.org/wiki/Guangyun] on Wikipedia.

## Where is this project going?

At this point, it consists of a couple proof-of-concept Python scripts that load the Guangyun into memory and will (when complete) automate the analysis of tonal distribution and rhyme of an arbitrary input text. It assumes, of course, that the input is pentasyllabic or septasyllabic Chinese metered verse.

Here is a sample output of the current work-in-progress:
```
$ ./ping_ze_poc.py test_inputs/libai.txt 
0001 	床前明月光 	平平平仄平
0002 	疑是地上霜 	平仄仄仄平
0003 	舉頭望明月 	仄平平平仄
0004 	低頭思故鄉 	平平平仄平
```

The goal is to create something that is user friendly and reliable enough for serious work by professors and grad students.

**Possible Future Directions**
* Python library, to maximize flexibility for users who code
* Windows executable, to minimize required technical expertise

## Upcoming TODOs (as of 10 Feb 2023)
* [ ] add tests for tonal distribution
* [ ] add tests for rhyme
    * [ ] strict, by rhyme group
    * [ ] distinguish du yong vs. tong yong
* [ ] add *fanqie* to parsing
* [x] find reliable, large dataset
    * [cjkvi-dict](https://github.com/cjkvi/cjkvi-dict/) is licensed GPLv2
    * provenance appears to be https://kanji-database.sourceforge.net/
<!--
## Misc

Notes to self: upgrading pip and installing cihai...

```
python3 -m pip install --upgrade pip
```
```
python3 -m pip install --user cihai
```
-->

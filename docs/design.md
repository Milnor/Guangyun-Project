# Design

## Motivation

I began this project years ago. Now I'm a better Python developer. It's time to
gut the repo and build back better.

A Python `dict` is easily robust enough to store a rhyme dictionary; however,
since the API requires non-trivial search functionality, we'll use real OOP and
build out a class with appropriate methods.

## Class Design

```mermaid
---
title: UML Plan for the Guang Yun
---
classDiagram
    RhymeDictionary <-- Volume
    Volume <-- RhymeGroup
    RhymeGroup <-- HomophoneGroup
    class RhymeDictionary{
        note "Storage container for all five volumes"
        -list Volumes
        +stats()
        +lookup()
    }
    class Volume{
        -list RhymeGroups
        +stats()
        -lookup()
    }
    class RhymeGroup{
        -str or None tongyong
        -list HomophoneGroups
        -lookup()
    }
    class HomophoneGroup{
        -str fanqie
        -set members
        +stats()
        -lookup()
    }
```

## UI

### CLI based, at least for starters

* Optional arguments
  * `-v` control verbosity of logging
  * `-zh` Chinese output

### Future

Potentially add interactive command interface with cmd.Cmd... or even a GUI.

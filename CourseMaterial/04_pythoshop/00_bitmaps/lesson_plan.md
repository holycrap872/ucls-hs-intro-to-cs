## Essential Questions

- What properties do files need in order to be run by computers?
- What are Bitmaps are what kind of data do they store?

## Lesson Plan

In this lesson, students use Hex Fiend to manipulate BitMaps. The goal is to
show them how real data requires very strict formatting rules. In addition,
it provides the opportunity to discuss the importance of abstraction and
functions; in some future lesson we can use the debugger to see the actions
they're exploring be used in the PythoShop software.

> Note: This class doesn't have to be the first class of the PythoShop unit.
  It can be put pretty much anywhere (during a long block) and framed as a
  "looking under the hood" / de-abstraction lesson.

### Setup

- `BitMap Manual Editing Worksheet` loaded up on Schoology
    - https://docs.google.com/document/d/1ZvwvCIIadERbB6w8pEogAD431598T8ARJezJt5OjL3Q
- `simple.bmp` loaded up on Schoology

### Actual Lesson

- Review
    - VSCode
    - Turbozzle
    - Functions
- Today, going way back to pictures
    - What do we remember about pictures?
    - BitPic data
        - 1-bit pictures
        - 1, 0 -> black/white
    - EmojiPic data
        - 3-bit pictures
        - RGB, yellow, cyan, magenta, white, black
- BitMaps
    - Real file format
    - Uncompressed
    - RGB values stored throughout
- Hex Fiend refresher
    - Put in `Overwrite Mode`
    - Put left side into decimal mode
    - Show how to find particular bytes
        - Count manually
        - Look at bottom
    - Change random pixel to be a random color
- Interacting with `simple.bmp`
    - Put on `Desktop`
    - Right click to get to "Get Info"
    - Right click to get to `Preview`
    - Right click to get to `Hex Fiend`
- `BitMap Manual Editing Worksheet`
    - Walk through first problem
    - Explain that can use hex -> decimal and decimal -> hex converter
    - As a class, put Hex Fiend in OVERWRITE MODE!!!!
        - Raise your hand if you see it at the top
- Debrief
    - What is the stuff before the actual data?
        - "metadata"
    - Answer other questions

### Homework

- TIL entry on what "metadata" in a file is used for

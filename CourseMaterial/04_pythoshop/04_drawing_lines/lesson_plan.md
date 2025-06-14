## Essential Questions

- How can I use Python to edit images?
- How do I use loops to change many pixels at once?

## Lesson Plan

### Setup

- Have `reflective_symmetry` PythoShop tool coded and ready to go
    ```python
    @export_tool
    def do_something(image, clicked_coordinate, color, **kwargs):
        height = get_height(image) - 1
        width = get_width(image) - 1
        x, y = clicked_coordinate
        set_pixel_rgb(image, (x, y), color)
        set_pixel_rgb(image, (width - x, y), color)
        set_pixel_rgb(image, (x, height - y), color)
        set_pixel_rgb(image, (width - x, height - y), color)
    ```
- `Drawing Lines Worksheet` loaded up in Schoology
    - https://docs.google.com/document/d/1wijKCu1sCK8tCembiKr5q3JuGVCXh5LgpYa_k9Daz2c
- `Changing Pixel Parts Worksheet` loaded up in Schoology (just in case)
    - https://docs.google.com/document/d/1uXbiT-LXxW9RWpdDqQPeNiizP-wa0hThpcdDe1A90_I
- `loops.py` ready for demo

### Actual Lesson

- Review
    - PRIMM of `reflective_symmetry`
    - How to run
    - Tools vs. filters
    - Set/get pixel
- Loops in PythoShop
    - Why loops useful?
    - Show `loops.py`
- Class filter
    - Create a picture half-filled with a given color
    - First do bottom-half filled with color
    - Then do top-half filled with color
    - Use debugger to show it working step by step
        - Reemphasize how important understanding debugger is
        - I will ask "did you debug it" before I help you
- Reframe grading
    - Do the extensions you like
    - Move on if don't like/get it
    - This is confusing for the students, so take time here
- Start assignment

### Homework

- Finish `Drawing Lines Worksheet`

### Possible Extensions

- Various teachers in use GoogleDocs to automatically get/greade students work
    - I find it more trouble than it's worth
    - If you do want to do this then:
    - Before end of class, have students:
        - Create GoogleDrive folder via website
        - Share folder with me
        - Close out out `vscode`
        - Log into GoogleDrive on Desktop/laptop
        - Navigate to new folder in GoogleDrive
        - Drag `PythoShop` to GoogleDrive folder
        - Reopen `vscode` from that location 

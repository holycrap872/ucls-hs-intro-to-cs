## Essential Questions

- How can I use python to edit images?
- How do I prepare myself for a long term CS project?

## Lesson Plan

### Setup

- Have `four_corners` PythoShop filter coded and ready to go
    ```python
    @export_filter
    def do_something(image, color, **kwargs):
        width = get_width(image)
        height = get_height(image)
        set_pixel_rgb(image, (0, 0), color)
        set_pixel_rgb(image, (width - 1, 0), color)
        set_pixel_rgb(image, (0, height - 1), color)
        set_pixel_rgb(image, (width - 1, height - 1), color)
    ```
- `Change Multiple Pixels Worksheet` loaded up in Schoology
    - https://docs.google.com/document/d/1HLtrNlvG8lK3hfLYP8F_Riwv06pI9ktlbIk8dypn5ds
- `Drawing Lines Worksheet` loaded up in Schoology (just in case)
    - https://docs.google.com/document/d/1kv9eGOh2T1Kr3K7YNIEm_U7-RmefU2ErWha9lOEuQKQ

### Actual Lesson

- Review
    - PRIMM of `four_corners`
    - PythoShop
    - Tools vs. filters
    - Helper functions
    - How to run PythoShop
- Class filter
    - Yellow line along bottom row
- Minutia
    - Reemphasize grading
    - Cheating
        - Will get caught
        - Variable changes get caught by "abstract syntax trees"
            - Show Wikipedia article
            - https://observablehq.com/@aarebecca/ast-explorer with simple example
            - https://astexplorer.net/
                - Choose `Python`
        - Honestly a little hard to detect in the beginning with small programs
        - People always get caught at the end when functions get harder
        - Just work hard in class and won't have to worry about it
- Show assignment
    - Talk through it
    - How to set background to a particular picture
        - Change `config.py`
        - Requires overwrite
- Go!

### Homework

- Finish `Change Multiple Pixels Worksheet`
- TIL entry on `get_width()` / `get_height()` helper functions

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
    - https://docs.google.com/document/d/1xbOrwUMz_48eGLWHmHnraCnf2AQEE11Qt9aEErpWM5c
- `Drawing Lines Worksheet` loaded up in Schoology (just in case)
    - https://docs.google.com/document/d/1wijKCu1sCK8tCembiKr5q3JuGVCXh5LgpYa_k9Daz2c
- AST Websites open
    - https://en.wikipedia.org/wiki/Abstract_syntax_tree
    - https://observablehq.com/@aarebecca/ast-explorer

### Actual Lesson

- Review
    - PRIMM of `four_corners`
    - PythoShop
    - Tools vs. filters
    - Helper functions
    - How to run PythoShop
- Class filter
    - Yellow _line_ along bottom row
    - Don't add any width to it for now
- Grading minutia
    - Remphasize and acknowledge it's confusing
    - Do the extensions you like
    - Move on if don't like/get it
    - This is confusing for the students, so take time here
- Cheating (delay until next class if not long block)
    - Will get caught
    - Variable changes get caught by "abstract syntax trees"
        - https://en.wikipedia.org/wiki/Abstract_syntax_tree
        - https://observablehq.com/@aarebecca/ast-explorer with simple example
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
- TIL entry on `get_width()` and `get_height()` helper functions

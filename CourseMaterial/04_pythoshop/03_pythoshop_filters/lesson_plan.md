## Essential Questions

- How can I use python to edit images?
- How do I prepare myself for a long term CS project?

## Lesson Plan

### Setup

- Have `four_corners` filter coded and ready to go
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
    - Tools vs. Filters
    - Helper functions
    - How to run PythoShop
- Class tool
    - Create a class tool to create an `X` wherever the user clicks
    - Why a tool and not a filter?
    - Figure it out together
- Minutia
    - Testing
        - Don't have to worry about it now
        - Will show you in next few classes how tests get run
        - Eventually move to GoogleDrive so I can auto-grade everything
    - Cheating
        - Will get caught
        - Variable changes get caught by "abstract syntax trees"
            - Show wikipedia article
            - https://observablehq.com/@aarebecca/ast-explorer with simple example
            - https://astexplorer.net/
                - Choose python
        - Honestly a little hard to detect in the beginning with small programs
        - People always get caught at the end when functions get harder
        - Just work hard in class and won't have to worry about it
    - Extra credit
- Show assignment
    - Talk through
- Go!

### Homework

- Finish `Change a Pixel` worksheet
- TIL entry on topic of your choice

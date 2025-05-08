## Essential Questions

- How can I use python to edit images?
- How do I prepare myself for a long term CS project?

## Lesson Plan

### Setup

- Have `bottom_l_pixels` tool coded and ready to go
    ```python
    @export_tool
    def do_something(image, clicked_coordinate, **kwargs):
        set_pixel_rgb(image, (0, 0), (255, 0, 0))
        set_pixel_rgb(image, (1, 0), (0, 255, 0))
        set_pixel_rgb(image, (2, 0), (0, 0, 255))
        set_pixel_rgb(image, (0, 1), (0, 255, 255))
        set_pixel_rgb(image, (0, 2), (255, 255, 255))
    ```
- `Change a Pixel Worksheet` loaded up in Schoology
    - https://docs.google.com/document/d/1vai-0xjDI6uLtVG7dGk1mcJOQsknVRocFFkGs8LMb7A
- `Change Multiple Pixels Worksheet` loaded up in Schoology (just in case)
    - https://docs.google.com/document/d/1HLtrNlvG8lK3hfLYP8F_Riwv06pI9ktlbIk8dypn5ds

### Actual Lesson

- Review
    - PRIMM of `bottom_l_pixels`
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
        - Start at a B
        - 85 points to get to an A+
- Show assignment
    - Talk through
- Go!

### Homework

- Finish `Change a Pixel` worksheet
- TIL entry on `set_pixel_rgb()` helper function

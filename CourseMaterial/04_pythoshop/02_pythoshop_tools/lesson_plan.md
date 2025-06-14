## Essential Questions

- How can I use Python to edit images?
- How do I prepare myself for a long term CS project?

## Lesson Plan

### Setup

- Have `bottom_l_pixels` PythoShop tool coded and ready to go
    ```python
    @export_tool
    def do_something(image, clicked_coordinate, color, **kwargs):
        set_pixel_rgb(image, (0, 0), (255, 0, 0))
        set_pixel_rgb(image, (1, 0), (0, 255, 0))
        set_pixel_rgb(image, (2, 0), (0, 0, 255))
        set_pixel_rgb(image, (0, 1), (0, 255, 255))
        set_pixel_rgb(image, (0, 2), (255, 255, 255))

        h = get_height(image)
        set_pixel_rgb(image, (0, h - 1), (0, 0, 0))
    ```
- `Change a Pixel Worksheet` loaded up in Schoology
    - https://docs.google.com/document/d/1LGuQQPHvYpMwVn269lRUtp7xrQAV-5hhj4m443Yi9n0
- `Change Multiple Pixels Worksheet` loaded up in Schoology (just in case)
    - https://docs.google.com/document/d/1xbOrwUMz_48eGLWHmHnraCnf2AQEE11Qt9aEErpWM5c

### Actual Lesson

- Review
    - PRIMM of `bottom_l_pixels`
        - Why are `clicked_coordinate` and `color` greyed out?
    - PythoShop
    - Tools vs. Filters
    - Helper functions
    - How to run PythoShop
- Class tool
    - Create a class tool to create an `X` wherever the user clicks
    - Why a tool and not a filter?
    - Figure it out together
- Grading minutia
    - Extensions
        - If finish all expected requirements (87)
        - 40 pts of extensions -> 91
        - 80 pts of extensions -> 96
        - 120 pts of extensions -> 100
    - Do the extensions you like
    - Move on if don't like/get it
    - This is confusing for the students, so take time here
- Show assignment
    - Talk through it
- Go!

### Homework

- Finish `Change a Pixel Worksheet`
- TIL entry on `set_pixel_rgb()` helper function

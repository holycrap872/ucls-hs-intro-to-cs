## Essential Questions

- How can I use python to edit images?

## Lesson Plan

### Setup

- Have `quarter_image` filter coded and ready to go
    ```python
    @export_filter
    def do_something(image, color, **kwargs):
        width = get_width(image)
        mid_width = width // 2
        height = get_height(image)
        mid_height = height // 2

        for x in range(0, mid_width):
            for y in range(0, mid_height):
                r, g, b = get_pixel_rgb(image, (x, y))
                set_pixel_rgb(image, (x, y), (r, 0, 0))

        for x in range(mid_width, width):
            for y in range(0, mid_height):
                r, g, b = get_pixel_rgb(image, (x, y))
                set_pixel_rgb(image, (x, y), (0, g, 0))

        for x in range(0, mid_width):
            for y in range(mid_width, height):
                r, g, b = get_pixel_rgb(image, (x, y))
                set_pixel_rgb(image, (x, y), (0, 0, b))
    ```
- `Conditional Modifications Worksheet` loaded up in Schoology
    - https://docs.google.com/document/d/1E3v36HUh18ogVqMij1zDeYAKccBm6d_4fSuFeeACrlc
- `Blending Pictures Worksheet` loaded up in Schoology (just in case)
    - https://docs.google.com/document/d/16Ojx0zLR8qMaISlor8awAbqrqwX1n94_QZEQiyfUnLw

### Actual Lesson

- Review
    - PRIMM of `quarter_image`
        - Intentional bug... can you find it?
        - Show `extra` field in PythoShop GUI
            - **Breakpoint** to show that it passes value through
        - How could we use `extra` here?
            - Replace 0's with set value
    - How to identify loops?
- Class filter:
    - 45 degree line moving up and right: `color`
    - 45 degree line moving up and left: `extra`
- Get started on assignment

### Homework

- Finish `Conditional Modifications Worksheet`

## Essential Questions

- How can I use python to edit images?
- How do I take in "extra" input and use it?

## Lesson Plan

### Setup

- Have `rotate_colors` filter coded and ready to go
    ```
    @export_filter
    def do_something(image, color, **kwargs):
        height = get_height(image)
        width = get_width(image)

        for x in range(width):
            for y in range(height):
                r, g, b = get_pixel_rgb(image, (x, y))
                set_pixel_rgb(image, (x, y), (g, b, r))
    ```
- Fourth assignment loaded up in Schoology
    - `03_drawing_lines`

### Actual Lesson

- Review
    - PRIMM of `rotate_colors`
    - PythoShop
    - Tools vs. Filters
    - Helper functions
- Class filter
    - Create a class filter to draw a border around an image
        - Start with width 1
        - Work up to using `extra`
    - Why a filter and not a tool?
    - Figure it out together
- Show assignment
    - Talk through
- Go!

### Homework

- None

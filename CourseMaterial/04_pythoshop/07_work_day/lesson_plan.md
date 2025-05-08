## Essential Questions

- How can I use python to edit images?

## Lesson Plan

### Setup

- Have `quarter_image` filter coded and ready to go
    ```
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
- Sixth assignment loaded up in Schoology
    - `05_changing_pixels_based_on_values`

### Actual Lesson

- Review
    - PRIMM of `make_light_black`
        - How could we use `extra` here?
    - How to identify loops?
    - ...
- Class filter: random walk
    - Figure it out together
    - Why `while` loop?
    - When should it stop?
- Get start on assignment

## Essential Questions

- How can I use python to edit images?
- How do I visualize loops so I can easily detect when they're useful?

## Lesson Plan

### Setup

- Have `make_light_black` filter coded and ready to go
    ```
    @export_filter
    def do_something(image, color, **kwargs):
        height = get_height(image)
        width = get_width(image)

        for x in range(width):
            for y in range(height):
                r, g, b = get_pixel_rgb(image, (x, y))
                if r + g + b > 700:
                    set_pixel_rgb(image, (x, y), (0, 0, 0))
    ```
- Fifth assignment loaded up in Schoology
    - `04_changing_parts_of_pixels`

### Actual Lesson

- Review
    - PRIMM of `make_light_black`
        - How could we use `extra` here?
    - Functions
    - Filters
    - ...
- How to identify loops?
    - Find starting point
    - Plot out several next steps
    - Create loop
- Create filter that does bottom left corner up at 45 degrees
    - First pixels coordinates?
    - What's next (do 3-4 times)
    - What's the loop
- Create filter that draws line where use clicked
    - First pixels coordinates?
    - What's next (do 3-4 times)
    - What's the loop
- Start assignment

### Homework

- None

## Essential Questions

- How can I use python to edit images?
- How do I visualize loops so I can detect when they're useful?

## Lesson Plan

### Setup

- Have `make_light_black` filter coded and ready to go
    ```python
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
- `Value Based Changes Worksheet` loaded up in Schoology
    - https://docs.google.com/document/d/1qHopc_4zF7gBwDq1mNek4pfs8pqFPa32jo2Nk7IMQHE
- `Conditional Modifications Worksheet` loaded up in Schoology (just in case)
    - https://docs.google.com/document/d/1i1K_0L-XeLQaoK2A_rpamfJCfCU8Gf279b7Lblk4Qto

### Actual Lesson

- Review
    - PRIMM of `make_light_black`
        - Do for 700, then 500, then 300
    - Functions
    - Filters
    - Use break and examine values
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

- Finish `Value Based Changes Worksheet`

## Essential Questions

- How can I use Python to edit images?
- How do I get and set the values of particular pixels?

## Lesson Plan

### Setup

- Have `first_to_all` PythoShop filter coded and ready to go
    ```python
    @export_filter
    def do_something(image, color, **kwargs):
        height = get_height(image)
        width = get_width(image)

        r, g, b = get_pixel_rgb(image, (0, 0))
        for x in range(width):
            for y in range(height):
                set_pixel_rgb(image, (x, y), (r, g, b))
    ```
- `Pixel Parts Worksheet` loaded up in Schoology
    - https://docs.google.com/document/d/1uXbiT-LXxW9RWpdDqQPeNiizP-wa0hThpcdDe1A90_I
- `Value Based Changes Worksheet` loaded up in Schoology (just in case)
    - https://docs.google.com/document/d/1b-_Eq48VScdFNqXwF3JEXckwO5AoHbu4r5UPynUX7JQ


### Actual Lesson

- PRIMM of `first_to_all`
    - What does it do?
    - What if put `get_pixel_rgb(image, (x, y))` inside loop?
    - What if did `width // 2`?
    - What if did `(g, b, r)`
- Review
    - PythoShop
    - Tools vs. Filters
    - Helper functions
- Class filter
    - Bottom left red channel
    - Bottom right blue channel
- Show assignment
    - Talk through
- Go!

### Homework

- Finish `Pixel Parts Worksheet`

## Essential Questions

- How can I use python to edit images?

## Lesson Plan

### Setup

- Have `side_by_side` filter coded and ready to go
    ```python
    @export_filter
    def do_something(image, other_image, color, extra, **kwargs):
        h = get_height(image)
        w1 = get_width(image)
        w2 = get_width(other_image)

        new_image = create_bmp(w1 + w2, h)

        for x in range(w1):
            for y in range(h):
                r, g, b = get_pixel_rgb(image, (x, y))
                set_pixel_rgb(new_image, (x, y), (r, g, b))

        for x in range(w1):
            for y in range(h):
                r, g, b = get_pixel_rgb(other_image, (x, y))
                set_pixel_rgb(new_image, (w1 + x, y), (r, g, b))

        return new_image
    ```
- `Pixel Positions Worksheet` loading up in Schoology
    - https://docs.google.com/document/d/165RAbgEFPmXiVjfx0JV7hHfMXBaBbA-7KXSoFgDGc20

### Actual Lesson

- Review
    - PythoShop so far
    - How feel about it?
- Today going to do something a little weird:
    - Going to dive into helper functions
    - Provide justification for them
- Talk about abstraction
    - What is abstraction?
    - Show functions that I provided
        - Why good?
        - Compare with code without functions
        - Why better?
- Phrase in CS: only two hard things, caching and naming
    - Philosophical endeavor
    - How do you cut problems so easy to think about
- Do art exercise
- Programming as art AND engineering
    - Art is finding space where human's intuitively engage with concepts
        - function naming
    - Engineering is filling in the details and making it work well
        - function code writing

### Homework

- Finish `Pixel Positions Worksheet`

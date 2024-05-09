## Essential Questions

- How can I use python to edit images?
- What is a debugger and how do I use it?

## Lesson Plan

### Setup

- Have `cross_wise_lines` filter coded and ready to go
    ```
    @export_filter
    def do_something(image, color, **kwargs):
        width = get_width(image)
        height = get_height(image)

        for x in range(0, width, 30):
            for y in range(0, height):
                set_pixel_rgb(image, (x, y), (0, 0, 0))

        for y in range(0, height, 30):
            for x in range(0, width):
                set_pixel_rgb(image, (x, y), (0, 0, 0))
    ```
- Seventh assignment loaded up in Schoology
    - `06_conditional_modifications`

### Actual Lesson

- Review
    - PRIMM of `cross_wise_lines`
    - What's been hard?
- Today going to talk about debugging
    - What is debugging?
    - Show original computer bug
        - Found by Grace Hopper on Harvard Mark II
        - Show picture of both bug and Harvard Mark II
    - What are debugging techniques we've seen before?
        - `print`
        - Ask Mr. Rizzi
        - Read code carefully
- Now going to learn python debugger
    - Allows you to pause a program and see what's going on
    - Show various commmands
        - next, step into, continue, ...
    - Run program and step into `get_height({)`
        - Show call stack
        - Show variable values
    - When might this have been useful?
- Emphasize how powerful this is
    - If take enough time, can figure out anything
    - Most of the reason I succeeded is I was willing to keep debugging
- Back to PythoShop

## Essential Questions

- How can I use python to edit images?
- What is a debugger and how do I use it?

## Lesson Plan

### Setup

- Have `count_color` filter coded and ready to go
    ```python
    @export_filter
    def do_something(image, color, extra, **kwargs):
        w = get_width(image)
        h = get_height(image)

        acc_r = 0
        acc_g = 0
        acc_b = 0

        for y in range(h):
            for x in range(w):
                r, g, b = get_pixel_rgb(image, (x, y))
                acc_r = acc_r + r
                acc_g = acc_g + g
                acc_b = acc_b + b

        if acc_r > acc_g and acc_r > acc_b:
            c = (255, 0, 0)
        elif acc_g > acc_b:
            c = (0, 255, 0)
        else:
            c = (0, 0, 255)

        for x in range(w):
            for y in range(h):
                set_pixel_rgb(image, (x, y), c)
    ```
- `Blending Pictures Worksheet` loaded up in Schoology
    - https://docs.google.com/document/d/16v8pJ_XwWuXVoKElX4S1r91-ELbhgBXlVNmu23_AKio
- `Pixel Positions Worksheet` loaded up in Schoology (just in case)
    - https://docs.google.com/document/d/165RAbgEFPmXiVjfx0JV7hHfMXBaBbA-7KXSoFgDGc20

### Actual Lesson

- Opening Problem
    - PRIMM of `count_color`
        - Problem because loops slightly different?
    - Test with various images
        - Have guess what final color will be
        - What happens if get perfectly white image?
- Review
    - What's been hard?
    - Things to remember?
- `create_bmp`
    - Why exists
    - Importance of return
- Class filter
    - Split images
    - Half from `image`, have from `other_image`
    - Questions?
- Plan going forward
    - Work day today
    - One more worksheet next class
    - Work day and "fix up" day
    - Project due end of day Wednesday
- Get started on assignment

### Homework

- Finish `Blending Pictures Worksheet`

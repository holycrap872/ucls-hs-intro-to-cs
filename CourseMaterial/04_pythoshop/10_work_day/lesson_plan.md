## Essential Questions

- How can I use python to edit images?

## Lesson Plan

### Setup

- Have `weird_gradient` filter coded and ready to go
    ```python
    @export_filter
    def do_something1(image, color, extra, **kwargs):
        h = get_height(image)
        w = get_width(image)

        acc = 0
        for x in range(w):
            for y in range(h):
                set_pixel_rgb(image, (x, y), (acc, acc, acc))
                acc += 1

                if acc > 255:
                    acc = 0

    ```

### Actual Lesson

- Review
    - PRIMM `weird_gradient`
        - What is first loop doing?
        - What is second loop doing?
        - Pay attention, you will use something like this today
- Discuss blending via example that is "close"
    ```python
    @export_filter
    def blend_channels(image, other_image, color, extra, **kwargs):
        width = get_width(image)
        height = get_height(image)

        blended_image = create_bmp(width, height)
        for x in range(width):
            for y in range(0, height):
                r1, g1, b1 = get_pixel_rgb(image, (x, y))
                r2, g2, b2 = get_pixel_rgb(other_image, (x, y))

                set_pixel_rgb(blended_image, (x, y), (r1, g2, 0))

        return blended_image
    ```
    - Talk about `other_image` parameter
    - Talk about `create_bmp`
    - Compare `image`, `other_image`, and `blended_image`
- Both are important for today
    - Look in slides for `max_color`
    - I'll leave `blend_channels` up here
- Go!

### Homework

- Work on project

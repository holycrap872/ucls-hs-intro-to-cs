## Essential Questions

- How can I use python to edit images?

## Lesson Plan

### Setup

- Have `flip_vertical` filter coded and ready to go
    ```
    @export_filter
    def do_something(image, color, extra, **kwargs):
        width = get_width(image)
        height = get_height(image)

        new_image = create_bmp(width, height)

        for x in range(width):
            for y in range(height):
                r, g, b = get_pixel_rgb(image, (x, y))
                set_pixel_rgb(new_image, (x, (height - y) - 1), (r, g, b))

        return new_image
    ```

### Actual Lesson

- Review
    - PRIMM `flip_vertical`
    - RGB in color vs RGB in grayscale
- Schedule for the rest of the year
- Debrief on 
    - Go to old one (`blending_images`) and talk about it
    - What was easy, what was hard?
    - Difference between `(r1 + r2 / 2)` and `((r1 + r2) / 2)`
- Remind that have CS help on lunch, Wednesdays
- Go!
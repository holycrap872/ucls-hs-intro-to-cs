## Essential Questions

- How can I use python to edit images?

## Lesson Plan

### Setup

- Have `most_color` filter coded and ready to go
    ```
    @export_filter
    def do_something(image, color, extra, **kwargs):
        width = get_width(image)
        height = get_height(image)

        total_r = 0
        total_g = 0
        total_b = 0
        for x in range(width):
            for y in range(0, height):
                r, g, b = get_pixel_rgb(image, (x, y))
                total_r = total_r + r
                total_g = total_g + g
                total_b = total_b + b

        if total_r >= total_g and total_r >= total_b:
            c = (255, 0, 0)
        elif total_g >= total_r and total_g >= total_b:
            c = (0, 255, 0)
        else:
            c = (0, 0, 255)

        print("Printing color:", c)
        for y in range(height):
            for x in range(0, width):
                set_pixel_rgb(image, (x, y), c)
    ```
- Seventh assignment loaded up in Schoology
    - `07_blending_pictures`

### Actual Lesson

- Review
    - PRIMM `most_color`
        - What is first loop doing?
        - What is second loop doing?
        - Pay attention, you will use something like this today
- Discuss blending via example that is "close"
    ```
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

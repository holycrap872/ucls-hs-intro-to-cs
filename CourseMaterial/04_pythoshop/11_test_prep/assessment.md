0. What would be the best name for the following filter?
    ```python
    @export_filter
    def do_something(image, color, **kwargs):
        h = get_height(image)
        w = get_width(image)
        set_pixel_rgb(image, (0, 0), color)
        set_pixel_rgb(image, (0, h-1), color)
        set_pixel_rgb(image, (w-1, 0), color)
        set_pixel_rgb(image, (w-1, h-1), color)
    ```
    - draw_t
    - mark_middle_with_x
    - draw_hline
    - mark_four_corners
1. What would be the best name for the following filter:
    ```python
    @export_filter
    def darken(image, color, extra, **kwargs):
        w = get_width(image)
        h = get_height(image)

        for x in range(w):
            for y in range(h):
                r, g, b = get_pixel_rgb(image, (x, y))
                new_r = int(r / 2)
                new_g = int(g / 2)
                new_b = int(b / 2)

                set_pixel_rgb(image, (x, y), (new_r, new_g, new_b))
    ```
    - darken
    - intensify
    - swap_rgb
    - flip_vertical
2. The following filter has a subtle bug. It is supposed to make images look like
   the one on the left, but instead it makes images look like the one on the right.
   What mistake did the programmer make?
    ```python
    @export_filter
    def make_two_tone(image, color, **kwargs):
        w= get_width(image)
        h= get_height(image)

        for x in range(w):
            for y in range(h):
                r, g, b = get_pixel_rgb(image, (x, y))
                avg = (r + g + b) / 3
                if avg < 127.5:
                    r, g, b = 255, 255, 255
                else:
                    r, g, b = 0, 0, 0

                set_pixel_rgb(image, (x, y), (r, g, b))
    ```
    - The `else` should have a condition in it
    - You first need to call `set_pixel_rgb()` before you can call `get_pixel_rgb()`
    - The condition in the `if`statement should be a `>`
    - The RGB values shouldn't all be equal
    - The required `extra` input isn't present
3. Which of the following would change the top left pixel of an image to the color red?
    - `set_pixel_rgb(image, (width - 1, height - 1), (255, 0, 0))`
    - `set_pixel_rgb(image, (0, height - 1), (255, 0, 0))`
    - `set_pixel_rgb(image, (0, 0), (255, 0, 0))`
    - `set_pixel_rgb(image, (0, height), (255, 0, 0))`
    - `set_pixel_rgb(image, (height, width - 1), (0, 0, 255))`
4. Match the following code snippets with their effects:
    - Column A:
        - ```python
            for x in range(w):
                for y in range(h):
                    set_pixel_rgb(image, (x, y), (0, 0, 0)
            ```
        - ```python
            set_pixel_rgb(image, (0, 0), (0, 0, 0)
            ```
        - ```python
            for x in range(w):
                set_pixel_rgb(image, (x, 0), (0, 0, 0)
            ```

        - ```python
            for y in range(h):
                set_pixel_rgb(image, (0, y), (0, 0, 0)
            ```

    - Column B:
        - Make every pixel in an image black
        - Make a vertical line of pixels in an image black
        - Make a single pixel in an image black
        - Make a horizontal line of pixels in an image black
5. The minimum value a color in an RGB "tuple" can be is _ and the maximum value
   is _. When all three numbers are their minimum value you get the color _ and
   when all three numbers are their maximum value you get the color _.
6. Why are the `if r > 255:`, `if g > 255:`, and `if b > 255:` statements necessary
   in the following snippet of code:
    ```python
    @export_filter
    def lighten(image, color, **kwargs):
        width = get_width(image)
        height = get_height(image)
        for y in range(height):
            for x in range(width):
                r, g, b = get_pixel_rgb(image, (x, y))
                r = int(r * 1.5)
                if r > 255:
                    r = 255

                g = int(g * 1.5)
                if g > 255:
                    g = 255

                b = int(b * 1.5)
                if b > 255:
                    b = 255

                set_pixel_rgb(image, (x, y), (r, g, b))
    ```
    - Because multiplication could make values go above the max RGB value
    - Because colors that are equal result in a gray scale image
    - Because no pixel should be completely white during lightening
    - To make all of the colors equal to have a well balanced image
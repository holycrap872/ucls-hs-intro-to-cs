## Lesson Plan

### Setup

- Have `reflective_symmetry` tool coded and ready to go
    ```
    @export_tool
    def do_something(image, clicked_coordinate, color, **kwargs):
        height = get_height(image) - 1
        width = get_width(image) - 1
        x, y = clicked_coordinate
        set_pixel_rgb(image, (x, y), color)
        set_pixel_rgb(image, (width - x, y), color)
        set_pixel_rgb(image, (x, height - y), color)
        set_pixel_rgb(image, (width - x, height - y), color)

    ```
- Fourth assignment loaded up in Schoology
    - Drawing lines

### Actual Lesson

- Review
    - How to run
    - Tools vs. filters
    - Set/get pixel
    - PRIMM of `reflective_symmetry`
- Loops in PythoShop
    - Why loops useful?
    - Create a border filter as a class
        - First do one pixel border than multi-pixel border
- Start assignment
- Before end of class, have students:
    - Create GoogleDrive folder via website
    - Share folder with me
    - Close out out `vscode`
    - Log into GoogleDrive on Desktop/laptop
    - Navigate to new folder in GoogleDrive
    - Drag PythoShop to GoogleDrive folder
    - Reopen `vscode` from that location 

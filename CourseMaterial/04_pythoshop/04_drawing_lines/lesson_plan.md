## Essential Questions

- How can I use python to edit images?
- How do I effectively share my work with myself and others?

## Lesson Plan

### Setup

- Have `reflective_symmetry` tool coded and ready to go
    ```python
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
- `Drawing Lines Worksheet` loaded up in Schoology
    - https://docs.google.com/document/d/1kv9eGOh2T1Kr3K7YNIEm_U7-RmefU2ErWha9lOEuQKQ
- `Changing Pixel Parts Worksheet` loaded up in Schoology (just in case)
    - https://docs.google.com/document/d/1S8WVgXGo02PCV_ldPlcWhPZB8NezWh2wP-ahVrTVwZo

### Actual Lesson

- Review
    - PRIMM of `reflective_symmetry`
    - How to run
    - Tools vs. filters
    - Set/get pixel
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
    - Drag `PythoShop` to GoogleDrive folder
    - Reopen `vscode` from that location 

### Homework

- None
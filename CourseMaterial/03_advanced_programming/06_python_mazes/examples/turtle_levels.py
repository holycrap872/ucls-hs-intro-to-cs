LEVEL_0 = [
    ["x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x"],
    ["g", "b", "b", "b", "b", "b", "b", "y"],
    ["x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x"],
]
COLOR_MAPPING = {
    "g": "green",
    "x": "black",
    "b": "blue",
    "y": "yellow",
    "r": "red",
}


def get_color(color_code: str) -> str:
    return COLOR_MAPPING[color_code]


FILE_TO_LEVEL_MAP = {
    "maze_0.png": LEVEL_0,
}

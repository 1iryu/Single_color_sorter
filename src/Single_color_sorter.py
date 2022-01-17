import math
from Vector3 import Vector3

colors = {
    "BlACK": "0, 0, 0",
    "RED": "255, 0, 0",
    "GREEN": "0, 128, 0",
    "YELLOW": "255, 255, 0",
    "BLUE": "0, 0, 255",
    "MAGENTA": "255, 0, 255",
    "CYAN": "0, 255, 255",
    "WHITE": "255, 255, 255"
}


def check_distance_by_vector(v1, v2):
    dx = v1.x - v2.x
    dy = v1.y - v2.y
    dz = v1.z - v2.z

    return math.sqrt(dx * dx + dy * dy + dz * dz)


def find_color(rgb_value: Vector3):
    color_name = ""
    most_close_distance = 10000
    for name, rgb in colors.items():
        distance = check_distance_by_vector(rgb_value,Vector3(rgb))
        if(most_close_distance >= distance):
            most_close_distance = distance
            color_name = name

    return color_name


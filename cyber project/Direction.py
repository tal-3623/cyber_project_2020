import enum

x = 0
y = 1


class Rect:
    def __init__(self, rect):
        self.top_right = rect.topright
        self.top_left = rect.topleft
        self.bottom_left = rect.bottomleft
        self.bottom_right = rect.bottomright


class Direction(enum.Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3
    NONE = 4


def get_collision_direction(my_rect: Rect, other_rect: Rect):
    x_right_diff = abs(my_rect.top_right[x] - other_rect.bottom_left[x])
    x_left_diff = abs(my_rect.bottom_left[x] - other_rect.top_right[x])
    y_up_diff = abs((my_rect.top_right[y] - other_rect.bottom_left[y]))
    y_down_diff = abs((my_rect.bottom_left[y] - other_rect.top_right[y]))
    m = min(x_right_diff, x_left_diff, y_up_diff, y_down_diff)
    if m == x_right_diff:
        direction = Direction.RIGHT
    elif m == x_left_diff:
        direction = Direction.LEFT
    elif m == y_up_diff:
        direction = Direction.UP
    else:
        direction = Direction.DOWN
    return direction, m

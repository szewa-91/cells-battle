SIZE_MULTIPLIER = 10


def to_screen_pos(val):
    if isinstance(val, tuple):
        return int(val[0] // SIZE_MULTIPLIER), int(val[1] // SIZE_MULTIPLIER)
    if isinstance(val, int):
        return int(val / SIZE_MULTIPLIER)


def to_game_pos(val):
    if isinstance(val, tuple):
        return val[0]*SIZE_MULTIPLIER, val[1]*SIZE_MULTIPLIER
    if isinstance(val, int):
        return val * SIZE_MULTIPLIER

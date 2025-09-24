INTERVALS = [0, 1, 3, 7, 14, 21, 35, 90]

MAX_LEVEL = len(INTERVALS) - 1
MIN_LEVEL = 0


def increase_interval(interval_level: int):
    new_level = min(interval_level + 1, MAX_LEVEL)
    return new_level, INTERVALS[new_level]


def decrease_interval(interval_level: int):
    new_level = max(interval_level - 1, MIN_LEVEL)
    return new_level, INTERVALS[new_level]

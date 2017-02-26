
def UpDownLeftRightIter(point:tuple):
    yield (point[0], point[1] - 1)
    yield (point[0], point[1] + 1)
    yield (point[0] - 1, point[1])
    yield (point[0] + 1, point[1])
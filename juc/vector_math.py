import numpy
from juc.box import *
import math


def DistanceSqr(p1, p2):
    #distVec = [p1[i] - p2[i] for i in range(0, len(p1))]
    distVec = numpy.subtract(p1,p2)
    #print(distVec)
    distSqr = 0.0
    for i in range(0, len(p1)):
        distSqr += distVec[i] ** 2
    return distSqr

def IsInCircle(center, radiusSqr, point):
    distSqr = DistanceSqr(center, point)
    return (distSqr < radiusSqr)

def AreVectorsEqual(v1:tuple, v2:tuple):
    for i in range(0,len(v1)):
        if v1[i] != v2[i]:
            return False
    return True

def CircleCircumferenceIter(xy, radius):
    xy = (int(xy[0]), int(xy[1]))
    x = int(radius)
    y = 0
    err = 0

    while (x >= y):
        yield (xy[0] + x, xy[1] + y)
        yield (xy[0] + y, xy[1] + x)
        yield (xy[0] - y, xy[1] + x)
        yield (xy[0] - x, xy[1] + y)
        yield (xy[0] - x, xy[1] - y)
        yield (xy[0] - y, xy[1] - x)
        yield (xy[0] + y, xy[1] - x)
        yield (xy[0] + x, xy[1] - y)

        if (err <= 0):
            y += 1
            err += int(2*y + 1)
        if (err > 0):
            x -= 1
            err -= int(2*x + 1)

            """
def CircleCircumferenceIter(center:tuple, radius:float):
    startPoint = (center[0] + radius, center[1])
    #it start off as anything, as long as it doesn't equal the start point
    #lastPoint = (startPoint[0] + 123, startPoint[1])
    lastPoint = startPoint
    currPoint = lastPoint

    radiusBiggerSqr = (radius) ** 2
    radiusSmallerSqr = (radius - 1) ** 2

    box = CreateBoxFromCenterAndSize(center, (radius, radius))
    for xy in BoxIter(box):
        if IsInCircle(center, radiusSmallerSqr, xy):
            continue
        if IsInCircle(center, radiusBiggerSqr, xy):
            yield xy
            """

    """
    while True:
        box = CreateBoxFromCenterAndSize(currPoint, (1,1))
        for xy in BoundOfBoxIter(box):
            if xy == startPoint:
                return
            if xy == lastPoint:
                #print("SDLKFJSDFKLSDJFLK")
                continue
            #if it's in the smaller circle
            if IsInCircle(center, radiusSmallerSqr, xy):
                continue
            if IsInCircle(center, radiusSqr, xy):
                lastPoint = currPoint
                currPoint = xy
                yield xy
                break
                """
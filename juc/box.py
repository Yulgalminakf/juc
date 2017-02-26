from juc.two_dimensional_list import FindInList
import math

class Box:
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.EnsureValidity()

    #ensures that left is less than right, and up is less than down
    def EnsureValidity(self):
        if self.up > self.down:
            self.up = self.down
        if self.left > self.right:
            self.left = self.right

    def GetStr(self):
        return "(Up: %f, Down: %f, Left: %f, Right: %f)" % (self.up, self.down, self.left, self.right)

    def IsPointInBox(self, point):
        return point[1] >= self.up and point[1] <= self.down and point[0] >= self.left and point[0] <= self.right

    def Width(self):
        return self.right - self.left

    def Height(self):
        return self.down - self.up

    def TopLeft(self):
        return (left, up)

    def TopRight(self):
        return (right, up)
    
    def BottomLeft(self):
        return (left, down)
    
    def BottomRight(self):
        return (right, down)

    def Center(self):
        return (self.Width() / 2 + self.left, self.Height() / 2 + self.up)

def CreateBoxFromCenterAndSize(center, size):
    return Box(center[1] - size[1], center[1] + size[1], center[0] - size[0], center[0] + size[0])

def CreateBoxFromCorners(topLeft, bottomRight):
    return Box(topLeft[1], bottomRight[1], topLeft[0], bottomRight[0])

def ClampBox(box, clampBox):
    rBox = Box(0,0,0,0)
    rBox.up = max(box.up, clampBox.up)
    rBox.down = min(box.down, clampBox.down)
    rBox.left = max(box.left, clampBox.left)
    rBox.right = min(box.right, clampBox.right)
    rBox.EnsureValidity()
    return rBox

"""
def counter(low, high):
    current = low
    while current <= high:
        yield current
        current += 1
"""

def SpiralOutwardBoxIter(box:Box, boxStepSize:tuple = (1,1), boundsStepSize:tuple = (1,1)):
    center = box.Center()
    center = (int(center[0]), int(center[1]))
    halfSize = (int(box.Width() / 2), int(box.Height() / 2))
    boxStepSize = (max(1,int(boxStepSize[0])), max(1, int(boxStepSize[1])))
    currSize = boxStepSize
    while currSize[0] <= halfSize[0] and currSize[1] <= halfSize[1]:
        iBox = CreateBoxFromCenterAndSize(center, currSize)
        for xy in BoundOfBoxIter(iBox, boundsStepSize):
            yield xy
        currSize = (currSize[0] + boxStepSize[0], currSize[1] + boxStepSize[1])

def BoxIter(box:Box, stepSizeXY:tuple = (1,1)):
    for y in range(box.up, box.down + 1, stepSizeXY[1]):
        for x in range(box.left, box.right + 1, stepSizeXY[0]):
            yield (x,y)

def BoundOfBoxIter(box:Box, stepSizeXY:tuple = (1,1)):
    #clockwise starting at top, left
    for x in range(box.left, box.right, stepSizeXY[0]):
        yield (x,box.up)
    for y in range(box.up, box.down, stepSizeXY[1]):
        yield (box.right, y)
    for x in range(box.right, box.left, -stepSizeXY[0]):
        yield (x, box.down)
    for y in range(box.down, box.up, -stepSizeXY[1]):
        yield (box.left, y)
    """
    #right SHOULD be plus 1, is inclusive, but range() is exclusive
    for x in range(box.left, box.right + 1, stepSizeXY[0]):
        yield (x,box.up)
        yield (x,box.down)
    #up SHOULD be plus 1, as (left,up) and (right,up) are given by previous for loop
    for y in range(box.up + 1, box.down, stepSizeXY[1]):
        yield (box.left, y)
        yield (box.right, y)
        """

def TestBoundBoxIter():
    for i in range(20,40):
        for j in range(0,20):
            list = []
            box = CreateBoxFromCorners((j,j), (i,i))
            for xy in BoundOfBoxIter(box):
                if FindInList(list, xy) is not None:
                    print("Found duplicate value!")
                list.append(xy)
            sizeShouldBe = (box.Width() * 2) + (box.Height() * 2)# - 2
            size = len(list) 
            if size is not sizeShouldBe:
                print("Not proper list size! Should be: %d. Is: %d." % (sizeShouldBe, size))
    print("Test finished.")
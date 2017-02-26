from array import array
import pickle

class TwoDList:
    def __init__(self, sizeXY, defaultValue = None):
        self.sizeXY = sizeXY
        self.list = [defaultValue] * sizeXY[0] * sizeXY[1]

    def GetIndexFromXY(self, xy):
        if xy[0] < 0 or xy[0] >= self.sizeXY[0] or xy[1] < 0 or xy[1] >= self.sizeXY[1]:
            print("XY is out of range: " + str(xy))
            print("Must be under: " + str(self.sizeXY))
            return None
        return xy[0] * self.sizeXY[0] + xy[1]

    def Get(self, xy):
        return self.list[self.GetIndexFromXY(xy)]

    def Set(self, xy, value):
        self.list[self.GetIndexFromXY(xy)] = value

        """
    def ToFile(self, filepath):
        pickle.dump(self.list, open(filepath,'wb'))
        #file = open(filepath, 'w')
        #file.write(str(self.sizeXY))
        #file.write(str(self.list))

    def FromFile(self, filepath):
        #file = open(filepath, 'r')
        self.list = pickle.load(open(filepath, 'rb'))
        
        #byteArr = bytearray(self.list)
        #arr = array('f', self.list)
        #array(
        #arr.tofile(file)
        """



def FindInList(list, value):
    for i in range(0,len(list)):
        if list[i] == value:
            return i
    return None
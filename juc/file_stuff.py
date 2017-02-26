#from os import listdir
#from os.path import 

from os import listdir
from os.path import isfile, join
from os.path import expanduser
import pickle
from juc.two_dimensional_list import *

def ConvertBackToForwardSlashes(str:str):
    return str.replace('\\','/')

def IsFileInDir(dir, filename):
    return FindInList(GetOnlyFilesInDirectory(dir), filename) is not None

def GetOnlyFilesInDirectory(dir):
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
    return onlyfiles
"""
    all = listdir(dir)
    if all is None:
        return None
    filesOnly = []
    for i in range(0,len(all)):
        if isfile(join(dir,all[i])):
            filesOnly.append(all[i])
    return filesOnly
"""

def GetUserDir():
    return ConvertBackToForwardSlashes(expanduser("~"))

def PickleObject(obj, filepath):
    pickle.dump(obj, open(filepath, 'wb+'))

def UnpickleObject(filepath):
    return pickle.load(open(filepath,'rb'))
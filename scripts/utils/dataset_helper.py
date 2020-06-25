import os
from os import listdir
from os.path import isfile, join, splitext
from numpy import unique

"""	
Args:
    path: The absolute path contain image and label file
Return:
    [[png, label],[]...] in absolute path
"""
def getFilenames(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    names = [splitext(f)[0] for f in files]
    unique_names = unique(names)
    data_names = [[join(path, f+'.png'), join(path, f+'.txt')] for f in unique_names]
    return data_names

"""
Args:
    filename: label filename, the label file with the following format:
    ratio x, ratio y, ratio w, ratio h, class
Return:
    out: 2-D list like
"""
def getLabel(filename):
    f = open(filename)
    lines = f.readlines()
    out = []
    for line in lines:
        data = line.split(" ")        
        out.append([float(data[i]) for i in range(5)])
    return out

"""
Args:
    filenames: List of label filenames
Return:
    out: 3-D List like
"""
def getLabelList(filenames):
    out = []
    for n in filenames:
        out.append(getLabel(n))
    return out

def exportLabelFile(filename, label):
    f = open(filename, "w")
    for l in label:
        line = ""
        for i,x in enumerate(l):
            if i == 0:
                line += str(int(x)) + " "
            else:
                line += str(x) + " "
        line += "\n"
        f.write(line)
    f.close()

def main():
    names = getFilenames('/home/joey3639570/dataset/original_for_yolo/')
    print(getLabel(names[5][1]))

if __name__ == '__main__':
    main()

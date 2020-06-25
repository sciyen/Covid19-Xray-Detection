import cv2
import os
from utils.dataset_helper import *
import numpy as np

FOLDER = '/home/joey3639570/dataset/original_splitted/train'
OUTPUT = '/home/joey3639570/dataset/augmentation/train'
CLASS = ['No', 'Pneumonia', 'GGO', 'Under']
SIZE = (1024, 1024)

METHOD = {
        'origin':{'method':"origin", 'iter':1, 'ker':1},
        'erosion':{'method':"erosion", 'iter':3, 'ker':3},
        'open':{'method':cv2.MORPH_OPEN, 'iter':3, 'ker':3},
        'close':{'method':cv2.MORPH_CLOSE, 'iter':3, 'ker':3},
        'grad':{'method':cv2.MORPH_GRADIENT, 'iter':5, 'ker':10},
        'tophat':{'method':cv2.MORPH_TOPHAT, 'iter':5, 'ker':10},
        'blackhat':{'method':cv2.MORPH_BLACKHAT, 'iter':5, 'ker':10}
        }
def morpho(img, config):
    kernel = np.ones((config['ker'], config['ker']), np.uint8)

    if config['method'] == "origin":
        out = img.copy()
    elif config['method'] == "erosion":
        out = cv2.erode(img, kernel, iterations=config['iter'])
    else:
        out = cv2.morphologyEx(img, config['method'], kernel, iterations=config['iter'])
    return out

def crop(img, label, crop_size):
    # Calculate offset (if label is too low to crop, offset the image first and then crop)
    offset = 0
    h, w = img.shape
    for i, l in enumerate(label):
        label[i][2] = l[2]*h/w
        if label[i][2]>1 and label[i][2]-1>offset:
            offset = label[i][2]-1

    if offset > 0:
        for i, l in enumerate(label):
            label[i][2] -= offset
            
    X = int(offset*h)
    out = img[X:X+w, 0:w]
    out = cv2.resize(out, crop_size)
    return out, label, offset

def main():
    names = getFilenames(FOLDER)    
    label_filename = [n[1] for n in names]
    labels = getLabelList(label_filename)
    
    for name, label in zip(names, labels):
        # READ
        img = cv2.imread(name[0])
        h, w = img.shape
        basename = os.path.splitext(os.path.basename(name[0]))[0]
        
        

        #print(label)
        print("Write into " + basename)
        for method in ['origin', 'erosion', 'open', 'close']:
            out = crop(img, SIZE)
            out = morpho(img, METHOD[method])

            new_name = method + "_" + basename
            cv2.imwrite(os.path.join(OUTPUT, new_name+".jpg"), out)
            exportLabelFile(os.path.join(OUTPUT, new_name+".txt"), label)

if __name__ == "__main__":
    main()

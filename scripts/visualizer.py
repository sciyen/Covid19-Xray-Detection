import cv2
import os
from utils.dataset_helper import *
import numpy as np

FOLDER = '/home/joey3639570/dataset/original_splitted/train'
OUTPUT = '/home/joey3639570/visualization/preprocessing'
CLASS = ['Pneumonia', 'GGO', 'Under']

def visualize(img, label):
    height, width = img.shape

    for l in label:
        # SCALE TO REAL PIXEL
        center = (int(l[1]*width), int(l[2]*height))
        size = (int(l[3]*width), int(l[4]*height))
        start = (int(center[0]-size[0]//2), int(center[1]-size[1]//2))
        end = (start[0] + size[0], start[1] + size[1])

        # DRAW
        cv2.rectangle(img, start, end, (0, 255, 0), 4)
        cv2.putText(img, CLASS[int(l[0])], start, cv2.FONT_HERSHEY_SIMPLEX,
                  3, (0, 255, 0), 3, cv2.LINE_AA)
    return img

def main():
    names = getFilenames(FOLDER)
    label_filename = [n[1] for n in names]
    labels = getLabelList(label_filename)
    
    for name, label in zip(names, labels):
        # READ
        img = cv2.imread(name[0])
        filename = os.path.basename(name[0])
        out = visualize(img, label)
        # OUTPUT
        output_filename = os.path.splitext(filename)[0] + ".jpg"
        print("Write into " + output_filename)
        cv2.imwrite(os.path.join(OUTPUT, output_filename), img)
    
if __name__ == "__main__":
    main()

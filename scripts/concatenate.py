import numpy as np
import cv2
import os
from utils.dataset_helper import *

#PREDICT = '/home/joey3639570/darknet/predictedimages'
PREDICT = '/home/joey3639570/darknet/20200612/darknet/predictedimages'
VISUAL = '/home/joey3639570/visualization/output'
OUTPUT = '/home/joey3639570/visualization/combine/0612'

predict_name = [f for f in os.listdir(PREDICT) if os.path.isfile(os.path.join(PREDICT, f))]

pure_name = [os.path.basename(n) for n in predict_name]

for pn in pure_name:
    pred_path = os.path.join(PREDICT, pn)
    visu_path = os.path.join(VISUAL, pn)
    if os.path.isfile(visu_path):
        print("Processing: " + pred_path)
        pred_img = cv2.imread(pred_path)
        visu_img = cv2.imread(visu_path)
        print(pred_img.shape)
        print(visu_img.shape)
        combine = np.concatenate((pred_img, visu_img), axis=1)
        cv2.imwrite(os.path.join(OUTPUT, pn), combine)
    else:
        print("Visual image not exist: " + pu)

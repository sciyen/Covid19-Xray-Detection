import os
from os import listdir, getcwd
from os.path import join
import pandas as pd
from PIL import Image

image_path = 'train_total'
csv_path = 'yolo_txt'
train_dataset = ['GGO','LLL','Pneumonia']

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[2])/2.0
    y = (box[1] + box[3])/2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(csv_file):
	dataname = csv_file.split('_')
	name = dataname[0]
	picname = dataname[0] + '.png'
	data_path = join(csv_path, csv_file)
	pic_path = join(image_path, picname)
	im = Image.open(pic_path)
	bb_size = im.size
	data_df = pd.read_csv(data_path,header=None)
	data = data_df.values
	out_file = open('train_total/%s.txt'%(name), 'w')
	for obj in data:
		cls_id = obj[-1]
		bb = convert(bb_size,obj)
		out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
	print(bb)


images = listdir(image_path)
labels = listdir(csv_path)
for label_file in labels:
	convert_annotation(label_file)

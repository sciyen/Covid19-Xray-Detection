import os
from os import listdir, getcwd
from os.path import join
import pandas as pd

train_dir = 'train_20200620'
train_dataset = ['GGO','LLL','Pneumonia']

def convert(box):
    box_w = box[2] - box[0]
    box_h = box[3] - box[1]
    dw = 1./box_w
    dh = 1./box_h
    x = (box[0] + box[2])/2.0
    y = (box[1] + box[3])/2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_to_one_row(txt_file):
	data = pd.read_table(txt_file,header=None,sep=',')
	data_list = []
	flag = 0
	temp = []
	for i in range(0,len(data)):
	    row = data.iloc[i,:].values
	    temp.append(row[0])
	    temp.append(row[1])
	    flag += 1
	    if(flag == 2):
	        temp.append(row[2]-1)
	        data_list.append(temp)
	       	temp = []
	        flag = 0
	return data_list

wd = getcwd()

for dset in train_dataset:
	dset_label = dset + ' Label'
	dset_dir = join(train_dir, dset_label)
	txtfiles = listdir(dset_dir)
	if not os.path.exists('yolo_txt'):
        	os.makedirs('yolo_txt')
	for txt in txtfiles:
		txt_path = join(train_dir, dset_label, txt)
		new_format_data = convert_to_one_row(txt_path)
		df = pd.DataFrame(new_format_data)
		new_path = join(wd,'yolo_txt',txt)
		df.to_csv(new_path, header=None, index=None)

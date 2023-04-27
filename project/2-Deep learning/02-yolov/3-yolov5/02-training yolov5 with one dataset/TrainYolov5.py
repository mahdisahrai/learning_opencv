
!git clone https://github.com/ultralytics/yolov5

%cd yolov5

!pip install -r requirements.txt


import os
from random import choice
import shutil
import torch
from IPython.display import Image



imgs =[]
xmls =[]

train_path = '/content/yolov5/data/images/train'
val_path = '/content/yolov5/data/images/val'
source_path = '/content/drive/MyDrive/dataset'

if not os.path.exists(train_path):
  os.mkdir(train_path)
if not os.path.exists(val_path):
  os.mkdir(val_path)

train_ratio = 0.8     # 0.8 for training
val_ratio = 0.2       # 0.2 for validation

#total count of imgs
totalImgCount = len(os.listdir(source_path))/2

#soring files to corresponding arrays
for (dirname, dirs, files) in os.walk(source_path):
    for filename in files:
        if filename.endswith('.txt'):
            xmls.append(filename)
        else:
            imgs.append(filename)


#counting range for cycles
countForTrain = int(len(imgs)*train_ratio)
countForVal = int(len(imgs)*val_ratio)
print("training images are : ",countForTrain)
print("Validation images are : ",countForVal)

trainimagePath = '/content/yolov5/data/images/train'
trainlabelPath =  '/content/yolov5/data/labels/train'
valimagePath = '/content/yolov5/data/images/val'
vallabelPath = '/content/yolov5/data/labels/val'

if not os.path.exists(trainimagePath):
  os.mkdir(trainimagePath)
if not os.path.exists(trainlabelPath):
  os.mkdir(trainlabelPath)
if not os.path.exists(valimagePath):
  os.mkdir(valimagePath)
if not os.path.exists(vallabelPath):
  os.mkdir(vallabelPath)

for x in range(countForTrain):

    fileJpg = choice(imgs) # get name of random image from origin dir
    fileXml = fileJpg[:-4] +'.txt' # get name of corresponding annotation file

    #move both files into train dir
    shutil.copy(os.path.join(source_path, fileJpg), os.path.join(trainimagePath, fileJpg))
    shutil.copy(os.path.join(source_path, fileXml), os.path.join(trainlabelPath, fileXml))


    #remove files from arrays
    imgs.remove(fileJpg)
    xmls.remove(fileXml)


#cycle for test dir   
for x in range(countForVal):

    fileJpg = choice(imgs) # get name of random image from origin dir
    fileXml = fileJpg[:-4] +'.txt' # get name of corresponding annotation file

    #move both files into train dir

    shutil.copy(os.path.join(source_path, fileJpg), os.path.join(valimagePath, fileJpg))
    shutil.copy(os.path.join(source_path, fileXml), os.path.join(vallabelPath, fileXml))
    
    #remove files from arrays
    imgs.remove(fileJpg)
    xmls.remove(fileXml)

#for moving from google drive
# shutil.copy('/content/gdrive/MyDrive/DL_projects_colab/dataset.yaml', '/content/yolov5/data/dataset.yaml')


!python train.py --img 415 --batch 16 --epochs 30 --data dataset.yaml --weights yolov5s.pt --cache #--cache showing details
!python detect.py --source /content/drive/MyDrive/images/traffic.jpg --weights /content/yolov5/runs/train/exp/weights/last.pt
Image('/content/yolov5/runs/detect/exp10/traffic.jpg')


!python train.py --img 415 --batch 16 --epochs 30 --data dataset.yaml --weights yolov5l.pt --cache #--cache showing details
!python detect.py --source /content/drive/MyDrive/images/traffic.jpg --weights /content/yolov5/runs/train/exp2/weights/best.pt
Image('/content/yolov5/runs/detect/exp9/traffic.jpg')


# for showing results and graph
# %load_ext tensorboard
# %tensorboard --logdir runs

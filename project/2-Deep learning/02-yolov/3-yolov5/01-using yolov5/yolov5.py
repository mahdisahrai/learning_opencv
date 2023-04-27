!python -m pip install --upgrade pip
!pip install tensorflow
!pip install tensorboard
!pip install torch


import torch
from IPython.display import Image


!git clone https://github.com/ultralytics/yolov5

%cd yolov5

!pip install -r requirements.txt


!python detect.py --weights yolov5m.pt  --source /content/drive/MyDrive/images/tehran.png
Image('/content/yolov5/runs/detect/exp/tehran.png')


!python detect.py --weights yolov5m.pt --conf-thres 0.7  --source /content/drive/MyDrive/images/tehran.png #conf-thres: accuracy
Image('/content/yolov5/runs/detect/exp2/tehran.png')


!python detect.py --weights yolov5m.pt --conf-thres 0.7 --source /content/drive/MyDrive/images/tehran.png --classes 0 3
Image('/content/yolov5/runs/detect/exp3/tehran.png')

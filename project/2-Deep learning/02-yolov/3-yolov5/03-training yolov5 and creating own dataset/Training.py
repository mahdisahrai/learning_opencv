!git clone https://github.com/ultralytics/yolov5

%cd yolov5

!pip install -r requirements.txt


import os
from random import choice
import shutil
import torch
from IPython.display import Image


!pip install roboflow


from roboflow import Roboflow
rf = Roboflow(api_key="OhaXBuHWLzwK4i1rCxMs")
project = rf.workspace("datasetyolov5-2k886").project("face_project")
dataset = project.version(1).download("yolov5")


!python train.py --img 415 --batch 16 --epochs 30 --data /content/yolov5/face_project-1/data.yaml --weights yolov5x.pt --cache #--cache showing details


# %load_ext tensorboard
# %tensorboard --logdir runs


!python detect.py --source /content/drive/MyDrive/images/2022-11-05-162137.jpg --weights /content/yolov5/runs/train/exp/weights/best.pt


Image('/content/yolov5/runs/detect/exp2/2022-11-05-162137.jpg')


from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode


def take_photo(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename
from IPython.display import Image
try:
  filename = take_photo()
  print('Saved to {}'.format(filename))

  # Show the image which was just taken.
  display(Image(filename))
except Exception as err:
  # Errors will be thrown if the user does not have a webcam or if they do not
  # grant the page permission to access it.
  print(str(err))


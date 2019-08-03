# -*- coding:utf-8 -*-

import cv2
import numpy as np

# 先ほど集めてきた画像データのあるディレクトリ
input_data_path = './downloads/face/geinoujin/women'
# 切り抜いた画像の保存先ディレクトリ(予めディレクトリを作っておいてください)
save_path = './downloads/face/'
# OpenCVのデフォルトの分類器のpath。(https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xmlのファイルを使う)
cascade_path = './settings/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascade_path)

# 収集した画像の枚数(任意で変更)
image_count = 80
# 顔検知に成功した数(デフォルトで0を指定)
face_detect_count = 0
# 画像の拡大率
expantion=1.6;

# 集めた画像データから顔が検知されたら、切り取り、保存する。
for i in range(image_count):
  print(i);
  img = cv2.imread(input_data_path + str(i) + '.jpg', cv2.IMREAD_COLOR)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  face = faceCascade.detectMultiScale(gray, 1.1, 3)
  img_h=len(img)-1
  img_w=len(img[0])-1
  if len(face) > 0:
    for rect in face:
      # 顔認識部分を赤線で囲み保存(今はこの部分は必要ない)
      # cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=1)
      # cv2.imwrite('detected.jpg', img)
      original_x = rect[0];
      original_y = rect[1];
      original_w = rect[2];
      original_h = rect[3];
      
      # 拡大率調整
      w=int(original_w*expantion);
      h=int(original_h*expantion);
      x=int(original_x-(w-original_w)*0.5);
      y=int(original_y-(h-original_h)*0.5);
      if x < 0:
        x = 0;
      if y < 0:
        y = 0;
      if x > img_w:
        x = img_w;
      if y > img_h:
        y = img_h;
      
      cv2.imwrite(save_path +"actor"+ str(face_detect_count) + '.jpg', img[y:y+h, x:x+w])
      face_detect_count = face_detect_count + 1
#  else:
#    print 'image'+str(i)+':NoFace'

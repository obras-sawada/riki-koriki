#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2
import tensorflow as tf
import os
import random
import main

# 学習結果(ckpt_path)のpath
CKPT_PATH = './model/kaomodel.ckpt'

# OpenCVのデフォルトの顔の分類器のpath
cascade_path = './settings/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascade_path)

# 識別ラベルと各ラベル番号に対応する名前
HUMAN_NAMES = {
  0: "kim",
  1: "phone",
  2: "other"  
}

#指定した画像(img_path)を学習結果(ckpt_path)(上記参照)を用いて判定する
def evaluation(img_path):
  ckpt_path = CKPT_PATH
  # GraphのReset(らしいが、何をしているのかよくわかっていない…)
  tf.reset_default_graph()
  # データを入れる配列
  image = []
  img = cv2.imread(img_path)
  img = cv2.resize(img, (28, 28))

  # 画像情報を一列にした後、0-1のfloat値にする
  image.append(img.flatten().astype(np.float32)/255.0)
  # numpy形式に変換し、TensorFlowで処理できるようにする
  image = np.asarray(image)
  # 入力画像に対して、各ラベルの確率を出力して返す(main.pyより呼び出し)
  logits = main.inference(image, 1.0)
  # We can just use 'c.eval()' without passing 'sess'
  sess = tf.InteractiveSession()
  # restore(パラメーター読み込み)の準備
  saver = tf.train.Saver()
  # 変数の初期化
  sess.run(tf.initialize_all_variables())
  if ckpt_path:
    # 学習後のパラメーターの読み込み
    saver.restore(sess, ckpt_path)
  # sess.run(logits)と同じ
  softmax = logits.eval()
  # 判定結果
  result = softmax[0]

  # 判定結果を%にして四捨五入
  rates = [round(n * 100.0, 1) for n in result]
  humans = []
  # ラベル番号、名前、パーセンテージのHashを作成
  for index, rate in enumerate(rates):
    name = HUMAN_NAMES[index]
    humans.append({
      'label': index,
      'name': name,
      'rate': rate
    })
  # パーセンテージの高い順にソート
  rank = sorted(humans, key=lambda x: x['rate'], reverse=True)

  # 判定結果を返す
  return rank


# コマンドラインからのテスト用
if __name__ == '__main__':
    # それぞれハイパーパラメータテスト画像のフォルダパス。確認したい画像のパスを、file_path=の後に置く

    test_data={0:"./hyper-test-pics/kim/kim",1:"./hyper-test-pics/tel/tel",2:"./hyper-test-pics/other/other"}
    print("test_resultファイルに書き込み開始")
    f = open('./test_result.txt', 'w')
    image_count = 100
    for i in range(image_count):
        result={}
        print("進捗:"+str(i))
        for label in test_data:
            file_path = (test_data[label] + str(i) + '.jpg')
            r = evaluation(file_path)
            result[label]=str(r[0]["label"]==label)
        f.write(result[1]+"\t"+result[0]+"\t"+result[2]+"\n")
    f.close()
    print("test_resultファイルに書き込み完了")
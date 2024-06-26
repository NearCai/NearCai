#用于计算数据集正则化的数值

import numpy as np
import cv2
import os

# img_h, img_w = 32, 32
img_h, img_w = 32,32  # 根据自己数据集适当调整，影响不大
means, stdevs = [], []
img_list = []

sample_size = 100

imgs_path = 'E:\\Pycharm\\Deep_Learning\\animal\\animal data\\train\\cat'
imgs_path_list = os.listdir(imgs_path)

len_ = len(imgs_path_list)
i = 0
for item in imgs_path_list:
    img = cv2.imread(os.path.join(imgs_path, item))
    img = cv2.resize(img, (img_w, img_h))
    img = img[:, :, :, np.newaxis]
    img_list.append(img)
    i += 1
    print(i, '/', len_)

    if i >= sample_size:
        break

imgs = np.concatenate(img_list, axis=3)
imgs = imgs.astype(np.float16) / 255.

for i in range(3):
    pixels = imgs[:, :, i, :].ravel()  # 拉成一行
    means.append(np.mean(pixels))
    stdevs.append(np.std(pixels))

# BGR --> RGB ， CV读取的需要转换，PIL读取的不用转换
means.reverse()
stdevs.reverse()

print("normMean = {}".format(means))
print("normStd = {}".format(stdevs))
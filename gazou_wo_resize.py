'''
単一画像ファイルをリサイズするコマンド
------------------------------------------------------
第1引数: 画像ファイルのパス
第2引数: リサイズする基準指定['w': 幅基準, 'h': 高さ基準]
第3引数: リサイズ後の大きさ
'''

import sys
import cv2
import glob
import shutil
import os

args = sys.argv

image_path = args[1]
sel = args[2]
val = float(args[3])

# 'image'ディレクトリ内の画像ファイル数だけループ
img = cv2.imread(image_path)
bw = img.shape[1]
bh = img.shape[0]

rt = float(bw) / float(bh)

if sel == 'w':
    nw = val
    nh = float(nw) / float(rt)
elif sel == 'h':
    nh = val
    nw = float(nh) * float(rt)
else:
    nw = bw
    nh = bh

img2 = cv2.resize(img, (int(nw), int(nh)))
base = os.path.basename(image_path)
os.remove(image_path)
cv2.imwrite(image_path, img2)

print('Resized ' + str(base) + ':')
print('Width: ' + str(bw) + '->' + str(int(nw)))
print('Height: ' + str(bh) + '->' + str(int(nh)))
print(' ')

print('Completed!')
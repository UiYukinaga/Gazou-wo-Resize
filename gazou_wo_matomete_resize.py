'''
ディレクトリ内の全画像ファイルを一括でリサイズする
---------------------------------------------------------
第1引数: 画像ファイルがあるディレクトリ
第2引数: リサイズする基準指定['w': 幅基準, 'h': 高さ基準]
第3引数: リサイズ後の大きさ
第4引数: 対象ファイル拡張子('.'除く)
'''

import sys
import cv2
import glob
import shutil
import os

args = sys.argv

dir_path = args[1]
sel = args[2]
val = float(args[3])
ext = "*." + args[4]

pick = dir_path
pick += '/'
pick += ext

save_dir = dir_path

# 画像ファイルリストの読み込み
image_names = glob.glob(pick)

# 'image'ディレクトリ内の画像ファイル数だけループ
for image_path in image_names:
    # n個目の画像ファイルの読み込み
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
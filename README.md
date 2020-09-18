# Gazou-wo-Resize
JPEGなどの静止画ファイルをリサイズするPythonコードです。


|Python Name|機能|
|:---|:---|
|gazou_wo_resize.py|指定した画像一枚をリサイズ|
|gazou_wo_matomete_resize.py|指定したディレクトリ内の画像をまとめてリサイズ|

## gazou_wo_resize.py
***
リサイズ後の幅もしくは高さを指定して、アスペクト比を維持したままリサイズします。

下記の要領で、引数3つを渡してpythonコードを実行します。

第1引数: 画像ファイルのパス
第2引数: 'w':幅を指定 'h':高さを指定
第3引数: 指定するサイズ[px]

```
$python gazou_wo_resize.py /home/user/images/hoge.jpg w 640
```

上記の例では、"/home/user/images/hoge.jpg"という画像ファイルを幅640ピクセルになるように、
アスペクト比を指示したままリサイズします。


## gazou_wo_matomete_resize.py
***
リサイズ後の幅もしくは高さを指定して、アスペクト比を維持したままリサイズします。
前述の"gazou_wo_resize.py"と違い、指定したディレクトリ内の画像ファイルをまとめて処理します。

下記の要領で、引数3つを渡してpythonコードを実行します。

第1引数: 画像ファイルのパス
第2引数: 'w':幅を指定 'h':高さを指定
第3引数: 指定するサイズ[px]
第4引数: ファイル拡張子('.'は除く)

```
$python gazou_wo_resize.py /home/user/images h 640 jpg
```

上記の例では、"/home/user/images"というディレクトリ内のjpgファイルを全てまとめて
高さ600ピクセルになるように、アスペクト比を指示したままリサイズします。


#numpyを使う課題
#4次元空間の座標a(1,2,3,4）と座標b(4,3,2,1)のユークリッド距離を求める
#計算を行うためにnumpyのメソッドを使う必要がある（平方根を求めるなど）
import numpy as np                      #numpyモジュールのインストール
a = np.array((1,2,3,4))                 #np.array(())内に座標(要素)を入れる
b = np.array((4,3,2,1))
euk = np.sqrt(np.sum(np.square(a-b)))   #numpy.sqrtは平方根,numpy.sumは要素の合計を返す関数,numpy.square()は要素の2乗を返す関数
print(euk)
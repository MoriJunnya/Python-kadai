#matplotlibを使う課題
#散布図を書く
#import matplotlib.pyplot as plt　というようにmatplotlibの描画機能をインポートして，散布図を描画して下さい．
#点を描画するだけでなく，軸のラベルなどを適切につけること
import numpy as np                  #numpyモジュールのインストール
import matplotlib.pyplot as plt     #matplotlibモジュールのインストール
#座標の入力
x = np.array([1452, 1796, 1894, 2584, 2735, 3447])
y = np.array([3231, 3747, 3726, 5853, 8866, 10913])

#散布図を描画
plt.scatter(x,y)
plt.xlabel('オープンキャンパス参加者数(人)', fontname="MS Gothic")
plt.ylabel('志願者数(人)', fontname="MS Gothic")
plt.show()
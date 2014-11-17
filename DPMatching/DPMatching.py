# モジュールのインポート
import pylab

file_1 = open("data_a.txt","r")
file_2 = open("data_b.txt","r")

x = []
y = []

# ファイルを１行ずつ読み込む
for line in file_1:
	 # 空白ずつ区切ってリストに入れる
	x = x + [float(line)]
	
for line in file_2:
	 # 空白ずつ区切ってリストに入れる
	y = y + [float(line)]


# pylab.subplot(321)
pylab.plot(x,"r")
pylab.title("A")

# pylab.subplot(321)
pylab.plot(y,"b")
pylab.title("B")

pylab.show()

file.close()
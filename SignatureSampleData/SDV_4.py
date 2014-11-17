# モジュールのインポート
import pylab

file = open("001.001.000.sdt","r")

# あらかじめ１行目を読み込みをしておく
file.readline()

x = []
y = []
hude = []
direction = []
height = []
Cont = []
con = 0

# y軸を0 ~ 200に限定する
pylab.xlim((0, 900))
# pylab.ylim((0, 1200))

# ファイルを１行ずつ読み込む
for line in file:
	con = con+1
	 # 空白ずつ区切ってリストに入れる
	itemList = line.split()

	if itemList[0]=="-1":
		pass

	else:
		# x,yにそれぞれ対応するデータを入れる
		x = x + [(int(itemList[0]))]
		y = y + [(int(itemList[1]))]
		hude = hude + [((int(itemList[2]))/3)]
		direction = direction + [((int(itemList[3]))/2)]
		height = height + [(int(itemList[4]))]
		Cont = Cont + [con]

# 最後のストロークは記述されないのでここでプロット
pylab.subplot(321)
pylab.plot(Cont,x,"r")
pylab.title("x軸")
# pylab.xlabel("1")

pylab.subplot(322)
pylab.title("y軸")
pylab.plot(Cont,y,"b")
# pylab.xlabel("2")

pylab.subplot(323)
pylab.title("筆圧")
pylab.plot(Cont,hude,"g")
# pylab.xlabel("3")

pylab.subplot(324)
pylab.title("方位")
pylab.plot(Cont,direction,"m")
# pylab.xlabel("4")

pylab.subplot(325)
pylab.title("高度")
pylab.plot(Cont,height,"y")
# pylab.xlabel("5")

pylab.show()

file.close()
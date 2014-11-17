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
		x = x + [(int(itemList[0]))+800]
		y = y + [(int(itemList[1]))+700]
		hude = hude + [((int(itemList[2]))/3)+400]
		direction = direction + [((int(itemList[3]))/2)-100]
		height = height + [(int(itemList[4]))-300]
		Cont = Cont + [con]

# 最後のストロークは記述されないのでここでプロット
pylab.plot(Cont,x,"r")
pylab.plot(Cont,y,"b")
pylab.plot(Cont,hude,"g")
pylab.plot(Cont,direction,"m")
pylab.plot(Cont,height,"y")

pylab.show()

file.close()
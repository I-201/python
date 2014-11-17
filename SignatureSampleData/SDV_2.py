# モジュールのインポート
import pylab

file = open("001.001.000.sdt","r")

# あらかじめ１行目を読み込みをしておく
file.readline()

# リストを中身空で宣言
x = []
y = []

# y軸を-300 ~ -50に限定する
pylab.ylim((-150,-50))

# ファイルを１行ずつ読み込む
for line in file:

	# 空白ずつ区切ってリストに入れる
	itemList = line.split()

	# -1が出たらそこまでのx,yでプロットするする


	if itemList[0]=="-1" or itemList[2]=="0":
		pylab.plot(x,y,"r")	
		
		# リストを中身空で宣言
		x = []
		y = []


	# x,yにそれぞれ対応するデータを入れる
	else:
		x = x + [int(itemList[0])]
		y = y + [-int(itemList[1])]

# 最後のストロークは記述されないのでここでプロット
pylab.plot(x,y,"r")
pylab.show()

file.close()


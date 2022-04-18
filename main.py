import translators as ts
import jieba
# print(ts.google("积极"))

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
import random
outputString=""
for w in seg_list:
	# rand=bool(random.getrandbits(1))
	# if rand:
	# 	print(ts.google(w))
	# else:
	# 	print(w)
	print(w)
	rand=bool(random.getrandbits(1))
	print("rand:",rand)
	if rand:
		# outputString+str(ts.google(w)[0])
		outputString=outputString+(ts.google(w))
		# print(outputString)
	else:
		outputString=outputString+(w)

print(outputString)
import asyncio
import time,random
import translators as ts
import jieba


seg_list = jieba.cut("我来到北京清华大学", cut_all=False)

async def google(seg_list):
    restr=""
    for w in seg_list:
        rand=bool(random.getrandbits(1))
        if rand:
            restr.join(ts.google(w))
        else:
            restr.join(w)

async def main():

    restr =await google(seg_list)
    print(restr)

asyncio.run(main())
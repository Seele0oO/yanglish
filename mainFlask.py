from ctypes import sizeof
import json
import random
from flask import Flask, render_template, request


def yanglish(putstring,languageList):
    from pygtrans import Translate
    # import translators as ts
    client = Translate()
    import jieba
    import random
    outputString = ""
    languageList=languageList.split(",")
    print(languageList)
    seg_list = jieba.cut(putstring, cut_all=False)
    # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
    for w in seg_list:
        print(w)
        # rand = bool(random.getrandbits(1))
        randlaugage=random.choice(languageList)
        print("randlaugage:",randlaugage)
        # print("rand:", rand)
        # if rand:
        text = client.translate(w,target=randlaugage,source='zh',fmt='text')
        outputString = outputString+" "+str(text.translatedText)+" "
            # print(outputString)
        # else:
            # outputString = outputString+(w)
            # print(outputString)
        # print(outputString)
    return outputString

def multiprocessing_yanglish(putstring):
    import asyncio
    import time,random
    import translators as ts
    import jieba
    seg_list = jieba.cut(putstring, cut_all=False)
    restr=""
    async def trans(seg_list):
        for w in seg_list:
            rand=bool(random.getrandbits(1))
            if rand:
                await restr.join(ts.google(w))
            else:
                await restr.join(w)
    async def main():
        restr = await trans(seg_list)
        print(restr)
        return restr
    return restr




app = Flask(__name__)

@app.route("/out")
def get_data():

    #可以通过 request 的 args 属性来获取参数
    getString = request.args.get("putstring")
    languageList = request.args.get("languageList")
    print(getString,languageList)
    # age = request.args.get("age")
    
    # 经过处理之后得到要传回的数据
    res= hello_world(getString,languageList)
    
    # 将数据再次打包为 JSON 并传回
    # res = '{{"obj": {} }}'.format(res.to_json(orient = "records", force_ascii = False))
    res = '{{"obj": {} }}'.format(res)
    
    return res

def hello_world(putstring,languageList):
    # putstring="我来到北京清华大学"
    outputString=yanglish(putstring,languageList)
    # print(outputString)
    outputStringJson=json.dumps(outputString)
    return outputStringJson


@app.route("/")
def index():
    if request.method =='GET':
        return render_template('index.html')
    

@app.route("/setu")
def setu():
    # print(response)
    return render_template('setu.html')
@app.route("/setu2")
def setu2():
    import requests
    response = requests.get("https://api.nyan.xyz/httpapi/sexphoto?num=1&r18=true")    
    # response.encoding = 'utf-8'
    response = response.json()
    # print(response)
    returnurl=response['data']['url'][0]
    # response = response['data'][0]['url']

    return returnurl

@app.route("/setu3")
def setu3():
    import requests
    imagelink=setu2()
    html = requests.get(imagelink)
    with open('/templates/picture.jpg', 'wb') as file:
        file.write(html.content)
    return render_template('setu3.html')


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)
    # yanglish("我来到北京清华大学")
    # index()
    
import json
import requests
import time


# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# error=""

mat = "{:<8}\t{:<16}\t{:<4}\t{:<11}\t{:<48}\t{:<8}\t{:<2}"
def load():
    while True:
        with open('urls.json','r',encoding='utf-8') as f:
            j=json.load(f)
            print(u'***********************************************************************************\n')
            print(u"****重新加载配置文件%s，版本：%s成功，版本日期：%s*****\n"%(j.get('name'),j.get('version'),j.get('datatime')))
            print(u'***********************************************************************************\n')
            f.close()
            print(mat.format("时间","名 称", "代码","响应时间(s)", "访问地址", "关键字","找到关键字")+'\n')
            for url in j.get('urls'):
                check(name=url.get('name'),url=url.get('url'), keyword=url.get('keyword'),meta=url.get('meta'))
        print("%s秒后重新检测"%(str(j.get('sleepTime'))))
        time.sleep(int(j.get('sleepTime')))
        print("\n\n\n")

def check(name,url,keyword,meta):
    starttime=time.strftime("%Y-%m-%d  %H:%M:%S")
    starttime=time.strftime("%H:%M:%S")
    try:
        Response=requests.get(url=url,timeout=5)
        status = Response.status_code
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout) as e:
        print(mat.format(starttime,name,"Error","Timeout",url,keyword,"N")+"\n")
    else:
        if status != 200:
            print(mat.format(starttime,name, status, str(Response.elapsed), url, keyword, "Y") + "\n")
        elif status == 200:
            print(mat.format(starttime,name, status, str(Response.elapsed), url, keyword, "Y" ) + "\n")

        if Response.status_code >= 400:
            pass
            # logger.warn("response status code fail:" + str(Response.status_code))
            # errorinfo.append("Access " + url + " fail, status code:" + str(Response.status_code))

def systeminfo():
    print("=================================================================================\n")
    print("===================Code by lizo From hnyxa.com===================================\n")
    print("=================================================================================\n")

systeminfo()
load()


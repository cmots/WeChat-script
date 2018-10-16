#-*-coding:utf-8 -*
import itchat,re
import math
import random
import requests
from itchat.content import *
def get_tuling_response(_info):
    print("    "+_info)
    api_url = "http://www.tuling123.com/openapi/api"
    data = {
        'key' : '60e5f912e2b34a54a3c55de5746fdd54',
        'info' : _info,
        'userid' : 'momo'
    }
    res = requests.post(api_url,data).json()
    print("I: "+res['text'])
    return res['text']
@itchat.msg_register([TEXT],isGroupChat=False)
def text_reply(msg):       
    match = re.search("(.*)",msg["Text"]).span()    
    if match: 
        content=msg['Content']
        #print(msg['FromUserName']);
        returnContent=get_tuling_response(content)
        if msg["FromUserName"]==itchat.search_friends(name='Destiny')[0]['UserName']:
            sentense=["乖","要乖乖哦","有急事要发短信哦","爱你","么么哒"]
            itchat.send((returnContent)+"【"+sentense[random.randint(0,4)]+"】",msg["FromUserName"])
        else:
            itchat.send((returnContent)+"【自动回复不代表本人观点】",msg["FromUserName"])

@itchat.msg_register([PICTURE,RECORDING,VIDEO,SHARING],isGroupChat=False)
def other_reply(msg):
    content=msg['Content']
    returnContent=get_tuling_response(content)
    if msg["FromUserName"]==itchat.search_friends(name='Destiny')[0]['UserName']:
        itchat.send((returnContent),msg["FromUserName"])
        itchat.send(("嘿嘿"),msg["FromUserName"])
    else:
         itchat.send((returnContent)+"【傻子AI不识别文本外数据】",msg["FromUserName"])
 
if __name__ == "__main__":    
    itchat.auto_login(enableCmdQR=True,hotReload=True)
    itchat.run()

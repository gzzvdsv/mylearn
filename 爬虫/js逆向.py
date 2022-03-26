import js2py
import json
import requests


# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 14:24
# @Author  : Xchen
# @Email   : 1272012812@qq.com
# @File    : TranslateBaidu.py
# @Software: PyCharm

# token: ea5ada4109c67257a32b444d7add8f51
import requests
import json
import execjs

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'cookie': '__yjs_duid=1_5ffb303a68cef187fa0bbd16672d28da1610896805863; BAIDUID=4D93AAC3A3CB1205043278144FDCA352:FG=1; BAIDUID_BFESS=4D93AAC3A3CB1205043278144FDCA352:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BIDUPSID=4D93AAC3A3CB1205043278144FDCA352; PSTM=1610897551; BDRCVFR[VXHUG3ZuJnT]=mk3SLVN4HKm; delPer=0; PSINO=5; H_PS_PSSID=; BA_HECTOR=0584alalak2g04ak8p1g0aar80r; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1610896807,1610951535; __yjsv5_shitong=1.0_7_bf96750ce6e3c2775d6ff12d4dbf3b4bc889_300_1610951535893_114.238.103.53_018a390e; yjs_js_security_passport=ae192e80ccd59875d5ef5dbd8ddbfc0aadf049c9_1610951536_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1610951556; ab_sr=1.0.0_NmEwZGZjNDc1YThmMzM5YTM1NWNjZDBjZDdlMzAwMmU2NGQ4YWM4Yjc4ZDAxNDJlYmFkNTYzY2MwMWIyYmQxYjcyOTE3NjFlYmQ3YmRhOTcxNDQ4MWE5YTNlNjMzNzJh'
}

# 获取sign标签
def get_sign(content):
    with open('baidu.js','r',errors='ignore') as f:
        rconnent=f.read()
    sign=execjs.compile(rconnent).call('e',content)
    return sign

#发送post请求
def parse_url(url,formdata):
    try:
        response=requests.post(url,data=formdata,headers=headers)
        if response.status_code==200:
            htmlstr=response.text
    except Exception as e:
        print(e.args)
        print('Request Error!!!')
    return htmlstr
    pass

# 获取json数据
def get_jsonData(htmlStr):
    jsondata=json.loads(htmlStr)
    result_c={}
    for item in jsondata["trans_result"]["data"]:
        result_c['result']=item['dst']
        return result_c

# 判断中英文
def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

# 处理表单数据
def dealwith_formdata(e,z,content,sign):
    '''
    发现发送请求之前需要识别中英文
    :param e: en
    :param z: zh
    :param content:翻译的内容
    :param sign: sign的值
    :return:
    '''
    form = {
        'from': e,
        'to': z,
        'query': content,
        'sign': sign,
        'token': 'ea5ada4109c67257a32b444d7add8f51',
    }
    return form

# 主函数逻辑及
def main():
    en = 'en'
    zh = 'zh'
    url='https://fanyi.baidu.com/v2transapi'
    # content =input('请输入要翻译的内容【汉\英】: ')
    print('请输入要翻译的内容【汉\英】: 汉字')
    content='汉字'
    sign=get_sign(content)
    if is_chinese(content):
        formdata=dealwith_formdata(zh,en,content,sign)
    else:
        formdata=dealwith_formdata(en,zh,content,sign)
        pass
    html_str = parse_url(url, formdata)
    res=get_jsonData(html_str)
    if is_chinese(content):
        print('<{}>的英文翻译为:{}'.format(content,res['result']))
    else:
        print('<{}>的中文翻译为:{}'.format(content,res['result']))
        pass

# 程序开关
if __name__ == '__main__':
    print('-----------------xchen翻译器----------------------')
    while True:
        main()

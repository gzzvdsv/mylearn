import requests


def request_jd(keyword):
    url = "https://search.jd.com/Search"
    params = {
        "keyword": keyword
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    response = requests.get(url=url, params=params, headers=headers)
    print(response.text)
      # 获取str类型的响应内容
    # response.content  # 获取bytes类型的响应内容
    # response.json()  # 获取json格式数据

if __name__=="__main__":
    request_jd("鼠标")

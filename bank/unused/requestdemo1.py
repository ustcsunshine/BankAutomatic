import requests


def getHTMLText(url):
    try:

        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "yi"

url="https://www.amazon.cn/dp/B0716WKH2J/ref=sr_1_2?__mk_zh_CN=亚马逊网站&crid=3CQ7XOJZ1AF7W&keywords=计算机网络&qid=1564195212&s=gateway&sprefix=计算机%2Caps%2C166&sr=8-2"
kv ={'wd':'Python'}
r=requests.get("http://baidu.com/s",params = kv)
print(r.request.url)
print(len(r.text))
print(r.status_code)
print(r.headers)
print(r.encoding)
print(r.apparent_encoding)
print(r.text)

if __name__ =="__main__":
    url ="http://baidu.com"
    print(getHTMLText(url))
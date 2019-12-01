import request
import os

url="http://image.ngchina.com.cn/2019/0419/20190419124312151.jpg"
root ="/Users/jingjing.li/Desktop/pics/"
path = root +url.split('/'[-1])
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r= request.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("succes")
    else:
        print("exists")
except:
    print("fail")
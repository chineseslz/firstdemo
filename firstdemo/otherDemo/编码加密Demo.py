from hashlib import md5
import base64

data= "musen"

# base编码
data = data.encode()
res = base64.b64encode(data)
print(res)

# base64解码
res2 = base64.b64decode(res)
print(res2)

def encrypt_md5(data):
    """md5加密"""
    # 创建md5对象
    new_md5 = md5()
    new_md5.update(data.encode('utf-8'))
    res = new_md5.hexdigest()
    # 加密
    return res

data = 'musen'
res = encrypt_md5(data=data)
print(res)
import os
import requests
# a="config.ini"
# b="c:\\path"
#
# a_path=b+"\\"+a
# c=os.path.join(b,a)
# print(c)
# print(a_path)
# 讲解的目的

#
# res=requests.request(method="get",
#                      url="baidu",
#                      params="token",
#                      json="12345")
# # 上面的requests等价于
# res=requests.get(url="baidu",
#                      params="token",
#                      json="12345")
# # 定义一个请求的数据，叫data，弄成一个字典
# data={
#     "method":"get",
#     "url":"baidu",
#     "params":"token",
#     "json":"12345"
# }
# res=requests.request(**data)

# pip install pyyaml
import yaml
# 由于yml是一个文件，需要打开和关闭，with open来打开并关闭这个文件
# 把文件读取出来，变成一个f文件流
with open(file="data/contact/member/member_api.yml") as f:
    a_list=yaml.safe_load(f)
    print(a_list)






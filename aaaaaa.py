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

# # pip install pyyaml
# import yaml
# # 由于yml是一个文件，需要打开和关闭，with open来打开并关闭这个文件
# # 把文件读取出来，变成一个f文件流
# with open(file="data/contact/member/member_api.yml") as f:
#     a_list=yaml.safe_load(f)
#     print(a_list)

from string import Template
aaaa={
  "userid": "${userid}",
  "name": "${name}",
  "department": "${department}"
}
aaaa=str(aaaa)
userid="tong"
name="tong"
department=[1,2]

# Template要传一个str类型的数据，因为aaaa字典，通过str(aaaa)转成为字符串
# 把要转化的变量统一写成${userid}的形式
# 只要substitute看到了，类似${userid}写法，那么里面要传一个字典类型，以key-value的形式转化
# key统一写成模板定义的${userid}，因此要写成userid，后面的value就是我们要改变的值，通常以变量
# 的方式展示出来
# 这里要传三个变量，因此data要弄成3个key-value的字典，一个传一个传
# Template(aaaa).substitute(data)

b=Template(aaaa).substitute({"userid":userid,"name":name,"department":department})

print(b)
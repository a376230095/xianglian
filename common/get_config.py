import configparser
import os


class GetConfig():
    base_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # 创建配置文件对象的初始化，要读取文件的
    def __init__(self):
        # 创建配置文件对象
        self.config=configparser.ConfigParser()
        # 读取配置文件,想要读取根路径下的config.ini
        config_path=os.path.join(self.base_path,"config.ini")
        self.config.read(config_path)

    # 通过section和option，获取到value
    def get_value(self,section,option):
        value=self.config.get(section,option)
        return value

# 在这里变成对象即可，我们引用对家就好了
cf=GetConfig()


if __name__ == "__main__":
    a=GetConfig()

    print(a.get_value("env", "ip"))
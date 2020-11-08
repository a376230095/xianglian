import configparser

class GetConfig():

    # 创建配置文件对象的初始化，要读取文件的
    def __init__(self):
        # 创建配置文件对象
        self.config=configparser.ConfigParser()
        # 读取配置文件
        self.config.read("config.ini")

    # 通过section和option，获取到value
    def get_value(self,section,option):
        value=self.config.get(section,option)
        return value


if __name__ == "__main__":
    a=GetConfig()
    print(a.get_value("env", "ip"))
import logging
import os


class Logs():
    base_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


    def __init__(self,):
        # 创建生成器日志对象
        self.logger=logging.getLogger("tong")
        # 设置生成器等级
        self.logger.setLevel(logging.DEBUG)
        # 生成格式化器
        self.formatter = logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s", "%Y-%m-%d-%H:%M")


    # 生成流处理器
    def set_stream_handle(self):
        # 生成流处理对象
        self.stream_handle=logging.StreamHandler()
        # 设置流处理器的等级
        self.stream_handle.setLevel(logging.DEBUG)
        # 设置把格式化器弄到流处理器中
        self.stream_handle.setFormatter(self.formatter)

    # 生成文件处理器
    def set_file_handle(self):
        # 把log放入到log文件夹中
        log_path=os.path.join(self.base_path,"log","log.log")
        # 生成流处理对象
        self.file_handle=logging.FileHandler(filename=log_path, mode="w")
        # 设置流处理器的等级
        self.file_handle.setLevel(logging.DEBUG)
        # 设置把格式化器弄到流处理器中
        self.file_handle.setFormatter(self.formatter)


    # 把处理器放到生成器里面去
    def get_log(self):
        self.set_stream_handle()
        self.set_file_handle()
        # 把处理器放到生成器里面去
        self.logger.addHandler(self.stream_handle)
        self.logger.addHandler(self.file_handle)
        # 这里必须返回logger对象，方便使用logger.info等方法
        return self.logger


if __name__ =="__main__":
    a=Logs()
    a.get_log().info("abc")
    # a.logger.info()
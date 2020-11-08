import logging


# 1.新建一个生成器
logger=logging.getLogger("tongtong")
# 定义一下这个生成器的日志等级
logger.setLevel(logging.DEBUG)

# 定义处理器，流处理器
steam_handle=logging.StreamHandler()
steam_handle.setLevel(logging.DEBUG)

# 定义文件处理器
filename="a.log"
file_handle=logging.FileHandler(filename=filename,mode="w")

# 定义一个格式化器
formatter = logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s", "%Y-%m-%d-%H:%M")

# 需要把格式化器放入到处理器中
steam_handle.setFormatter(formatter)
file_handle.setFormatter(formatter)

# 把处理器放入到生成器里面
logger.addHandler(file_handle)
logger.addHandler(steam_handle)


if __name__ =="__main__":
    logger.info("abc")


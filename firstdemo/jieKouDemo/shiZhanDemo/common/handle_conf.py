from configparser import ConfigParser


class Config(ConfigParser):
    """在创建对象是，直接加载配置文件中的内容"""

    def __init__(self, conf_file):
        super().__init__()

        self.read(conf_file, encoding='utf-8')


conf = Config(r'C:\testproject\firstdemo\firstdemo\firstdemo\jieKouDemo\shiZhanDemo\conf\config.ini')



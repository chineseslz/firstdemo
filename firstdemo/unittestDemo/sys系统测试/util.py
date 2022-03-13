class util:


    @classmethod
    def get_data(cls):
        testdata = [
                ('', 'pwd', '用户名 不能为空'),
                ('admin', '', '密码 不能为空'),
                ('adminx', 'pwd123', '没有此用户'),
                ('admin', 'pwd123', '密码错误')
        ]
        return testdata

    @classmethod
    def get_data_from_file(cls,path):
        rows=[]
        with open(path,'r',encoding='utf-8') as f:
            for line in f :
                user_data = line.strip().split(',')
                rows.append((user_data))
            return rows
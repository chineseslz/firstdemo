'''
    文件名以 test_*.py 文件或*_test.py
    函数名需要test开头
    类名需要test开头，类中的方法需要test开头
        类中不能有构造方法
    使用assert进行断言
    脚本名需要以test开头
'''

'''
    -s 将print语句的结果输出
    -v 以详细信息显示每条用例执行结果
    -q 以极简形式显示测试结果
    -k 通过关键字匹配脚本，函数名，类名，方法名
    -x 如果测试执行过程中有fail的用例，则测试立即停止
    -maxfile=n 当失败的用例达到指定的数量n，停止测试
    -m 对用例进行标记，执行指定的用例           python3 -m pytest -v -m a ./
        1.在项目根目录下新建pytest.ini
        2.在pytest.ini文件中添加标记
        3.使用装饰器标记测试用例'@pytest.mark.标记'
        4.执行，使用-m 标记  即可执行指定的用例
    
    @pytest.mark.skip(reason=xxx),无条件跳过指定用例
    @oytest.mark.skipif(条件，reason=xxx),有条件跳过指定用例
'''







import pytest


def test_1():
    print(123)
    assert 1 == 1


def atest_1():
    print(123)
    assert 1 == 1


if __name__ == '__main__':
    # pytest.main(['-s',__file__])  #-s 将print语句的结果输出
    pytest.main(['-v',__file__])  #-v 以详细信息显示每条用例执行结果
                                  #-q 以极简形式显示测试结果

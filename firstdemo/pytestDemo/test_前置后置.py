import pytest

def setup_module():#模块级别
#def setup_function():每条用例
#def setup_class(self):类级别
#def setup_method(self):方法级别
    print("\n前置...")

def teardown_module():#模块级别
# def teardown_function():每条用例
#def teardown_class(self):类级别
#def teardown_method(self):方法级别
    print("\n后置...")

@pytest.mark.parametrize('a',[1,2,3])
def test_a(a):
    print(a)

@pytest.mark.parametrize('b',[4,5,6])
def test_b(b):
    print(b)

if __name__ == '__main__':
    pytest.mark(['-s', __file__])
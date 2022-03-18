import pytest

# @pytest.mark.a
@pytest.mark.skip(reason='此版本不执行') #无条件跳过指定用例
def test_a(self):
    assert 120>100

# @pytest.mark.b
@pytest.mark.skipif(1==1,reason='此版本不执行')   #有条件跳过用例
def test_b(self):
    assert 12>100


if __name__ == '__main__':
    pytest.main('-v',__file__)
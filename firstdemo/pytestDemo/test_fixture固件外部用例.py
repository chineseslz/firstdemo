import pytest

cases = [('17551052310', 'slz', 'add-success'),
        ('17551052310', 'slz',  'already-added')]

@pytest.mark.parametrize("case",cases)
def test_add(fx,case):
    rq = fx
    url = ''
    add_data = {'customername':case[1],'customerphone':case[0],}
    r = rq.post(url=url,data = add_data)
    assert r.text == case[-1]

if __name__ == '__main__':
    pytest.mark(['-s', __file__])
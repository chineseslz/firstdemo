import unittest
# import stringTests, numberTests

from numberTests import numberTests
from stringTests import stringTests

def getFullTestCaseName(names):
    full_names = []
    for item in names:
        full_names.append("numberTests.numberTests."+item)
    return  full_names

if __name__ == '__main__':
    # fromTestCase   从class类
    # st = unittest.defaultTestLoader.loadTestsFromTestCase(stringTests)
    # num = unittest.defaultTestLoader.loadTestsFromTestCase(numberTests)
    # suite = unittest.TestSuite([st,num])
    # unittest.TextTestRunner().run(suite)

    # fromModule    从模板
    # names = [stringTests,numberTests]
    # modules = []
    # for item in names:
    #    module = unittest.defaultTestLoader.loadTestsFromModule(item)
    #    modules.append(module)
    # suite = unittest.TestSuite(modules)
    # unittest.TextTestRunner().run(suite)

    # fromNames     从用例名
    # names = ["numberTests.numberTests.testNum1", "stringTests.stringTests.testStr2"]
    # smoke_test = unittest.defaultTestLoader.loadTestsFromNames(names)
    # suite = unittest.TestSuite([smoke_test])
    # unittest.TextTestRunner().run(suite)

    # 函数批量用例名执行
    # names = unittest.defaultTestLoader.getTestCaseNames(numberTests)
    # smoke_test = unittest.defaultTestLoader.loadTestsFromNames(getFullTestCaseName(names))
    # suite = unittest.TestSuite([smoke_test])
    # unittestDemo1.TextTestRunner().run(suite)

    # 执行目录下的用例
    unit = "unittestDemo"
    dis = unittest.defaultTestLoader.discover(unit,pattern='*.py')
    # suite = unittest.TestSuite(dis)
    # unittestDemo1.TextTestRunner.run(suite)
    print(dis)
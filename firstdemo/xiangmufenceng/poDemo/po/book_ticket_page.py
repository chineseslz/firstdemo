'''
    页面的业务代码
'''

from firstdemo.xiangmufenceng.poDemo.base.base import Base
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Bookticket(Base):
    def book_start(self):
        return self.byname("")

    def book_end(self):
        return self.byname("")

    def move_click(self):
        action = ActionChains(self.driver)
        action.move_by_offset(0,0)
        action.click()
        action.perform()

    def book_date(self,date):
        self.byname("date").send_keys(Keys.CONTROL,"a")
        self.byname("date").send_keys(Keys.BACKSPACE)
        self.byname("date").send_keys(date)


    def book_ticket(self, start, end, date, name, id):

        self.book_start().send_keys(start)
        self.book_end().send_keys(end)
        self.move_click()
        self.book_date(date)
        # 各站点击操作



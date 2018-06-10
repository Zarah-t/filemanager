from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def find_element(self, loc, timeout=5.0, poll=1.0):
        by = loc[0]
        value = loc[1]  # "text,0"
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value) # //*
            print(value)
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, loc, timeout=5.0, poll=1.0):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value) # //*
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def make_xpath_with_unit_feature(self, loc):
        """
        拼接xpath中间的部分
        :param loc:
        :return:
        """
        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and "
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "

        return feature

    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            # 如果是正常的xpath
            if loc.startswith("//"):
                return loc

            # loc str
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            # loc 列表
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)

        feature = feature.rstrip("and ")

        loc = feature_start + feature + feature_end

        return loc

    def find_toast(self, message, is_screenshot=False, screenshot_name=None, timeout=3, poll=0.1):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位
        element = self.find_element((By.XPATH, message), timeout, poll)
        if is_screenshot:
            self.screenshot(screenshot_name)

        return element.text

    def is_toast_exist(self, message, is_screenshot=False, screenshot_name=None, timeout=3, poll=0.1):
        try:
            self.find_toast(message, is_screenshot, screenshot_name, timeout, poll)
            return True
        except Exception:
            return False

    def screenshot(self, file_name):
        self.driver.get_screenshot_as_file("./screen/" + file_name + ".png")

    def scroll_page_one_time(self, direction="down"):
        window_size = self.driver.get_window_size()
        window_height = window_size["height"]
        window_width = window_size["width"]
        up_y = window_height * 0.25
        down_y = up_y * 3
        left_x = window_width * 0.25
        rigth_x = left_x * 3
        center_x = window_width * 0.5
        center_y = window_height * 0.5

        if direction == "down":
            self.driver.swipe(center_x, down_y, center_x, up_y)
        elif direction == "up":
            self.driver.swipe(center_x, up_y, center_x, down_y)
        elif direction == "left":
            self.driver.swipe(left_x, center_y, rigth_x, center_y)
        elif direction == "right":
            self.driver.swipe(rigth_x, center_y, left_x, center_y)
        else:
            raise Exception("请输入正确的direction参数")

    def is_loc_exist(self, loc):
        try:
            self.find_element(loc)
            return True
        except Exception:
            return False


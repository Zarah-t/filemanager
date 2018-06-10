import os, sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())

from base.base_action import BaseAction


class FilePage(BaseAction):

    # 菜单
    menu_button = By.ID, "com.cyanogenmod.filemanager:id/ab_actions"
    # 刷新
    refresh_button = By.XPATH, "text,刷新"
    # 书签
    book_mark_button = By.XPATH, "text,书签"
    # 快捷方式
    shot_cut_button = By.XPATH, "text,快捷方式"
    # set_as_home
    set_as_home_button = By.XPATH, "text,set"
    # 侧边栏
    side_menu_button = By.ID, "android:id/home"

    # 文件列表的标题
    dir_list_title = By.ID, "com.cyanogenmod.filemanager:id/navigation_view_item_name"
    # 目录imageview的特征
    path_name = By.ID, "com.cyanogenmod.filemanager:id/breadcrumb_item"
    # 侧边栏书签的特征
    side_menu_book_mark = By.ID, "com.cyanogenmod.filemanager:id/bookmarks_item_name"

    def click_menu(self):
        self.click(self.menu_button)

    def click_refresh(self):
        self.click(self.refresh_button)

    def click_book_mark(self):
        self.click(self.book_mark_button)

    def click_shot_cut(self):
        self.click(self.shot_cut_button)

    def click_set_as_home(self):
        self.click(self.set_as_home_button)

    def click_side_menu(self):
        self.click(self.side_menu_button)

    def get_first_dir_name(self):
        return self.find_element(self.dir_list_title).text

    def get_last_path_name(self):
        return self.find_elements(self.path_name)[-1].text

    def get_side_menu_book_marks(self):
        book_marks = self.find_elements(self.side_menu_book_mark)
        book_mark_list = list()
        for i in book_marks:
            book_mark_list.append(i.text)
        return book_mark_list





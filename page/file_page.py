import os, sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())

from base.base_action import BaseAction


class FilePage(BaseAction):

    # 菜单
    menu_button = By.ID, "com.cyanogenmod.filemanager:id/ab_actions"
    # 刷新
    refresh_button = By.XPATH, "刷新"
    # 书签
    book_mark_button = By.XPATH, "书签"
    # 快捷方式
    shot_cut_button = By.XPATH, "快捷方式"


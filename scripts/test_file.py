import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.file_page import FilePage


class TestFile:

    def setup(self):
        self.driver = init_driver()
        self.file_page = FilePage(self.driver)

    def test_refresh(self):
        name = self.file_page.get_first_dir_name()
        self.file_page.scroll_page_one_time()
        self.file_page.click_menu()
        self.file_page.click_refresh()
        assert name == self.file_page.get_first_dir_name()

    def test_book_mark(self):
        name = self.file_page.get_last_path_name()
        self.file_page.click_menu()
        self.file_page.click_book_mark()
        self.file_page.click_side_menu()
        assert name in self.file_page.get_side_menu_book_marks()




    def test_shot_cut(self):
        pass

    def test_set_as_home(self):
        pass

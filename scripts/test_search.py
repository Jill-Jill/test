from base.base_driver import init_driver
from page.page import Page

import pytest

class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("keyword", ["xiaoming", "123", "hello"])
    def test_search(self, keyword):
        self.page.setting.click_search()
        self.page.search.input_search(keyword)
        self.page.search.click_back()

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_001(self):
        print("哈哈")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_002(self):
        print("呵呵")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_003(self):
        print("丫丫")
        assert 1
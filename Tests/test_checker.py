import pytest

from pages.main_page import OpenMainPage


@pytest.mark.checker
@pytest.skip
class TestChecker:
  def test_checker(self, browser):
    OpenMainPage(browser).checker_main_page()


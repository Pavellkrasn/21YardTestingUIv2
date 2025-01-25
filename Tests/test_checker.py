import pytest

from pages.main_page import OpenMainPage


@pytest.mark.checker
@pytest.mark.skip("Ждем готовности прода")
class TestChecker:
  def test_checker(self, browser):
    OpenMainPage(browser).checker_main_page()


from playwright.sync_api import Page
from data.environment import host
from playwright.sync_api import expect
from pages.base import Base


class Assertions(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def check_URL(self, uri):
        expect(self.page).to_have_url(f"{host.get_base_url()}{uri}", timeout=60000)

    def have_text(self, locator, text: str):  # элемент имеет текст
        loc = self.page.locator(locator)
        expect(loc).to_have_text(text)

    def check_presence(self, locator):
        loc = self.page.locator(locator)
        expect(loc).to_be_visible(visible=True, timeout=12000),

    def check_absence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_hidden(timeout=700), msg

    def check_equals(self, actual, expected, msg):
        assert actual == expected, msg

from playwright.sync_api import Page, expect, sync_playwright
from utils.config_parser import YamlParse


class Base:

    def __init__(self, page: Page):
        self.page = page
        self.config = YamlParse().parse_config()
        self.url = self.config['url']

    def GoToSite(self):
        print("dddddddddddddddddddddddd")
        print(self.url)
        print(self.config)
        url = self.config['url']
        self.page.goto(url)

    def AssertTitle(self):
        expect(self.page).to_have_title("Flight Booking")

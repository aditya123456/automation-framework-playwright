import pytest
from playwright.sync_api import Page, expect

from pages.base import *

@pytest.fixture
def navigation(page: Page):
    base = Base(page)
    base.GoToSite()

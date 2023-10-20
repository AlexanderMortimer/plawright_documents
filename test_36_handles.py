import re
from playwright.sync_api import Page, expect,Playwright
import pytest


def test_click_button(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/buttons",wait_until='domcontentloaded')
    ###Get by text
    # page.get_by_text("Click Me",exact=True).hover()
    # page.get_by_text("Click Me",exact=True).click()

    # page.query_selector("text=Clike Me").hover()
    click = page.query_selector("text=Clike Me")
    # print(click.json_value)

    context.close()
    browser.close()

   
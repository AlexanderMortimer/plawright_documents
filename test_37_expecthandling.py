import re
from playwright.sync_api import Page, expect,Playwright,sync_playwright
import pytest


def test_expect_button(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/webtables",wait_until='domcontentloaded')
    ###Get by text
    
    expect(page.get_by_role("gridcell", name="Vega")).to_be_hidden()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    test_expect_button(playwright)

   
import re
from playwright.sync_api import Playwright, expect,sync_playwright
import pytest
import time
def test_checkbox(playwright:Playwright):
    iphone_13 = playwright.devices['iPhone 13']
    browser = playwright.chromium.launch(headless=False,slow_mo=10000)
    context = browser.new_context(
        **iphone_13,
    )
    page = context.new_page()
    page.goto("https://www.reqres.in")

with sync_playwright() as playwright:
    test_checkbox(playwright)
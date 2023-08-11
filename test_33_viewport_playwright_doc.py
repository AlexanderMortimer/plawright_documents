import re
from playwright.sync_api import Playwright, expect,sync_playwright
import pytest
import time
def test_checkbox(playwright:Playwright):
    iphone_13 = playwright.devices['iPhone 13']
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context(viewport={"height":1200,"width":1500},
                                  device_scale_factor=20)
    page = context.new_page()
    page.goto("https://playwright.dev/python/docs/emulation")


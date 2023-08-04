import re
from playwright.sync_api import Playwright, expect

def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    

    page = context.new_page()

    page.goto("https://www.excoino.com/",wait_until='domcontentloaded')
    page.mouse.click(0,0)

    









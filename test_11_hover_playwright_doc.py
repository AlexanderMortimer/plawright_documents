import re
from playwright.sync_api import Playwright, expect

def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    

    page = context.new_page()

    page.goto("https://dribbble.com/shots/14639664--Hover-w-animated-letters",wait_until='domcontentloaded')
    scale_chckBox = page.get_by_role('button', name='Share Actions')
    scale_chckBox.hover()

    









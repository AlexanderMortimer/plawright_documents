import re
from playwright.sync_api import Playwright, expect

def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=10000)
    context = browser.new_context()
    

    page = context.new_page()

    page.goto("https://panel.excoino.com/auth/login")
    scale_chckBox = page.get_by_label("رمز عبور")
    scale_chckBox.focus()
    

    









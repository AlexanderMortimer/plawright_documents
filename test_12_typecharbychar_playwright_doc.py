import re
from playwright.sync_api import Playwright, expect

def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    

    page = context.new_page()

    page.goto("https://panel.excoino.com/auth/login",wait_until='domcontentloaded')
    scale_chckBox = page.get_by_label("شماره موبایل یا ایمیل")
    scale_chckBox.type("morteza Oskuei",delay=1000)

    









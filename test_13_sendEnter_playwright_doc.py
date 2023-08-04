import re
from playwright.sync_api import Playwright, expect

def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=10000)
    context = browser.new_context()
    

    page = context.new_page()

    page.goto("https://panel.excoino.com/auth/login",wait_until='domcontentloaded')
    page.press(key="Enter",selector=" ")
    ###press enter directly inside a page not on an element
    
    page.keyboard.press('Enter')
    scale_chckBox = page.get_by_label("شماره موبایل یا ایمیل")
    scale_chckBox.type("morteza Oskuei")
    scale_chckBox.press("Enter")
    scale_chckBox.press("Control+a")

    









import re
from playwright.sync_api import Playwright, expect
import time
def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    

    page = context.new_page()

    page.goto("https://www.bing.com/create")
    # page.get_by_alt_text("Microsoft Bing").drag_to(page.get_by_placeholder("Describe what you'd like to create"))
    page.get_by_alt_text("Microsoft Bing").hover()
    page.mouse.down()
    page.get_by_placeholder("Describe what you'd like to create").hover()
    page.mouse.up()
    time.sleep(5)

    









import re
from playwright.sync_api import Playwright, expect

def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=10000)
    context = browser.new_context()
    

    page = context.new_page()

    page.goto("https://filebin.net/")
    # page.get_by_label("Select files to upload").set_input_files(['screen.png','screen.png'])
    page.get_by_label("Select files to upload").set_input_files(
    files=[
        {"name": "test.txt", "mimeType": "text/plain", "buffer": b"this is a test"}
    ],
)

    
    

    









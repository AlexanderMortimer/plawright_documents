
import re
from playwright.sync_api import Page, expect,Playwright,sync_playwright
import pytest
import time

def test_expect_button(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.route(
        "**/BookStore/v1/Books",
        lambda route: route.fulfill(path="book.json")
    )
    page.goto("https://demoqa.com/books")
    time.sleep(60)
    ###Get by text
    
    

    context.close()
    browser.close()

with sync_playwright() as playwright:
    test_expect_button(playwright)

   
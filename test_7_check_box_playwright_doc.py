import re
from playwright.sync_api import Playwright, expect

def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    

    page = context.new_page()

    page.goto("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox",wait_until='domcontentloaded')
    # page.get_by_role("button", name="Run ❯").click()
    scale_chckBox = page.frame_locator("iframe[name=\"iframeResult\"]").get_by_label("I have a bike")
    scale_chckBox.check()

    expect(scale_chckBox).to_be_checked









import re
from playwright.sync_api import Playwright, expect
import time
def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    

    page = context.new_page()

    page.goto("https://panel.excoino.com/panel")
    login_inputBox = page.get_by_label("رمز عبور")
    expect(login_inputBox).to_be_empty()
    expect(login_inputBox).not_to_be_editable()
    expect(login_inputBox).to_be_hidden()
    

    









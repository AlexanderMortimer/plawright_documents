import re
from playwright.sync_api import Playwright, expect
import pytest

def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=10000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://panel.excoino.com/auth/login")
    login_inputBox = page.get_by_label("رمز عبور")
    
    pytest.mark.fail
    expect(login_inputBox).to_be_empty()

    

    pytest.mark.fail
    expect(login_inputBox).not_to_be_editable()
    pytest.mark.fail
    expect(login_inputBox).to_be_hidden()
   
    
    
   
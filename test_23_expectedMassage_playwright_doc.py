import re
from playwright.sync_api import Playwright, expect
import pytest

def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=10000)
    pixel_2 = playwright.devices['Pixel 2']
    context = browser.new_context(**pixel_2,)
    page = context.new_page()

    page.goto("https://panel.excoino.com/auth/login")
    login_inputBox = page.get_by_label("رمز عبور")
    
    # expect.set_options(timeout=10_000)
    expect((login_inputBox),'Should be loged in').not_to_be_empty(timeout=1000)
   
    
    
   
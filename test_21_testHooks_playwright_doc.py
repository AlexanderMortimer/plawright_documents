import re
from playwright.sync_api import Playwright, expect,Page
import time
import pytest



@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    # Go to the starting url before each test.
    page.goto("https://panel.excoino.com/panel")
    global login_inputBox 
    login_inputBox = page.get_by_label("رمز عبور")
    yield
    print("afterEach")

def test_checkbox_1(page:Page):
    
    
    expect(login_inputBox).to_be_empty()
def test_checkbox_2(page:Page):
    expect(login_inputBox).not_to_be_editable()
def test_checkbox_3(page:Page):
    expect(login_inputBox).to_be_hidden()
    

    









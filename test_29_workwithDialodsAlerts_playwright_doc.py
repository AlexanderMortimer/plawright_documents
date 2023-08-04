import re
from playwright.sync_api import Playwright, expect
import pytest
import time
def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=10000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nxtgenaiacademy.com/alertandpopup/",wait_until='domcontentloaded')
    # alert_box = page.get_by_role("button",name="Alert Box")
    
    page.on("dialog",lambda dialog: print(dialog.message))
    page.on("dialog",lambda dialog: dialog.accept())
    

    alert_box = page.get_by_role("button",name="Alert Box",exact=True)
    alert_box.click()
    
    confirm_alert_box = page.get_by_role("button",name = "Confirm Alert Box")
    confirm_alert_box.click()

    

    
   
    
    
   
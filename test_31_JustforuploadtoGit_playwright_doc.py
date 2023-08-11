import re
from playwright.sync_api import Playwright, expect
import pytest
import time
def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nxtgenaiacademy.com/alertandpopup/",wait_until='domcontentloaded')
    # alert_box = page.get_by_role("button",name="Alert Box")
    
    with page.expect_event("dialog") as dialog_info:
    # Dismiss (or accept) next dialog
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("button",name="Alert Box",exact=True).click()
    dialog = dialog_info.value
    assert dialog.message == "I am an alert box!"

    with page.expect_event("dialog") as dialog_info:
# Dismiss (or accept) next dialog
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("button",name="Confirm Alert Box").click()
    dialog = dialog_info.value
    assert dialog.message == "Confirm pop up with OK and Cancel button"
###Upload for merge



    

    
   
    
    
   
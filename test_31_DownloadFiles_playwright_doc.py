import re
from playwright.sync_api import Playwright, expect
import pytest
import time
def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.freeimages.com/download/spagetti-1465102",wait_until='domcontentloaded')
    
    # Start waiting for the download
    with page.expect_download() as download_info:
    # Perform the action that initiates download
        page.get_by_role("button",name="Download").click()
# Wait for the download to start
    download = download_info.value
    # Wait for the download process to complete
    print(download.path())
    # Save downloaded file somewhere
    download.save_as("./test.jpg")
import re
from playwright.sync_api import Page, expect,Playwright
import pytest


def test_videorecord(playwright:Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()
    page.goto("https://playwright.dev/")
    page.goto("https://www.varzesh3.com")
    context.close()
    browser.close()

   
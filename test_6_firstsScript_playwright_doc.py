from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False,slow_mo=100)
    page = browser.new_page()
    page.goto('https://playwright.dev/')
    page.screenshot(path='screen.png')
    browser.close()

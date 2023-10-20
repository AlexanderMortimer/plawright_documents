# import re
# from playwright.sync_api import Page, expect


# def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
#     page.goto("https://playwright.dev/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))

#     # create a locator
#     get_started = page.locator("text=Get Started")

#     # Expect an attribute "to be strictly equal" to the value.
#     expect(get_started).to_have_attribute("href", "/docs/intro")

#     # Click the get started link.
#     get_started.click()

#     # Expects the URL to contain intro.
#     expect(page).to_have_url(re.compile(".*intro"))

# def test_return():
#     return False
# assert test_return()

from playwright.sync_api import Playwright, sync_playwright, expect
import re

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/")
    page.locator("div").filter(has_text=re.compile(r"^Alerts, Frame & Windows$")).first.click()
    page.locator("li").filter(has_text=re.compile(r"^Frames$")).click()
    page.frame_locator.
    # ---------------------
    context.close()
    browser.close()

    

with sync_playwright() as playwright:
    run(playwright)

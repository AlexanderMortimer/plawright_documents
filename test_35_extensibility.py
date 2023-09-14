import re
from playwright.sync_api import Page, expect,Playwright
import pytest


def test_click_button(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/buttons",wait_until='domcontentloaded')
    tag_selector = """
    // Must evaluate to a selector engine instance.
    {
      // Returns the first element matching given selector in the root's subtree.
      query(root, selector) {
        return root.querySelector(selector);
      },

      // Returns all elements matching given selector in the root's subtree.
      queryAll(root, selector) {
        return Array.from(root.querySelectorAll(selector));
      }
    }"""

    # register the engine. selectors will be prefixed with "tag=".
    playwright.selectors.register("tag", tag_selector)

# now we can use "tag=" selectors.
    # button = page.locator("tag=button")
    # button.click()

# we can combine it with built-in locators.
    # page.locator("tag=div").get_by_text("click me").click()

# we can use it in any methods supporting selectors.
    button_count = page.locator("tag=link").count()
    print(button_count+1)
    context.close()
    browser.close()

   
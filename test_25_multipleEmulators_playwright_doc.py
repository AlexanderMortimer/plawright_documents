from playwright.sync_api import sync_playwright,expect

def test_run_tests_in_emulators():
    with sync_playwright() as playwright:
        for browser_type in [playwright.chromium, playwright.webkit]:
            browser = browser_type.launch(headless=False)
            for emulator_name in ["iPhone 11", "Pixel 2", "Nexus 10"]:
                context = browser.new_context( **playwright.devices[emulator_name])
                page = context.new_page()

                page.goto("https://panel.excoino.com/auth/login",wait_until='domcontentloaded')
                login_inputBox = page.get_by_label("رمز عبور")
    
    # expect.set_options(timeout=10_000)
                expect((login_inputBox),f'Should run in {browser_type} and {emulator_name}').to_be_empty()
                
                # Close the page and context
                page.close()
                context.close()

            # Close the browser
            browser.close()

    
    
   
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch Browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://playwright.dev/python')

    # Locate a link element with "Docs" text
    docs_button = page.get_by_role('link', name="docs")
    docs_button.click()

    # Get page URL
    print("Docs: ", page.url)
    browser.close
    
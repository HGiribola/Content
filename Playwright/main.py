from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch()
    blank_page = browser.new_page()
    blank_page.goto("https://bard.google.com/")

    print(blank_page.title())

    browser.close()
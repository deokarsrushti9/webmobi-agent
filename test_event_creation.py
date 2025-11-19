import os
from playwright.sync_api import sync_playwright

# Credentials
os.environ["WM_EMAIL"] = "deokarsrushti9@gmail.com"
os.environ["WM_PASSWORD"] = "12345678"

WM_EMAIL = os.getenv("WM_EMAIL")
WM_PASSWORD = os.getenv("WM_PASSWORD")

def test_event_creation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://events.webmobi.com/")
        page.wait_for_load_state()

        page.click("text=Login")
        page.fill("input[type='email']", WM_EMAIL)
        page.fill("input[type='password']", WM_PASSWORD)
        page.click("button:has-text('Sign in')")
        page.wait_for_selector("text=Dashboard", timeout=15000)

        page.click("a:has-text('Create Event')")

        page.wait_for_selector("div:has-text('webinar')", timeout=20000)
        page.locator("div:has-text('webinar')").first.click()

        page.fill("textarea", "Automated event created using Cursor AI Agent.")

        send_btn = page.locator("button:has(svg)").first
        send_btn.click()

        page.wait_for_timeout(6000)

        page.click("text=My Events")
        page.wait_for_selector("text=Frontiers", timeout=20000)

        # ⬇⬇⬇ Screenshot saved in same directory ⬇⬇⬇
        screenshot_path = "eventcreated.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print("Screenshot saved at:", os.path.abspath(screenshot_path))

        page.wait_for_timeout(2000)
        browser.close()

if __name__ == "__main__":
    test_event_creation()

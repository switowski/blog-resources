import asyncio
import os
from typing import Optional

from pyppeteer import launch
from pyppeteer.browser import Browser
from pyppeteer.page import Page

# I've removed my username and any other confidential information
MAIN_URL = "https://www.tradingview.com/u/<my-username>/"
LOGIN_URL = "https://www.tradingview.com/accounts/signin/"

USERNAME = os.environ["TV_USERNAME"]
PASSWORD = os.environ["TV_PASSWORD"]

# Indicator ID can be found in the POST requests that TradingView sends
# Use the "Network" tab of your browser's dev tools to find that ID
INDICATOR_IDS = {
    "Script1": "PUB;<alphanumeric ID1>",
    "Script2": "PUB;<alphanumeric ID2>",
}

API_URLS = {
    "add": "https://www.tradingview.com/pine_perm/add/",
    "check": "https://www.tradingview.com/pine_perm/list_users/",
    "remove": "https://www.tradingview.com/pine_perm/remove/",
}


async def post_request(page: Page, url: str, params: dict) -> dict:
    """Prepare and evaluate a JavaScript code with POST request in the context of the current page."""
    form = "let formData = new FormData();\n"
    for key, value in params.items():
        form += f"formData.append('{key}', '{value}');\n"
    payload = "() => {\n" + form
    payload += f'return fetch("{url}",'
    payload += '{"credentials": "include", "mode": "cors", "method": "POST", "body": formData}'
    payload += ").then(res => res.json());}"
    return await page.evaluate(payload)


async def launch_browser() -> tuple[Browser, Page]:
    """Open browser and set some default settings."""
    browser = await launch(
        executablePath="/usr/bin/chromium-browser",
        headless=True,
        args=["--no-sandbox", "--disable-gpu"],
    )
    page = await browser.newPage()
    # Set some legitimately looking user agent
    await page.setUserAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 14.5; rv:126.0) Gecko/20100101 Firefox/126.0")
    return (browser, page)


async def login(page: Page):
    # networkidle2: consider navigation to be done when there are no more than 2 network connections for at least 500 ms
    await page.goto(LOGIN_URL, {"waitUntil": "networkidle2"})

    await page.click('button[name="Email"]')
    await page.waitForSelector("input[name=id_username]")

    await page.type("input[name=id_username]", USERNAME)
    await page.type("input[name=id_password]", PASSWORD)
    submit_button = await page.xpath("//button[contains(., 'Sign in')]")
    await submit_button[0].click()
    await asyncio.sleep(3)
    await page.goto(MAIN_URL, {"waitUntil": "networkidle2"})


# Functions creating POST requests with JSON payload
async def add_access_json(page: Page, script: str, user: str, expiration_str: Optional[str] = None):
    """Add access to a script for a given user and return JSON response."""
    payload = {
        "pine_id": INDICATOR_IDS[script],
        "username_recip": user,
    }
    if expiration_str:
        payload["expiration"] = expiration_str
    return await post_request(page, API_URLS["add"], payload)


async def check_access_json(page: Page, script: str, user: str):
    """Check access to a script for a given user and return a JSON response."""
    payload = {
        "pine_id": INDICATOR_IDS[script],
        "username": user,
    }
    return await post_request(page, API_URLS["check"], payload)


async def remove_access_json(page: Page, script: str, user: str):
    """Remove access to a script from a given user and return JSON response."""
    payload = {
        "pine_id": INDICATOR_IDS[script],
        "username_recip": user,
    }
    return await post_request(page, API_URLS["remove"], payload)

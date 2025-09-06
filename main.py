from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from qr_getter import get_qr_screenshot, get_qr_raw

if __name__ == "__main__":
    # Set up Firefox in headless mode
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://web.whatsapp.com")
    driver.implicitly_wait(30)
    print("Opened WhatsApp Web")

    # Wait for QR code to load
    time.sleep(5)

    # Get QR code image using get_qr_screenshot
    qr_bytes_screenshot = get_qr_screenshot(driver, output_path="images/qr_from_screenshot.png")
    print("Saved QR code from screenshot as qr_from_screenshot.png")

    # Get QR code image using get_qr_raw
    qr_bytes_raw = get_qr_raw(driver, output_path="images/qr_from_raw.png")
    print("Saved QR code from raw as qr_from_raw.png")

    # driver.quit()
    print("Done.")


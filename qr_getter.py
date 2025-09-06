from selenium.webdriver.common.by import By
import base64

def get_qr_screenshot(driver, output_path=None):
    """
    Takes a screenshot of the QR canvas element only and saves it to output_path.
    Returns the PNG bytes of the screenshot.
    Throws ValueError if output_path is not provided.
    """
    if output_path is None or driver is None:
        raise ValueError("output_path parameter must be provided.")
    canvas = driver.find_element(By.TAG_NAME, "canvas")
    canvas.screenshot(output_path)
    with open(output_path, "rb") as f:
        png_bytes = f.read()
    return png_bytes

def get_qr_raw(driver, output_path=None):
    """
    Extracts the QR code image from the canvas HTML element as raw PNG bytes.
    Saves the PNG bytes to output_path.
    Returns the PNG bytes.
    Throws ValueError if output_path is not provided.
    """
    if output_path is None or driver is None:
        raise ValueError("Both driver and output_path parameters must be provided.")
    canvas = driver.find_element(By.TAG_NAME, "canvas")
    canvas_png = driver.execute_script("return arguments[0].toDataURL('image/png').substring(22);", canvas)
    png_bytes = base64.b64decode(canvas_png)
    with open(output_path, "wb") as f:
        f.write(png_bytes)
    return png_bytes

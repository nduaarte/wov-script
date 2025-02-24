import pyautogui

def find_image_on_screen(image_path, region=None):
    if region:
        image_found = pyautogui.locateOnScreen(image_path, confidence=0.8, region=region)
    else:
        image_found = pyautogui.locateOnScreen(image_path, confidence=0.8)

    if image_found is not None:
        x, y, width, height = image_found
        center_x = x + width // 2 
        center_y = y + height // 2  
        return center_x, center_y
    else:
        return None

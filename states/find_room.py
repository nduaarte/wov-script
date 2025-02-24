from utils.tools import find_image_on_screen
import pytesseract
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

farm_room_names = ["vill win", "village win", "nt", "win vill"]

while True:
  flag_coords = find_image_on_screen(r"C:\Users\nycol\Desktop\wovbot\assets\na_server.png")
  center_x, center_y = flag_coords

  room_name_screenshot = pyautogui.screenshot(region=(center_x+30, center_y-17, 150, 20))
  room_name_text = pytesseract.image_to_string(room_name_screenshot)
  print(room_name_text)

  def check_if_room_is_farm():
    for keyword in farm_room_names:
      if keyword.lower() in room_name_text.lower(): 
        return True
    return False
  
  if check_if_room_is_farm():
    print("✅ room is farm...")
    break
  else:
    print("🔎 next room...")

pyautogui.click(center_x, center_y)
  
while True:
  time.sleep(0.5)
  enter_button_coords = find_image_on_screen(r"C:\Users\nycol\Desktop\wovbot\assets\buttons\play.png")

  if enter_button_coords is not None:
    center_x, center_y = enter_button_coords
    pyautogui.click(center_x, center_y)
    break




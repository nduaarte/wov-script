import time
import pyautogui
import pytesseract
from utils.tools import find_image_on_screen
from configs import IMAGE_PATH

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

screen_width, screen_height = pyautogui.size()
current_region = (0, 0, screen_width, screen_height)

FARM_ROOM_NAMES = ["vill win", "village win", "nt", "win vill", "will win"]
FIND_ROOM_COMPLETE = False

while True:
  if FIND_ROOM_COMPLETE:
    print("find_room complete!")
    break

  # Loop pra procurar sala.
  while True: 
    flag_coords = find_image_on_screen(f"{IMAGE_PATH}\\ui\\na_server.png", region=current_region)
    # Casa não tenha mais salas, vai dar refresh e pesquisar novamente.
    if flag_coords is None:
      continue  

    center_x, center_y = flag_coords
    room_name_screenshot = pyautogui.screenshot(region=(center_x+30, center_y-17, 250, 20))
    room_name_text = pytesseract.image_to_string(room_name_screenshot)
    print(room_name_text)

    def check_if_room_is_farm():
      for keyword in FARM_ROOM_NAMES:
        if keyword.lower() in room_name_text.lower(): 
          return True
      return False
    
    if check_if_room_is_farm():
      print("✅ farm room")
      break
    else:
      current_region = (0, center_y+50, screen_width, screen_height)
      print("🔎 next room...")

  time.sleep(1)

  pyautogui.click(center_x, center_y)
    
  # Loop pra aguardar popup de confirmação de entrar na sala. Dependendo do servidor pode demorar.
  while True:
    time.sleep(1)
    enter_room_button_coords = find_image_on_screen(f"{IMAGE_PATH}\\ui\\enter_room.png")
    
    if enter_room_button_coords is not None:
      center_x, center_y = enter_room_button_coords
      pyautogui.click(center_x, center_y)
      break

  while True:
    time.sleep(1)
    game_in_progress_warn_coords = find_image_on_screen(f"{IMAGE_PATH}\\ui\\game_in_progress_warn.png")
    welcome_lobby_coords = find_image_on_screen(f"{IMAGE_PATH}\\ui\\welcome_lobby.png")

    if welcome_lobby_coords is not None:
      FIND_ROOM_COMPLETE = True
      break

    if game_in_progress_warn_coords is not None:
      print("parece que a sala está cheia ou indisponível...")
      time.sleep(0.5)
      pyautogui.click()
      break
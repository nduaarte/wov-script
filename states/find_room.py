from utils.tools import find_image_on_screen
import pytesseract
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

farm_room_names = ["vill win", "village win", "nt", "win vill", "will win"]
screen_width, screen_height = pyautogui.size()
current_region = (0, 0, screen_width, screen_height)
FIND_ROOM_COMPLETE = False

# time.sleep(3)
while True:
  if FIND_ROOM_COMPLETE:
    print("verificação de sala concluída!")
    break

  # Loop pra procurar sala.
  while True: 
    flag_coords = find_image_on_screen(r"C:\Users\nycol\Desktop\wovbot\assets\na_server.png", region=current_region)
    # Casa não tenha mais salas, vai dar refresh e pesquisar novamente.
    if flag_coords is None:
      print("sem salas de farms. aguardando atualizar...")
      time.sleep(4)
      continue  

    center_x, center_y = flag_coords
    room_name_screenshot = pyautogui.screenshot(region=(center_x+30, center_y-17, 250, 20))
    room_name_text = pytesseract.image_to_string(room_name_screenshot)
    print(room_name_text)

    def check_if_room_is_farm():
      for keyword in farm_room_names:
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
    enter_room_button_coords = find_image_on_screen(r"C:\Users\nycol\Desktop\wovbot\assets\buttons\enter_room.png")
    
    if enter_room_button_coords is not None:
      center_x, center_y = enter_room_button_coords
      time.sleep(1)
      pyautogui.click(center_x, center_y)
      break

  for i in range(3):
    time.sleep(1)
    game_in_progress_warn = find_image_on_screen(r"C:\Users\nycol\Desktop\wovbot\assets\game_in_progress_warn.png")

    if game_in_progress_warn is None:
      print("parece que a sala está cheia ou indisponível...")
      pyautogui.click(200, 200)
    else:
      FIND_ROOM_COMPLETE = True
      break





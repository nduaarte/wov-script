import pyautogui
from configs import IMAGE_PATH

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

def role_indentifier(): 
  my_character_coords = find_image_on_screen(f"{IMAGE_PATH}\\character.png")

  if my_character_coords is not None:
    print("personagem encontrado")
    center_x, center_y = my_character_coords
    my_role_screenshot = pyautogui.screenshot(region=(center_x+110, center_y+20, 65, 65))


   #todo comparar a imagem da role e comparar com outras roles
  else:
    print("personagem não encontrado")
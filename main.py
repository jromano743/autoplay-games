import cv2
import numpy as np
import pyautogui
import time

def find_play_button():
    
    image_ref = 'assets/accept_btn.png'
    threshold = 0.8
    height_img, width_img = 73, 224

    while True:
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        result = cv2.matchTemplate(screenshot, cv2.imread(image_ref), cv2.TM_CCOEFF_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(result)

        if result[max_loc[1], max_loc[0]] > threshold:
            print(f"Imagen encontrada")
            x_center = max_loc[0] + width_img // 2
            y_center = max_loc[1] + height_img // 2
            pyautogui.click(x_center, y_center)
            break
        else:
            print("Buscando...")
            time.sleep(1)

if __name__ == "__main__":
    find_play_button()


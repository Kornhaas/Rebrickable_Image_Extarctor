import inspect
import os
import pyautogui
import time
from icecream import ic

# from PIL import ImageGrab
# from functools import partial
# ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

time.sleep(5)
print(pyautogui.position())

CURRENTBASEDIR = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))


def click_on_image(image):
    image = "D:/Python/htmltocsv/img/" + image
    ic(image)
    r = None
    while r is None:
        try:
            time.sleep(1)
            location = pyautogui.locateOnScreen(image)
            break
        except Exception as e:
            r = None
            ic(r)


    ic(location)
    pyautogui.click(location)

def check_and_click_on_image(image):
    image = "D:/Python/htmltocsv/img/" + image
    ic(image)
    
    for i in range(1, 5):
        location = pyautogui.locateOnScreen(image)
        ic(location)
        time.sleep(1)
        i += 1

    ic(location)
    if location != None:
        for i in range(1, 5):
            click_on_image("ok.png")
            time.sleep(5)
            i += 1


for number in range(752, 1000+1):
    time.sleep(1)

    print("select picture")
    click_on_image("picture1.png")
    #time.sleep(1)

    print("click on build ersetzten ")
    click_on_image("replace.png")
    
   # time.sleep(1)

    print("click on seach file")
    click_on_image("searchfile.png")
    time.sleep(1)

    print("select input line")
    time.sleep(1)
    pyautogui.write('{0:04}'.format(number))
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.typewrite(["enter"])
    time.sleep(0.5)

    print("open")
    click_on_image("open.png")
    time.sleep(5)
    
    # Warnung druck optimierung
    check_and_click_on_image("print.png")
    time.sleep(5)
    
    print("next page")
    click_on_image("next.png")

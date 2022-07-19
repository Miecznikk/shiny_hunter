from pynput.keyboard import Key, Controller
import time
import cv2
import pytesseract
import pyscreenshot as sc


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

keyboard = Controller()

def sweetscent():
    keyboard.press(Key.f2)
    keyboard.release(Key.f2)

def run():
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(0.1)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.1)
    keyboard.press('z')
    keyboard.release('z')

def leppas():
    keyboard.press(Key.f2)
    keyboard.release(Key.f2)
    time.sleep(1.5)
    keyboard.press('z')
    keyboard.release('z')
    time.sleep(.5)
    keyboard.press('z')
    keyboard.release('z')
    time.sleep(.5)

def screen_check():
    im = sc.grab(bbox=(1080, 90, 1850, 210))
    im.save('im.png')
    img_cv = cv2.imread('im.png')
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    x = pytesseract.image_to_string(img_rgb)
    print(x)
    if 'Shiny' in x or 'shiny' in x or 'SHINY' in x:
        print('SHINY DETECTED')
        return False
    print('####\nNO SHINY DETECTED\n######')
    return True


print('Program will start in 5...',end='')
time.sleep(1)
print('4... ',end='')
time.sleep(1)
print('3... ',end='')
time.sleep(1)
print('2... ',end='')
time.sleep(1)
print('1... ')
time.sleep(1)
print('Program started')

running = True

while running:
    for i in range(6):
        sweetscent()
        time.sleep(13)
        if screen_check():
            run()
            time.sleep(2.2)
        else:
            running = False
            quit()
    leppas()







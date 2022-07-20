from pynput.keyboard import Key, Controller
import time
import cv2
import pytesseract
import pyscreenshot as sc
import random
import datetime

HORDES = 5

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
    time.sleep(random.uniform(1.5,1.7))
    keyboard.press('z')
    keyboard.release('z')
    time.sleep(random.uniform(0.4,.6))
    keyboard.press('z')
    keyboard.release('z')
    time.sleep(random.uniform(0.4,.6))

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

def save_encounters(enc):
    with open('encounters.txt',"w") as f:
        f.write(str(enc))

def shiny_enc(enc):
    with open('shiny.txt',"w") as f:
        f.write(f'Shiny encountered after {enc} encounters')

def timestamps(stop,start):
    with open('time.txt',"w") as f:
        f.write(f'{start.date()};{(stop-start).seconds}')

with open('encounters.txt') as f:
    encounters = int(f.read())

print('Program will start in 5 seconds ',end='')
time.sleep(5)
program_start = datetime.datetime.now()

running = True
print(f'Program started on {program_start}')

try:
    while running:
        for i in range(6):
            sweetscent()
            encounters+=HORDES
            time.sleep(random.uniform(12.6,13.2))
            if screen_check():
                run()
                time.sleep(random.uniform(2.0,2.3))
            else:
                running = False
                save_encounters(encounters)
                shiny_enc(encounters)
                program_stop = datetime.datetime.now()
                print(f'program stopped at {program_stop}')
                timestamps(program_stop,program_start)
        leppas()
except KeyboardInterrupt:
    print('program stopped')
    with open('encounters.txt',"w") as f:
        f.write(str(encounters))
    program_stop = datetime.datetime.now()
    print(f'program stopped at {program_stop}')
    timestamps(program_stop,program_start)








import pyautogui as pg
import webbrowser as web
import time 

#web.open('https://web.whatsapp.com/send?phone=+51903028886')//ani
web.open('https://web.whatsapp.com/send?phone=+51947298008') #XIO
#web.open('https://web.whatsapp.com/send?phone=+51955024017')//mina
time.sleep(15)
for i in range(50):
    pg.write('-----')
    pg.press('enter')
    print(i)
    pass


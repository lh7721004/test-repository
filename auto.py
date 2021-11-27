import pyautogui
import time
import datetime

ind = 0
meeting_room_numbers = ["1581735478"]
meeting_room_passes = ["112233"]
meeting_room_number = meeting_room_numbers[ind]
meeting_room_pass = meeting_room_passes[ind]

while True:
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    print(hour,minute,second)
    if hour == 9 and minute == 0 and second == 0 or hour == 9:
        break
    # break
pyautogui.hotkey('win', 'd')
pyautogui.hotkey('win', 'r')
pyautogui.typewrite("C:\Program Files (x86)\WebEx\Webex\Applications\ptoneclk.exe", interval=0.01)
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(1600,250,1,0)
pyautogui.hotkey('ctrl', 'a')
pyautogui.typewrite(meeting_room_number, interval=0.01)
pyautogui.press('enter')
time.sleep(10)
pyautogui.click(1290,840,1,0)
time.sleep(3)
pyautogui.click(1120,820,1,0)
time.sleep(3)
pyautogui.click(1125,995,1,0)
# time.sleep(3)
# pyautogui.press(['win', 'alt', 'r'])
# pyautogui.press('enter')
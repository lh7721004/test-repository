import pyautogui
import time
import datetime
from selenium import webdriver



"""
ind
컴프 0
프랙티컬 1
"""
ind = 0
meeting_room_numbers = ["26417180685"]
meeting_room_passes = ["123456"]
meeting_room_number = meeting_room_numbers[ind]
meeting_room_pass = meeting_room_passes[ind]

while True:
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    print(hour,minute,second)
    if hour == 10 and minute == 0 and second == 0 or hour == 10:
        break
    # break

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)



# options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome('chromedriver.exe',options=options)
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.implicitly_wait(5)

driver.get(url='https://eclass.dongguk.ac.kr/Main.do?cmd=viewHome#0')
driver.implicitly_wait(5)

driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/ul/li[1]").click()

driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/form/fieldset/ul/li[1]/input").click()
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/form/fieldset/ul/li[1]/input").send_keys("2021212816")
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/form/fieldset/ul/li[2]/input").click()
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/form/fieldset/ul/li[2]/input").send_keys("lh984988@")
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/form/fieldset/p/a").click()
driver.implicitly_wait(5)
time.sleep(1)
driver.get(url='https://eclass.dongguk.ac.kr/Course.do?cmd=viewStudyHome&courseDTO.courseId=K2021U0002003UICT13201&boardInfoDTO.boardInfoGubun=study_home&gubun=study_course')
driver.implicitly_wait(3)
print(driver.find_element_by_xpath("/html/body/div/div[2]/div[12]/form/div/div[4]/table/tbody/tr[1]/td[2]/div[1]/ul[1]/li").text)
driver.find_element_by_xpath("/html/body/div/div[2]/div[12]/form/div/div[4]/table/tbody/tr[1]/td[2]/div[1]/ul[3]/li/a").click()
# exit()
driver.implicitly_wait(3)
driver.execute_cdp_cmd(cmd, cmd_args)

exit()
#프랙티컬 26426375791,202111
#컴프 26446814568, 112233
pyautogui.hotkey('win', 'd')
pyautogui.hotkey('win', 'r')
pyautogui.typewrite("C:\Program Files (x86)\WebEx\Webex\Applications\ptoneclk.exe", interval=0.01)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(1600,250,1,0)
pyautogui.hotkey('ctrl', 'a')
pyautogui.typewrite(meeting_room_number, interval=0.01)
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(1290,840,1,0)
time.sleep(1)
pyautogui.click(1120,820,1,0)
# pyautogui.press('enter')
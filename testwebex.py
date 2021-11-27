
import pyautogui
import time
import datetime
from selenium import webdriver
class Classes:
    def __init__(self):
        self.professor = ""
        self.email = ""
        self.start_hour = 0
        self.start_minute = 0
        self.start_second = 0
    def setvalue(self,professor,email,start_hour,start_minute,start_second):
        self.professor = professor
        self.email = email
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.start_second = start_second
test = []
test.append(Classes())
print(test[0].setvalue("John Buckley 존버클리[외국어교육부]", email, start_hour, start_minute, start_second))

while True:
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    print(hour,minute,second)
    if hour == start_h and minute == start_m and second == start_m:
        break
    break

options = webdriver.ChromeOptions()
# options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome('chromedriver.exe',options=options)
driver.implicitly_wait(5)

driver.get(url='https://donggukuniv.webex.com/webappng/sites/donggukuniv/meeting/home')
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/button[1]").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[1]/div[1]/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[1]/div[1]/input").send_keys("2021212816@dongguk.ac.kr")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/button").click()
driver.find_element_by_xpath("/html/body/div[1]/form/div/ul/li[1]/input").click()
driver.find_element_by_xpath("/html/body/div[1]/form/div/ul/li[1]/input").send_keys("2021212816@dongguk.ac.kr")
driver.find_element_by_xpath("/html/body/div[1]/form/div/ul/li[2]/input").click()
driver.find_element_by_xpath("/html/body/div[1]/form/div/ul/li[2]/input").send_keys("lh984988")
driver.find_element_by_xpath("/html/body/div[1]/form/div/span/a").click()
cnt = 1
while True:
    try:
        print(driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/ul/li["+str(cnt)+"]/div[3]/div[2]/span").text)
        cnt += 1
    except:
        break
for i in range(1,cnt+1):
    temp = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/ul/li["+str(i)+"]/div[3]/div[2]/span").text
    if temp == professor:
        print(temp)
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/ul/li["+str(i)+"]").click()
        break
meeting_number = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/dl/dd[2]/span").text
meeting_pass = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/dl/dd[3]").text
print(meeting_number)
print(meeting_pass)
driver.close()
while True:
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    if hour == 9 and minute == 0 and second == 0:
        break
    break

pyautogui.hotkey('win', 'd')
pyautogui.hotkey('win', 'r')
pyautogui.typewrite("C:\Program Files (x86)\WebEx\Webex\Applications\ptoneclk.exe", interval=0.01)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(1600,250,1,0)
pyautogui.hotkey('ctrl', 'a')
pyautogui.typewrite(meeting_number, interval=0.01)
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(1290,840,1,0)
time.sleep(1)
pyautogui.click(1120,820,1,0)
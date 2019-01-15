import logging
import time

from PIL import Image, ImageEnhance

import pytesseract
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(pathname)s ::: %(message)s', level=logging.INFO)

downloaddir = "/media/bladrome/backup/demchina"


def get_auth_code(driver, codeEelement):
    driver.save_screenshot('login/login.png')
    imgSize = codeEelement.size
    imgLocation = codeEelement.location
    rangle = (int(imgLocation['x']), int(imgLocation['y']), int(
        imgLocation['x'] + imgSize['width']), int(imgLocation['y']+imgSize['height']))  # 计算验证码整体坐标
    login = Image.open("login/login.png")
    frame4 = login.crop(rangle)
    frame4.save('login/authcode.png')
    authcodeImg = Image.open('login/authcode.png')
    authCodeText = pytesseract.image_to_string(authcodeImg).strip()

    return authCodeText

# display = Display(visible=0, size=(800, 600))
# display.start()


chromeOptions = Options()
prefs = {"download.default_directory": downloaddir}
chromeOptions.add_experimental_option("prefs", prefs)

# browser = webdriver.PhantomJS()
browser = webdriver.Chrome(options=chromeOptions)
# browser = webdriver.Firefox()

browser.get("http://www.gscloud.cn/accounts/login")

useridinput = browser.find_element_by_id("userid")
useridinput.send_keys(input("your id:"))

passwdinput = browser.find_element_by_id("password")
passwdinput.send_keys(input("your passwd:"))

vericodeinput = browser.find_element_by_id("id_captcha_1")

vericodeimg = browser.find_element_by_class_name("captcha")
vericode = get_auth_code(browser, vericodeimg)
print(vericode)

# # Brute force? Not good
# while not vericode and len(vericode) < 4 and not vericode.isalpha():
#     vericode = get_auth_code(browser, vericodeimg)
#     print(vericode)
#     vericodeimg = browser.find_element_by_class_name("captcha")
#     vericodeimg.click()

vericodeinput.send_keys(input("code:"))

logginbtn = browser.find_element_by_class_name("btn")
logginbtn.click()

time.sleep(2)

demdatabtn = browser.find_element_by_link_text("DEM数字高程数据")
demdatabtn.click()

time.sleep(2)

demdatalist = browser.find_elements_by_link_text("数据列表")[3]
demdatalist.click()

time.sleep(2)

i = 1
for longitude in range(9, 55):
    for latitude in range(140, 141):
        # dataid = ASTGTM2_N00E006
        dataid = "ASTGTM2_N{:02}E{:03}\n".format(longitude, latitude)
        dataidinput = browser.find_element_by_css_selector(
            "#all_datasets_listview > div > table > tbody > tr.dlv-filter > td:nth-child(2) > div > input[type=\"text\"]")
        dataidinput.send_keys(dataid)
        time.sleep(1)
        try:
            browser.find_element_by_css_selector(
                "#all_datasets_listview > div > table > tbody > tr.dlv-row.dlv-row-0 > td:nth-child(9) > div > div > a:nth-child(2)").click()
        except:
            dataidinput.clear()
            continue
        dataidinput.clear()
        logging.info("{} filename:{}/{}.zip".format(i,
                                                    downloaddir, dataid.strip()))
        i = i + 1


time.sleep(30 * 1000)
browser.close()

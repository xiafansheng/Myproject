#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 10:33
# @Author  : Xu
# @Software: PyCharm Community Edition

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytesseract
import re
from PIL import Image
import calendar
import time

def init_spider(keyword):

    url = 'http://index.baidu.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    cookieList = []
    for cookie in cookieList:
        driver.add_cookie(cookie)
    driver.get(url)
    time.sleep(3)
    driver.refresh()
    #ÊäÈë¹Ø¼ü´Ê
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='search-input']")))
    driver.find_element_by_xpath("//input[@class='search-input']").send_keys(keyword)
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='search-input-cancle']")))
    driver.find_element_by_xpath("//span[@class='search-input-cancle']").click()
    driver.maximize_window()
    return driver

def aveIndex(driver):

    time.sleep(1)
    WebDriverWait(driver, 10, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='tabLi gColor1']")))
    driver.find_element_by_xpath("//a[@class='tabLi gColor1']").click()
    time.sleep(3)
    driver.save_screenshot('so.png')
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="auto_gsid_5"]/div[3]/table/tbody/tr[2]/td[2]/div/span[1]')))
    element=driver.find_element_by_xpath('//*[@id="auto_gsid_5"]/div[3]/table/tbody/tr[2]/td[2]/div/span[1]')
    # »úÆ÷Ê¶±ðÍ¼Æ¬
    image = Image.open("so.png")
    left = element.location.get("x")+20
    top = element.location.get("y")
    right = left + element.size.get("width")+10
    bottom = top + element.size.get("height")
    cropImg = image.crop((left, top, right, bottom))
    cropImg=cropImg.resize((200,20))
    cropImg.save("aveIndex.png")
    number=Image.open('aveIndex.png')
    number=pytesseract.image_to_string(number)

    number=re.sub(r',?\.?\s?:?','',number)
    print(number)

    #Ê±¼ä¶Î
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='blkUnit grpUnit']//span[@class='compInfo'][2]")))
    datetime = driver.find_element_by_xpath("//div[@class='blkUnit grpUnit']//span[@class='compInfo'][2]").text
    print(datetime)
    return number,datetime

def getElementImage(driver,element,fromPath,toPath,keyword):

    # ÕÒµ½Í¼Æ¬×ø±ê
    locations = element.location
    # ¿çä¯ÀÀÆ÷¼æÈÝ
    scroll = driver.execute_script("return window.scrollY;")
    top = locations['y'] - scroll
    # ÕÒµ½Í¼Æ¬´óÐ¡
    sizes = element.size
    # ¹¹Ôì¹Ø¼ü´Ê³¤¶È
    add_length = (len(keyword) - 2) * sizes['width'] / 15
    # ¹¹ÔìÖ¸ÊýµÄÎ»ÖÃ
    rangle = (
        int(locations['x'] + sizes['width'] / 4 + add_length)-2, int(top + sizes['height'] / 2),
        int(locations['x'] + sizes['width'] * 2 / 3)+2, int(top + sizes['height']))
    time.sleep(2)
    image = Image.open(fromPath)
    cropImg = image.crop(rangle)
    cropImg.save(toPath)

def dailyIndex(driver,x,y,index):
    time.sleep(2)
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#trend > svg > rect')))
    element = driver.find_elements_by_css_selector('#trend > svg > rect')[1]
    time.sleep(2)
    ActionChains(driver).move_to_element_with_offset(element, x, y).perform()
    cot = 0   #viewbox²»³öÏÖ
    while (ExistBox(driver) == False):
        cot += 1
        time.sleep(2)
        y=y+10
        dailyIndex(driver, x, y, index)
        if ExistBox(driver) == True:
            break
        if cot == 6:
            return None
    time.sleep(3)
    driver.get_screenshot_as_file(str(index)+'.png')

    try:
        WebDriverWait(driver, 10, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='viewbox']")))
        datetime=driver.find_element_by_xpath('//*[@id="viewbox"]/div[1]/div[1]').text
        print(datetime)
    except:
        print('´ÎÊýÓÐÎó£¡')
    finally:
        element = driver.find_element_by_xpath("//div[@id='viewbox']")
        getElementImage(driver,element, str(index)+'.png', 'day'+str(index)+'.png',keyword)
        time.sleep(2)
        number = Image.open('day'+str(index)+'.png')
        number = pytesseract.image_to_string(number,lang='fontyp')
        number = re.sub(r',?\.?\s?', '', number)
        number=number.replace('z','2').replace('i','7').replace('e','9')
        print(number)
        return number



def ExistBox(driver):
    try:
        WebDriverWait(driver, 10, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='viewbox']")))
        return True
    except:
        return False

def defaultIndex(driver):
    aveindex,datetime=aveIndex(driver)
    width = 41.68
    x1 = [1]
    x2 = [i * width for i in range(1, 30)]
    x = x1 + x2
    cot = 30
    allIndex=[]
    for i in range(len(x)):
        day=dailyIndex(driver, x[i], cot, i)
        allIndex.append(day)
    return allIndex,aveindex,datetime

keyword='特朗普­'
driver = init_spider(keyword)
aveIndex(driver)
defaultIndex(driver)


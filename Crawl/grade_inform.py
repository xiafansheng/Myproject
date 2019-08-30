from sklearn.externals import joblib
import os
import requests
from PIL import Image
import numpy as np
import requests
from selenium import webdriver
import pandas as pd
from pyquery import PyQuery as pq
from Mail.mail import sendmail
import schedule

driver = webdriver.Chrome()

def convert_image(image):
    image=image.convert('L')
    image2=Image.new('L',image.size,255)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pix=image.getpixel((x,y))
            if pix<120:
                image2.putpixel((x,y),0)
    return image2

def cut_image(image):
    inletter=False
    foundletter=False
    letters=[]
    start=0
    end=0
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pix=image.getpixel((x,y))
            if(pix==0):
                inletter=True
        if foundletter==False and inletter ==True:
            foundletter=True
            start=x
        if foundletter==True and inletter==False:
            end=x
            letters.append((start,end))
            foundletter=False
        inletter=False
    images=[]
    for letter in letters:
        img=image.crop((letter[0],0,letter[1],image.size[1]))
        img = img.resize((9, 20), Image.BILINEAR)
        images.append(img)
    return images


def read_yzm(image):
    knn = joblib.load('yzm.pkl')
    #image=Image.open(yzm_path)
    image = convert_image(image)
    images = cut_image(image)[:4]
    string = []
    for j in images:
        m = np.matrix(j.getdata()).tolist()[0]
        yzm = knn.predict([m])
        string.append(str(int(yzm)))
    return ''.join(string)

def get_yzm(self):
    driver.save_screenshot('screenshot.png')
    imgelement = driver.find_element_by_xpath('//*[@id="Image1"]')  # 定位验证码
    location = imgelement.location  # 获取验证码x,y轴坐标
    size = imgelement.size
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))
    i = Image.open("screenshot.png")  # 打开截图
    captcha = i.crop(rangle)
    return captcha

class GetAndInform_grade():
    def __init__(self,username,password,url):
        self.username = username
        self.password = password
        self.url = url

    def get_grade(self):
        driver.get(url)
        yzm_pic = get_yzm(self)
        yzm = read_yzm(yzm_pic)
        driver.find_element_by_xpath('//*[@id="username"]').clear()
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
        driver.find_element_by_xpath('//*[@id="password"]').clear()
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="code1"]').clear()
        driver.find_element_by_xpath('//*[@id="code1"]').send_keys(yzm)
        driver.find_element_by_xpath('//*[@id="ImageButton2"]').click()
        driver.implicitly_wait(0.5)
        driver.get('http://yjsy.cufe.edu.cn/PostGraduate/WitMis_CourseScoreView.aspx')
        driver.implicitly_wait(0.5)
        res = driver.page_source
        return res

    def parse_page(self,res):
        df = pd.read_html(res)[-2]
        course_name = df.ix[:,1].values
        course_score = df.ix[:,8].values
        course_result = {i[0]:i[1] for i in zip(course_name,course_score) if i[0]}
        need_inform_course = ['国际经济学（Ⅱ）','英语','二外日语']
        for course in need_inform_course:
            if course_result[course] != '隐藏':
                inform_result = '你的课程：' + course + '考试结果已出,你的成绩为：' + course_result[course]
                print(inform_result)
                sendmail('课程成绩提醒',inform_result)
            else:
                '此课程当前成绩尚未出'

def main():
    username = 2018210176
    password = 'xiafansheng9619'
    url = 'http://yjsy.cufe.edu.cn/login.aspx'
    mycourse_result = GetAndInform_grade(username,password,url)
    grade = mycourse_result.get_grade()
    inform = mycourse_result.parse_page(grade)

if __name__=='__main__':
    schedule.every().hour.do(main)




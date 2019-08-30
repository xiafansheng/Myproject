#coding:utf-8

import os
import requests
from PIL import Image
import math
import requests
import pytesseract


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
        images.append(img)
    return images

def imagesget():
    #os.mkdir('images')
    count=0
    while True:
        img=requests.get('http://yjsy.cufe.edu.cn/Image.aspx').content
        with open('captcha.jpeg', 'wb') as imgfile:
            imgfile.write(img)
        img = Image.open(img)
        image = convert_image(img)
        images = cut_image(image)
        for i in images:
            with open('images/%s-%s.jpeg'%(count,i),'wb') as imgfile:
                imgfile.write(img)
        count+=1
        if(count==100):
            break
#

# for i in range(1,100):
# session = requests.session()
# session.get('http://yjsy.cufe.edu.cn/').text
# img = session.get('http://yjsy.cufe.edu.cn/Image.aspx').content
# s = pytesseract.image_to_string(img)
# with open('%s.jpeg'%s, 'wb') as imgfile:
#     imgfile.write(img)
# path = '3.jpeg'
# image=Image.open(path)
# image=convert_image(image)
# image.show()

#
# def buildvector(image):
#     result={}
#     count=0
#     for i in image.getdata():
#         result[count]=i
#         count+=1
#     return result
#
#
# class CaptchaRecognize:
#     def __init__(self):
#         self.letters=['0','1','2','3','4','5','6','7','8','9']
#         self.loadSet()
#
#     def loadSet(self):
#         self.imgset=[]
#         for letter in self.letters:
#             temp=[]
#             for img in os.listdir(r'C:\pycharm project\Crawl\CaptchaRecognise\icon\%s'%(letter)):
#                 temp.append(buildvector(Image.open(r'C:\pycharm project\Crawl\CaptchaRecognise\icon\%s\%s'%(letter,img))))
#             self.imgset.append({letter:temp})
#
#     #计算矢量大小
#     def magnitude(self,concordance):
#         total = 0
#         for word,count in concordance.items():
#             total += count ** 2
#         return math.sqrt(total)
#
#     #计算矢量之间的 cos 值
#     def relation(self,concordance1, concordance2):
#         relevance = 0
#         topvalue = 0
#         for word, count in concordance1.items():
#             if word in concordance2:
#                 topvalue += count * concordance2[word]
#         return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))
#
#     def recognise(self,image):
#         image=convert_image(image)
#         images=cut_image(image)
#         vectors=[]
#         for img in images:
#             vectors.append(buildvector(img))
#         result=[]
#         for vector in vectors:
#             guess=[]
#             for image in self.imgset:
#                 for letter,temp in image.items():
#                     relevance=0
#                     num=0
#                     for img in temp:
#                         relevance+=self.relation(vector,img)
#                         num+=1
#                     relevance=relevance/num
#                     guess.append((relevance,letter))
#             guess.sort(reverse=True)
#             result.append(guess[0])
#         return result

# if __name__=='__main__':
#     imageRecognize=CaptchaRecognize()
#     image=Image.open('3.jpeg')
#     result=imageRecognize.recognise(image)
#     string=[''.join(item[1]) for item in result]
#     print(string)
# import pandas as pd
# df = pd.read_csv('finance magazine.csv')
# df.columns= ['index','title','author','year','issue','name']
# print(df['year'].unique())
#
# # coding=utf-8
# __author__ = 'w00*'
#
# import requests
# import chardet
# url = 'http://10.12.162.31/pages/IC/LoginForm.aspx?'
# proxies = {"http": "http://2018210176:xfs9619.@192.168.141.61:443"
#            ,"https": "http://2018210176:xfs9619.@192.168.141.61:443"}
# r = requests.get(url, proxies=proxies)
#
# print(r.status_code)
# print(r.content)
#coding=utf8
import urllib
from urllib.request import urlopen
import requests
import re

url = "http://kimerfly.blogspot.com/2012/10/86-120g.html"
headers = {
    'user-agent': 'Mozilla/5.0'
}
proxies = {
    'https': 'https://127.0.0.1:1080',
    'http': 'http://127.0.0.1:1080'
}
response = requests.get(url, proxies=proxies)
text = response.text
pattern = re.compile(r'ed2k\:\/\/\|file\|.*\|\/')
cinfo = pattern.findall(text)
for i in cinfo:
    with open('a.txt','a+',encoding='utf-8') as f:
	    f.write(str(i) + "\n")
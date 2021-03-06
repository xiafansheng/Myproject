

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pytesseract


# 打开浏览器
def openbrowser():
    global browser
    url = "https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F"
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element_by_id("TANGRAM__PSP_3__userName").clear()
    browser.find_element_by_id("TANGRAM__PSP_3__password").clear()
    account = ['xfs9619','xfs9619']
    browser.find_element_by_id("TANGRAM__PSP_3__userName").send_keys(account[0])
    browser.find_element_by_id("TANGRAM__PSP_3__password").send_keys(account[1])
    browser.find_element_by_id("TANGRAM__PSP_3__submit").click()
    print("等待网址加载完毕...")
    select = input("请观察浏览器网站是否已经登陆(y/n)：")
    while 1:
        if select == "y" or select == "Y":
            print("登陆成功！")
            print("准备打开新的窗口...")
            break

        elif select == "n" or select == "N":
            selectno = input("账号密码错误请按0，验证码出现请按1...")
            # 账号密码错误则重新输入
            if selectno == "0":

                # 找到id="TANGRAM__PSP_3__userName"的对话框
                # 清空输入框
                browser.find_element_by_id("TANGRAM__PSP_3__userName").clear()
                browser.find_element_by_id("TANGRAM__PSP_3__password").clear()

                # 输入账号密码
                account = []
                try:
                    fileaccount = open("../baidu/account.txt", encoding='UTF-8')
                    accounts = fileaccount.readlines()
                    for acc in accounts:
                        account.append(acc.strip())
                    fileaccount.close()
                except Exception as err:
                    print(err)
                    input("请正确在account.txt里面写入账号密码")
                    exit()

                browser.find_element_by_id("TANGRAM__PSP_3__userName").send_keys(account[0])
                browser.find_element_by_id("TANGRAM__PSP_3__password").send_keys(account[1])
                # 点击登陆sign in
                # id="TANGRAM__PSP_3__submit"
                browser.find_element_by_id("TANGRAM__PSP_3__submit").click()

            elif selectno == "1":
                # 验证码的id为id="ap_captcha_guess"的对话框
                input("请在浏览器中输入验证码并登陆...")
                select = input("请观察浏览器网站是否已经登陆(y/n)：")

        else:
            print("请输入“y”或者“n”！")
            select = input("请观察浏览器网站是否已经登陆(y/n)：")


def getindex(keyword, day):
    openbrowser()
    time.sleep(2)
    js = 'window.open("http://index.baidu.com");'
    browser.execute_script(js)
    handles = browser.window_handles
    browser.switch_to_window(handles[-1])
    time.sleep(5)
    browser.find_element_by_id("schword").clear()
    browser.find_element_by_id("schword").send_keys(keyword)
    browser.find_element_by_id("searchWords").click()
    time.sleep(5)
    browser.maximize_window()
    time.sleep(2)
    sel = '//a[@rel="' + str(day) + '"]'
    browser.find_element_by_xpath(sel).click()
    time.sleep(2)
    # 滑动思路：http://blog.sina.com.cn/s/blog_620987bf0102v2r8.html
    # 滑动思路：http://blog.csdn.net/zhouxuan623/article/details/39338511
    # 向上移动鼠标80个像素，水平方向不同
    # ActionChains(browser).move_by_offset(0,-80).perform()
    # <div id="trend" class="R_paper" style="height:480px;_background-color:#fff;"><svg height="460" version="1.1" width="954" xmlns="http://www.w3.org/2000/svg" style="overflow: hidden; position: relative; left: -0.5px;">
    # <rect x="20" y="130" width="914" height="207.66666666666666" r="0" rx="0" ry="0" fill="#ff0000" stroke="none" opacity="0" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0;"></rect>
    # xoyelement = browser.find_element_by_xpath('//rect[@stroke="none"]')
    xoyelement = browser.find_elements_by_css_selector("#trend rect")[2]
    num = 0
    # 获得坐标长宽
    # x = xoyelement.location['x']
    # y = xoyelement.location['y']
    # width = xoyelement.size['width']
    # height = xoyelement.size['height']
    # print(x,y,width,height)
    # 常用js:http://www.cnblogs.com/hjhsysu/p/5735339.html
    # 搜索词：selenium JavaScript模拟鼠标悬浮
    x_0 = 1
    y_0 = 0

    if day == "all":
        day = 1000000

    # 储存数字的数组
    index = []
    try:
        # webdriver.ActionChains(driver).move_to_element().click().perform()
        # 只有移动位置xoyelement[2]是准确的
        for i in range(day):
            # 坐标偏移量???
            ActionChains(browser).move_to_element_with_offset(xoyelement, x_0, y_0).perform()

            # 构造规则
            if day == 7:
                x_0 = x_0 + 202.33
            elif day == 30:
                x_0 = x_0 + 41.68
            elif day == 90:
                x_0 = x_0 + 13.64
            elif day == 180:
                x_0 = x_0 + 6.78
            elif day == 1000000:
                x_0 = x_0 + 3.37222222
            time.sleep(2)
            # <div class="imgtxt" style="margin-left:-117px;"></div>
            imgelement = browser.find_element_by_xpath('//div[@id="viewbox"]')
            # 找到图片坐标
            locations = imgelement.location
            # 跨浏览器兼容
            scroll = browser.execute_script("return window.scrollY;")
            top = locations['y'] - scroll
            # 找到图片大小
            sizes = imgelement.size
            # 构造关键词长度
            add_length = (len(keyword) - 2) * sizes['width'] / 15
            # 构造指数的位置
            rangle = (
            int(locations['x'] + sizes['width'] / 4 + add_length), int(top + sizes['height'] / 2),
            int(locations['x'] + sizes['width'] * 2 / 3), int(top + sizes['height']))
            # 截取当前浏览器
            path = "../baidu/" + str(num)
            browser.save_screenshot(str(path) + ".png")
            # 打开截图切割
            img = Image.open(str(path) + ".png")
            jpg = img.crop(rangle)
            jpg.save(str(path) + ".jpg")

            # 将图片放大一倍
            # 原图大小73.29
            jpgzoom = Image.open(str(path) + ".jpg")
            (x, y) = jpgzoom.size
            x_s = 146
            y_s = 58
            out = jpgzoom.resize((x_s, y_s), Image.ANTIALIAS)
            out.save(path + 'zoom.jpg', 'png', quality=95)

            # 图像识别
            try:
                image = Image.open(str(path) + "zoom.jpg")
                code = pytesseract.image_to_string(image)
                if code:
                    index.append(code)
                else:
                    index.append("")
            except:
                index.append("")
            num = num + 1

    except Exception as err:
        print(err)
        print(num)

    print(index)
    # 日期也是可以图像识别下来的
    # 只是要构造rangle就行，但是我就是懒
    file = open("../baidu/index.txt", "w")
    for item in index:
        file.write(str(item) + "\n")
    file.close()


if __name__ == "__main__":
    # 每个字大约占横坐标12.5这样
    # 按照字节可自行更改切割横坐标的大小rangle
    keyword = input("请输入查询关键字：")
    sel = int(input("查询7天请按0，30天请按1，90天请按2，半年请按3，全部请按4："))
    day = 0
    if sel == 0:
        day = 7
    elif sel == 1:
        day = 30
    elif sel == 2:
        day = 90
    elif sel == 3:
        day = 180
    elif sel == 4:
        day = "all"
    getindex(keyword, day)
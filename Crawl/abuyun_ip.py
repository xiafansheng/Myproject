import requests
from selenium import webdriver

def get_page(url):
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"
    proxyUser = "HSA14D96OZ0V6LVD"
    proxyPass = "8741E842355CBF33"
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }
    proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }
    resp = requests.get(url, proxies=proxies)
    #print(resp.status_code)
    pagesource = resp.text
    return pagesource


def get_page_selenium(url):
    driver = webdriver.PhantomJS()
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"
    proxyUser = "H1X078RX5J171Z5D"
    proxyPass = "16259B73C47D4A34"
    service_args = [
        "--proxy-type=http",
        "--proxy=%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
        },
        "--proxy-auth=%(user)s:%(pass)s" % {
            "user": proxyUser,
            "pass": proxyPass,
        },
    ]
    driver = webdriver.Chrome(service_args=service_args)
    driver.get(url)
    data = driver.page_source
    return data
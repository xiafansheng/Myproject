# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
import json
from Crawl.get_cookie_header import get_headers


url = 'https://dataweb.usitc.gov/trade/search/Import/HTS'
urls = 'https://datawebws.usitc.gov/dataweb/api/v1/report2/dataExport'
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath('/html/body/dw-root/dw-layout/div/div/div/dw-login/main/article/div/div[1]/form/div[2]/div/input').clear()
driver.find_element_by_xpath('/html/body/dw-root/dw-layout/div/div/div/dw-login/main/article/div/div[1]/form/div[2]/div/input').send_keys('xfs9619')
driver.find_element_by_xpath('/html/body/dw-root/dw-layout/div/div/div/dw-login/main/article/div/div[1]/form/div[3]/div/input').clear()
driver.find_element_by_xpath('/html/body/dw-root/dw-layout/div/div/div/dw-login/main/article/div/div[1]/form/div[3]/div/input').send_keys('@Xfs9619')
driver.find_element_by_xpath('/html/body/dw-root/dw-layout/div/div/div/dw-login/main/article/div/div[1]/form/div[4]/button').click()
driver.get_cookies()

# cookie = driver.get_cookies()
#
# payloadData = {
#   "jsonInput": 'null',
#   "savedQueryID": 'null',
#   "savedQueryName": 'null',
#   "savedQueryDesc": 'null',
#   "reportOptions": {
#     "tradeType": "Import",
#     "classificationSystem": "HTS"
#   },
#   "searchOptions": {
#     "componentSettings": {
#       "dataToReport": [
#         "CONS_CUSTOMS_VALUE"
#       ],
#       "scale": "1",
#       "years": [
#         "2017"
#       ],
#       "yearsTimeline": "Annual"
#     },
#     "commodities": {
#       "commodities": [],
#       "commoditiesManual": 'null',
#       "searchGranularity": 2,
#       "commoditiesChapter": 'nul',
#       "commodityGroups": {
#         "systemGroups": [],
#         "userGroups": []
#       },
#       "commodityGroupNameInput": 'null',
#       "commoditySelectType": "all",
#       "granularity": "2",
#       "aggregation": "Aggregate Commodities",
#       "codeDisplayFormat": "NO"
#     },
#     "countries": {
#       "countries": [],
#       "countryGroups": {
#         "systemGroups": [],
#         "userGroups": []
#       },
#       "countriesSelectType": "all",
#       "aggregation": "Aggregate countries"
#     },
#     "MiscGroup": {
#       "importPrograms": {
#         "importPrograms": [],
#         "aggregation": "Aggregate CSC",
#         "programsSelectType": "all"
#       },
#       "extImportPrograms": {
#         "extImportPrograms": [],
#         "aggregation": "Aggregate CSC2"
#       },
#       "provisionCodes": {
#         "rateProvisionCodes": [],
#         "aggregation": "Aggregate RPCODE",
#         "provisionCodesSelectType": "all"
#       },
#       "districts": {
#         "districts": [],
#         "aggregation": "Aggregate District",
#         "districtGroups": {
#           "userGroups": []
#         },
#         "districtsSelectType": "all"
#       }
#     }
#   },
#   "sortingAndDataFormat": {
#     "DataSort": {
#       "sortOrder": [],
#       "columnOrder": [],
#       "fullColumnOrder": [],
#       "sortYear": 'null',
#       "sortYearValue": 'null'
#     },
#     "reportCustomizations": {
#       "totalRecords": "5000",
#       "showAllSubtotal": 'true',
#       "enableSubtotals": 'false',
#       "displayCommodityList": 'false',
#       "reportsFontSize": "m",
#       "displayPercentChange": 'true'
#     }
#   }
# }
# text = 'Host: datawebws.usitc.gov\
#         Connection: keep-alive\
#         Content-Length: 2085\
#         Timeout: 540000\
#         Origin: https://dataweb.usitc.gov\
#         Authorization: Basic WElBRkFOU0hFTkc6QFhGUzk2MTk=\
#         content-type: application/json\
#         Accept: application/json, text/plain, */*\
#         User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36\
#         Referer: https://dataweb.usitc.gov/trade/search\
#         Accept-Encoding: gzip, deflate, br\
#         Accept-Language: zh-CN,zh;q=0.9,en;q=0.8'
# headers = get_headers(text)
# cookies = {}
# for cook in cookie:
#     cookies[cook['name']] = cook['value']
# result = requests.post(urls,data=json.dumps(payloadData),headers = headers,cookies =cookies)
# print(result)
#

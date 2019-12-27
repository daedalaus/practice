# mystr = '''\
# t=4cbbabc07c48e5c58c92d151bad52053; cna=A7QVFkeQzEgCAbSkfDf265lS; thw=cn; uc3=id2=Uoe9bFIZMAAUaw%3D%3D&vt3=F8dByuDnymtK4hhEbjw%3D&nk2=0RI5S1x6dwo%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; lgc=%5Cu6B8B%5Cu9633%5Cu5BD2%5Cu98CE; tracknick=%5Cu6B8B%5Cu9633%5Cu5BD2%5Cu98CE; _cc_=WqG3DMC9EA%3D%3D; tg=0; enc=Y3CpfRg3b8lNgd6zQf8w%2BTi3m%2BWx4ObBOI%2BeKGWLW7tmfNWu34VCjFboS1ZJv2tT%2F3FVRcsck9vZTX%2FnnfytFw%3D%3D; mt=ci=53_1; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; cookie2=16de08bdbda9f42d3c1a4f50202bc29a; _tb_token_=3367e38883737; JSESSIONID=57A98DC607BBE756667FE335576F6E9B; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; uc1=cookie14=UoTbnV%2BARYtTHg%3D%3D; l=cBMX9rEeq4tEEE8vBOfZKurza77T4QAf11FzaNbMiICP_wCM511CWZIveYYHCnGVKsGH73oTJ-juBf8NiyCqJxpswAaZk_f..; isg=BI2N1rtX7MzP1Ejbd2TSrq-8nKkHasE8HsplhM8QdSSTxqh4n7kkDL4UNFqgQdn0'''
# cookie_dict = {}
# items = mystr.split(';')
# for item in items:
#     key, value = item.strip().split('=', 1)
#     cookie_dict[key] = value
# print(cookie_dict)

# import requests
# response = requests.get('https://s.taobao.com/search?q=ipad', cookies=cookie_dict)
# print(response.status_code)
# print(response.text)

import json

from selenium.webdriver import Chrome, PhantomJS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = Chrome()
# browser = PhantomJS()
wait = WebDriverWait(browser, 60)
# browser.add_cookie({'name': 'hng', 'value': 'CN%7Czh-CN%7CCNY%7C156'})
browser.get('https://www.taobao.com/')
input_el = browser.find_element_by_id('q')
input_el.clear()
input_el.send_keys('ipad')
submit_el = browser.find_element_by_css_selector('.btn-search.tb-bg')
submit_el.click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form>span.btn.J_Submit')))
cookies = browser.get_cookies()
print(cookies)
with open('cookies-11-9.json', 'w', encoding='utf-8') as fp:
    json.dump(cookies, fp)



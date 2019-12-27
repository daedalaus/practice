from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')


# 错误 logo = browser.find_element_by_class_name('Icon ZhihuLogo ZhihuLogo--blue Icon--logo')
# logo = browser.find_element_by_xpath('//*[@class="Icon ZhihuLogo ZhihuLogo--blue Icon--logo"]')
# print(logo)
# print(logo.get_attribute('class'))


input_el = browser.find_element_by_id('Popover1-toggle')
print(input_el.id)
print(input_el.location)
print(input_el.tag_name)
print(input_el.size)




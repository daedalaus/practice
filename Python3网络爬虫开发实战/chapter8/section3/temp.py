# from selenium import webdriver
# import time
# from PIL import Image
# url = "https://www.baidu.com"
# driver = webdriver.Chrome()
# driver.get(url)
# driver.maximize_window()#全屏
# driver.implicitly_wait(10)
# driver.save_screenshot("baidu.png")#截取全屏
# element = driver.find_element_by_id('su') #定位百度一下搜索按钮
# xpoint = element.location['x']
# ypoint = element.location['y']
# element_width = xpoint + element.size['width']
# element_high = ypoint + element.size['height']
# picture = Image.open("baidu.png")
# pic = picture.crop((xpoint, ypoint, element_width, element_high))
# pic.save("baidu_bbb.png")
# driver.quit()
# element.get_attribute()

3083122313174500012
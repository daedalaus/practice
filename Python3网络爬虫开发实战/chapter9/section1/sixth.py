from selenium import webdriver

service_args = [
    '--proxy=47.103.138.66:8050',
    '--proxy-type=http',
    '--proxy-auth=feiyu:123456'
]
browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
print(browser.page_source)

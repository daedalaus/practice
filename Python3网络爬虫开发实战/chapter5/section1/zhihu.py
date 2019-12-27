import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
# html = requests.get(url, headers=headers).text
# doc = pq(html)
# items = doc('div.ExploreCollectionCard-contentItem').items()
# for item in items:
#     question = item.find('a').text()
#     answer = item('div.ExploreCollectionCard-contentExcerpt').text()
#     agree = item.find('div.ExploreCollectionCard-contentTags>span:nth-child(2)').text()
#     comment = item.find('div.ExploreCollectionCard-contentTags>span:last-child').text()
#     with open('explore.txt', 'a', encoding='utf-8') as f:
#         f.write('\n'.join([question, answer, agree, comment]))
#         f.write('\n' + '=' * 50 + '\n')


# with open('demo.txt', 'a') as f:
#     print(f.read())
#
# with open('hello.txt', 'r+') as g:
#     g.write('hello65656')

import json

my_str = '''
[{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
'''
obj = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]
# data = json.loads(my_str)
json_str = json.dumps(obj, indent=2, ensure_ascii=False)
print(type(json_str))
print(json_str)
with open('hello.txt', 'w', encoding='utf-8') as f:
    f.write(json_str)

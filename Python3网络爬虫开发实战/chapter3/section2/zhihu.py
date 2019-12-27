import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0'
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
# r = requests.get('https://www.zhihu.com/explore')
print(r.text)
pattern = re.compile('ExploreSpecialCard-contentTitle.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

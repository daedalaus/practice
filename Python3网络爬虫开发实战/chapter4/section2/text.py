import re

html = """
<div class="panel">
<div class="panel-body">
<a>Hello, this is a link</a>
</div>
</div>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text=re.compile(r'link$')))
# print(type(soup.find_next_siblings()))
# print(len(soup.find_next_siblings()))
# print(soup.find_next_siblings())

# print(type(soup.find_parents(name='span')))
# print(list(enumerate(soup.find_parents(name='span'))))
#
# span = soup.find(name='span')
# print(type(span.find_parents()))
# print(list(enumerate(span.find_parents())))

print(soup.p.children)

for i, tag in enumerate(soup.p.children):
    print(i, ":", type(tag))
    if i == 0:
        print(tag.find_parents())
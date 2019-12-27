#! /usr/bin/env python
# -*- coding:utf-8 -*-

html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')))
# print(type(soup.find_all(name='ul')[0]))
# print(list(enumerate(soup.find_all(name='ul')[0].children)))

# print(type(soup.find_all(attrs={'id': 'list-1'})))
# print(soup.find_all(attrs={'class': 'element'}))

# print(soup.find_all(id='list-1'))
# print(soup.find_all(name='elements'))

# print(soup.select('.panel .panel-heading'))
# print(type(soup.select('.panel .panel-heading')))
#
# # print(soup.select('ul li'))
# print(type(soup.select('ul li')))
# print(soup.select('#list-2 .element'))
# print(type(soup.select('ul')[0]))
# print(type(soup.select('#list-1')))

for li in soup.select('li'):
    print('Get Text: ', li.get_text())
    print('String: ', li.string)

print('---')
print(type(li))
import html.parser
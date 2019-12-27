#! /usr/bin/env python
# -*- coding:utf-8 -*-

html = """
<html>
<body>
<p class="story">
         Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>h
          Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
          and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
        and they lived at the bottom of a well.
        </p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print('Next sibling', soup.a.next_sibling)
# print('Previous sibling', soup.a.previous_sibling)
# print('Next siblingssss', list(enumerate(soup.a.next_siblings)))
# print('Previous siblingssss', list(enumerate(soup.a.previous_siblings)))

print(type(soup.a.next_siblings))
print(next(soup.a.next_siblings))
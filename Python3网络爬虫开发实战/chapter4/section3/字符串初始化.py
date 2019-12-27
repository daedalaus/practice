from pyquery import PyQuery as pq

html = """
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
"""

# doc = pq(html)
# print(doc('li'))
# print(type(doc('li')))

# doc2 = pq(url='https://cuiqingcai.com')
# print(doc2('title'))

# doc3 = pq(filename='./demo.html')
# print(doc3('li'))


html1 = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html">outer<span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
"""

doc = pq(html1)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

items = doc('.list')
# print(type(items))
# print(items)

# lis = items.find('li')
# print(type(lis))
# print(lis)

# lis2 = items.children('.active')
# print(lis2)

# container = items.parent()
# print(type(container))
# print(container)

parents = items.parents()
# print(type(parents))
# print(parents)
# print(len(parents))

# parents2 = items.parents('.wrap')
# print(len(parents2))
# print(parents2)

# li = doc('.list .item-0.active')
# print(type(li.siblings('.active')))
# print(len(li.siblings('.active')))
# print(li.siblings('.active'))

# a = doc('.list .item-0.active a')
# print(type(a))
# print(a.attr('href'))
# print(a.attr.href)

# a = doc('a')
# print(len(a))
# print(a)
#
# print(a.attr.href)

# container = doc('#container')
# print(len(container))
# for i in container.items():
#     print("hel")

# a = doc('.item-0.active a')
# print(a)
# print(a.text())
# print(a.html())

html1 = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html">outer<span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
"""

# doc2 = pq(html1)
# li = doc2('li')
# print(li.html())
# print(li.text())
# print(type(li.text()))
# print(type(li.html()))

# doc3 = pq(html1)
# li = doc3('.item-0.active')
# print(li)
# li.remove_class('active')
# print(li)
# li.add_class('active')
# print(li)

html4 = """
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
"""

doc4 = pq(html4)
# li = doc4('.item-0.active')
# print(li, end='')
# li.attr('name', 'link')
# print(li, end='')
# # li.attr('age', '22', 'hg', 'haha')
# li.attr(('age', '20'), ('hg', 'haha'))
# li.text('change item')
# print(li, end='')
# li.html('<span>changed item</span>')
# print(li, end='')

# ul = doc4('ul')
# li = ul.find('li')
# print(li)
# li.attr('name', 'link')
# print(li)
# print(ul('li'))

html5 = """
<div class="outer">
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
</div>
</div>
"""
doc5 = pq(html5)
outer = doc5('.outer')
# print(outer.text())
# print(outer.html())
outer.find('p').remove()
print(outer.text())
print(outer.html())

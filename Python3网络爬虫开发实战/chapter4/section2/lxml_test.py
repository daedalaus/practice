from lxml import etree

text = '''
<div>
<ul>
<li class="item-0" name="hello"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

html = etree.HTML(text)
print(type(html))
ul_el = html.xpath('.//ul')[0]
print(type(ul_el))
lis = ul_el.xpath('li')
print(type(lis))
print(lis)
li = lis[1]
a = li.xpath('./a')
print(type(a))
print(a)



#
# result2 = html.xpath('//li[last()]/a/text()')
# print(result2)
#
# result3 = html.xpath('//li[position()<3]/a/text()')
# print(result3)
#
# result4 = html.xpath('//li[last()-2]/a/text()')
# print(result4)

#
# result1 = html.xpath('//li[1]/ancestor::*')
# print(result1)
#
# result2 = html.xpath('//li[1]/ancestor::div')
# print(result2)
#
# result3 = html.xpath('//li[1]/attribute::*')
# print(result3)
#
# result4 = html.xpath('//li[1]/child::a[@href="link1.html"]')
# print(result4)
#
# r4 = html.xpath('//li[1]/parent::*')
# print(r4)
#
# result5 = html.xpath('//li[1]/descendant::span')
# print(result5)
#
# result6 = html.xpath('//li[1]/following::*[2]')
# print(result6)
#
# result8 = html.xpath('//li[3]/preceding::*[3]')
# print(result8)
#
# result7 = html.xpath('//li[2]/preceding-sibling::*/a/span/text()')
# print(result7)
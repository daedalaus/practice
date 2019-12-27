from lxml import etree

with open('github.html', encoding='utf-8') as f:
    content = f.read()

html = etree.HTML(content)

text = html.xpath('//div[contains(@class, "news")]')
print(text)


# text = selector.xpath('//div[contains(@class, "news")]/text()')
# print('text is -->', text)


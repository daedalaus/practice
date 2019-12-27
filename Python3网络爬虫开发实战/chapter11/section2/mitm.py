import json
import pymongo
import requests
from mitmproxy import ctx


# def request(flow):
#     flow.request.headers['User-Agent'] = 'MitmProxy'
#     ctx.log.info(str(flow.request.headers))
#     ctx.log.warn(str(flow.request.headers))
#     ctx.log.error(str(flow.request.headers))


# def request(flow):
#     request = flow.request
#     info = ctx.log.info
#     info(request.url)
#     info(str(request.headers))
#     info(str(request.cookies))
#     info(request.host)
#     info(request.method)
#     info(str(request.port))
#     info(request.scheme)


# def response(flow):
#     response = flow.response
#     info = ctx.log.info
#     info(str(response.status_code))
#     info(str(response.headers))
#     info(str(response.cookies))
#     info(str(response.text))


# def response(flow):
#     print(flow.request.url)
#     print(flow.response.text)


# def response(flow):
#     url = 'https://entree.igetget.com/ebook2/v1/ebook/list'
#     if flow.request.url.startswith(url):
#         text = flow.response.text
#         data = json.loads(text)
#         books = data.get('c').get('list')
#         for book in books:
#             ctx.log.info('======='+str(book)+'=======')


# class MyMongoClient(pymongo.MongoClient):
#     def __call__(self, *args, **kwargs):
#         print('call method called', 'args:', args, '<-->kwargs', kwargs)


# client = pymongo.MongoClient('localhost')
#
# db = client.igetget
# collection = db.books


def response(flow):
    # global collection
    url = 'https://entree.igetget.com/ebook2/v1/ebook/list'
    if flow.request.url.startswith(url):
        text = flow.response.text
        with open('text.txt', 'a', encoding='utf-8') as f:
            f.write(text)
        requests.post('http://127.0.0.1:5000', data=text.encode('utf-8'))
        data = json.loads(text)
        books = data.get('c').get('list')
        for book in books:
            item = {
                'title': book.get('operating_title'),
                'cover': book.get('cover'),
                'summary': book.get('other_share_title'),
                'price': book.get('price')
            }
            ctx.log.info(str(item))
            # collection.insert(item)


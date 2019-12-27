import json
import pymongo
import requests
from mitmproxy import ctx


# class MyMongoClient(pymongo.MongoClient):
#     def __call__(self, *args, **kwargs):
#         print('call method called', 'args:', args, '<-->kwargs', kwargs)


client = pymongo.MongoClient('localhost')

db = client.igetget
collection = db.books


def response(flow):
    # global collection
    url = 'https://entree.igetget.com/ebook2/v1/ebook/list'
    if flow.request.url.startswith(url):
        text = flow.response.text
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
            collection.insert(item)


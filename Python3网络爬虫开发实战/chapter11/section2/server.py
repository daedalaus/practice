from flask import Flask, g, request
import pymongo
import json

client = pymongo.MongoClient('localhost')
db = client['igetget']
collection = db['books']


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.data
        print(data.decode('utf-8'))
        json_data = json.loads(data.decode('utf-8'))
        books = json_data.get('c').get('list')
        for book in books:
            item = {
                'title': book.get('operating_title'),
                'cover': book.get('cover'),
                'summary': book.get('other_share_title'),
                'price': book.get('price')
            }
            collection.insert(item)
        return 'success'
    else:
        print('Get method')
        return 'get get'


if __name__ == '__main__':
    app.run()

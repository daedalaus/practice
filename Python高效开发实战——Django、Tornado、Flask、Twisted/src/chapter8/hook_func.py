from werkzeug.contrib.cache import SimpleCache
from flask import Flask, request, render_template

CACHE_TIMEOUT = 300

cache = SimpleCache()
cache.timeout = CACHE_TIMEOUT


app = Flask(__name__)


@app.before_request
def return_cached():
    if not request.values:
        response = cache.get(request.url0)
        if response:
            print('Got the page from cache.')
            return response
    print('Will load the page.')


@app.after_request
def cache_response(response):
    if not request.values:
        print(request.url)
        cache.set(request.url, response, CACHE_TIMEOUT)
    return response


@app.route('/get_index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis',port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as e:
            if retries == 0:
                raise e
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def index():
    count = get_hit_count()
    return f'{count}'
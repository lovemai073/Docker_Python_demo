from flask import Flask
#from redis import Redis, RedisError
import os
import socket
#import redis 

# Connect to Redis
#pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
#r = redis.Redis(connection_pool=pool)

app = Flask(__name__)

@app.route("/")
def hello():
    #try:
    #    visits = r.incr("counter",22)
    #except RedisError as e:
    #    visits = e

    html = "<h3>This is web{name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           
    return html.format(name=os.getenv("NAME", "00"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
from flask import Flask
from redis import Redis
from werkzeug.routing import BaseConverter
from flask import session, redirect, url_for, escape, request
from blueprint import simple_page

app = Flask(__name__)
app.secret_key = 'some_secret'

# app.register_blueprint(simple_page)
# Blueprint can be registered many times
app.register_blueprint(simple_page, url_prefix='/pages')



# app = Flask(__name__)
# redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # redis.incr('hits')
    return 'Hello! I have been seen %s times.' % 1

@app.route('/item/<id>/')
def item(id):
	return 'this is {}'.format(id)
 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
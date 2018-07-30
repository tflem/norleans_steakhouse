from flask import Flask, render_template
app = Flask(__name__)

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from flask_moment import Moment
moment = Moment(app)

from datetime import datetime

@app.route('/')
def index():
	return render_template('index.html',
		                   current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def hello():
	return 'Hello World!'


@app.route('/shop/')
def shop():
	return 'hi user!'


@app.route('/template/')
def template():
	return render_template(['/templates/index.html'], message='Hello template!')


@app.route('/static/<path:filename>')
def send_file(filename):
	return send_from_directory('static', 'filename')


if __name__ == '__main__':
	app.run(debug=True)
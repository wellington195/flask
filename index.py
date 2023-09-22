from flask import Flask ,render_template

app =Flask(__name__)

#para rodar flask --app index run
@app.route("/")
def index(name=None):
    return render_template('home.html', name=name)


@app.route('/home/')
@app.route('/home/<name>')
def home(name=None):
    return render_template('home.html', name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
 app.run(debug=True)
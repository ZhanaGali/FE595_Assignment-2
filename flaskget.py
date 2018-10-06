##Zhana Gali FE-595-WS Assignment 2: Basic Flask
##I start with importing Flask and creating app. Then I route to URL and add parameters to generate Get and Post methods

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

##Request.method and request.form
def basic():
    if request.method == 'POST':
        if request.form['name'] and request.form['password']:
            return 'Validation successful'
        else:
            return 'Validation unsuccessful'
        return 'Thanks'

    return render_template('FlaskPostZG.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)

##Thank you
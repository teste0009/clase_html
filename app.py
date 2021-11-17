from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/oi')
def hola():
    # return 'Tudo bom. Beleza?'
    return render_template("empleado_nuevo.html")

if __name__ == '__main__':
  app.run(port=5000, debug=True)


"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "!Holaaaaaavcvcvc  Mundoooooooo¡"

if __name__ == '__main__':
    app.run(debug = True)
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def rota1():
    return 'Hello, World'

@app.route('/rota2')
def rota2():
    return

if __name__ == '__main__':
    app.run(debug=True)

